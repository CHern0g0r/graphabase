from antlr_parser.GramListener import GramListener
from weak_cfg import Weak_chom_cfg
from antlr4.tree.Tree import TerminalNodeImpl
from os import listdir
from copy import deepcopy
from hellings import Graph, Hellings


class ScriptExecutor(GramListener):
    def __init__(self):
        self.gram = Weak_chom_cfg()
        self.path = None
        self.graph = None
        self.commands = {'connect': self.connect,
                         'list': self.listify}
        self.l_rule = None
        self.rule = None
        self.select_type = None
        self.select_types = {None: self.pure,
                             'exists': self.exists,
                             'count': self.count}
        self.unit = None
        self.start = None
        self.start_id = None
        self.end = None
        self.end_id = None
        self.query_res = []
        self.start_nonterm = None

    def connect(self, ctx):
        self.path = ctx.children[2].symbol.text[1:-1]

    def listify(self, ctx):
        print("\n".join(filter(lambda x: x.endswith('.txt'),
                               listdir(self.path))))

    def pure(self):
        pass

    def exists(self):
        res = self.query()
        self.query_res += [len(res) != 0]
        return self.query_res[-1]

    def count(self):
        pass

    def check_id(self, ID, v):
        if ID is None:
            return True
        else:
            return ID == v

    def query(self):
        c = deepcopy(self.gram)
        self.start_nonterm = self.gram.fresh_nonterm()
        c.new_rule(self.start_nonterm, self.rule)
        c.start = self.start_nonterm
        g = Graph()
        g.read_from_file(self.path + '/' + self.graph)
        r = Hellings(c, g)
        res = [(u, v) for u, N, v in r if N == self.start_nonterm]
        res = list(filter(lambda x: self.check_id(self.start_id, x[0]) and
                          self.check_id(self.end_id, x[1]), res))
        return res

    def enterStatement(self, ctx):
        command = ctx.children[0]
        if type(command) is TerminalNodeImpl:
            self.commands[command.symbol.text](ctx)

    def enterSelect(self, ctx):
        self.graph = ctx.children[3].symbol.text[1:-1]
        self.rule = []

    def exitSelect(self, ctx):
        print(self.select_types[self.select_type]())
        self.rule = None
        self.graph = None
        self.start = None
        self.end = None
        self.start_id = None
        self.end_id = None
        self.select_type = None
        self.unit = None
        self.start_nonterm = None

    def enterObj(self, ctx):
        if len(ctx.children) != 1:
            self.select_type = ctx.children[0].symbol.text

    def enterUnit(self, ctx):
        if len(ctx.children) == 1:
            self.unit = (ctx.children[0].symbol.text, )
        else:
            self.unit = (ctx.children[1].symbol.text,
                         ctx.children[3].symbol.text)

    def enterWhere_expr(self, ctx):
        pass

    def enterVert_expr(self, ctx):
        vert = ctx.children[0].symbol.text
        vert_id = None
        if len(ctx.children) > 1:
            vert_id = int(ctx.children[4].symbol.text)
        if self.start is None:
            self.start = vert
            self.start_id = vert_id
        else:
            self.end = vert
            self.end_id = vert_id

    def enterNamed_pattern(self, ctx):
        self.l_rule = ctx.children[0].symbol.text
        self.rule = []

    def exitNamed_pattern(self, ctx):
        self.gram.new_rule(self.l_rule, self.rule)
        self.l_rule = None
        self.rule = None

    def enterPattern(self, ctx):
        pass

    def enterAlt(self, ctx):
        pass

    def enterSeq(self, ctx):
        pass

    def enterSubseq(self, ctx):
        pass

    def enterScoped(self, ctx):
        self.rule.append(ctx.children[0].symbol.text)
