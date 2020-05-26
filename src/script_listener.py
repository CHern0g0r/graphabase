from antlr_parser.GramListener import GramListener
from weak_cfg import Weak_chom_cfg
from antlr4.tree.Tree import TerminalNodeImpl
from os import listdir
from copy import deepcopy
from hellings import Graph, Hellings
from mat_prod import eval_cfr, handle_ans
from tensor_prod import eval_tensor_cfr


class ScriptExecutor(GramListener):
    def __init__(self):
        self.gram = Weak_chom_cfg()
        self.cur_gram = None
        self.path = None
        self.graph = None
        self.edges = None
        self.algo = 'hellings'
        self.algos = {'hellings': self.query,
                      'matrix': self.mat_query,
                      'tensor': self.tens_query}
        self.commands = {'connect': self.connect,
                         'list': self.listify}
        self.l_rule = None
        self.rule = None
        self.rules = []
        self.stack = []
        self.r_stack = []
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

    def listify(self, ctx, path=None):
        if path is None:
            path = self.path
        print("\n".join(filter(lambda x: x.endswith('.txt'),
                               listdir(path))))

    def list_edges(self, path):
        graph = Graph()
        graph.read_from_file(path)
        self.edges = list(graph.labels.keys())
        return self.edges

    def pure(self):
        res = self.algos[self.algo]()
        ans = None
        if len(self.unit) == 1:
            if self.unit[0] == self.start == self.end:
                ans = {x for x, y in res if x == y}
            elif self.unit[0] == self.start:
                ans = {x for x, y in res}
            elif self.unit[0] == self.end:
                ans = {y for x, y in res}
        else:
            if self.unit[0] == self.start and self.unit[1] == self.end:
                ans = {(x, y) for x, y in res}
            elif self.unit[0] == self.end and self.unit[1] == self.start:
                ans = {(y, x) for x, y in res}
        self.query_res += [ans]
        return ans

    def exists(self):
        res = self.algos[self.algo]()
        self.query_res += [len(res) != 0]
        return self.query_res[-1]

    def count(self):
        cnt = len(self.pure())
        self.query_res.pop()
        self.query_res += [cnt]
        return cnt

    def check_id(self, ID, v):
        if ID is None:
            return True
        else:
            return ID == v

    def query(self):
        list(map(lambda x: self.cur_gram.new_rule(x[0], x[1]), self.rules))
        g = Graph()
        g.read_from_file(self.path + '/' + self.graph)
        r = Hellings(self.cur_gram, g)
        res = [(u, v) for u, N, v in r if N == self.start_nonterm]
        res = list(filter(lambda x: self.check_id(self.start_id, x[0]) and
                          self.check_id(self.end_id, x[1]), res))
        return res

    def mat_query(self):
        list(map(lambda x: self.cur_gram.new_rule(x[0], x[1]), self.rules))
        g = Graph()
        g.read_from_file(self.path + '/' + self.graph)

        matrices = eval_cfr(g, self.cur_gram)
        res = handle_ans(matrices, len(g.V), self.start_nonterm)
        res = list(filter(lambda x: self.check_id(self.start_id, x[0]) and
                          self.check_id(self.end_id, x[1]), res))
        return res

    def tens_query(self):
        list(map(lambda x: self.cur_gram.new_rule(x[0], x[1]), self.rules))
        g = Graph()
        g.read_from_file(self.path + '/' + self.graph)

        gram_lines = [(left, ' '.join(right))
                      for left, right in self.cur_gram.rules]
        r = eval_tensor_cfr(g, gram_lines, self.cur_gram)
        res = [(edge[0], edge[1]) for edge in r.edges(data='label')
               if self.start_nonterm in edge[2]]
        res = list(filter(lambda x: self.check_id(self.start_id, x[0]) and
                          self.check_id(self.end_id, x[1]), res))
        return res

    def enterStatement(self, ctx):
        command = ctx.children[0]
        if type(command) is TerminalNodeImpl:
            self.connect(ctx)

    def enterListify(self, ctx):
        if len(ctx.children) == 1:
            self.listify(ctx)
        elif len(ctx.children) == 2:
            self.listify(ctx, ctx.children[1].symbol.text[1:-1])
        else:
            print(self.list_edges(ctx.children[2].symbol.text[1:-1]))

    def enterSelect(self, ctx):
        self.graph = ctx.children[3].symbol.text[1:-1]
        self.cur_gram = deepcopy(self.gram)
        self.start_nonterm = self.cur_gram.fresh_nonterm()
        self.cur_gram.start = self.start_nonterm
        if len(ctx.children) > 6:
            self.algo = ctx.children[7].symbol.text
        self.stack.append(self.start_nonterm)
        self.rules = []

    def exitSelect(self, ctx):
        print(self.select_types[self.select_type]())
        self.cur_gram = None
        self.algo = 'helligns'
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
        # self.l_rule = ctx.children[0].symbol.text
        # self.rule = []
        self.stack.append(ctx.children[0].symbol.text)

    def exitNamed_pattern(self, ctx):
        # self.gram.new_rule(self.l_rule, self.rule)
        # self.l_rule = None
        # self.rule = None
        list(map(lambda x: self.gram.new_rule(x[0], x[1]), self.rules))
        self.stack = []
        self.rules = []

    def enterPattern(self, ctx):
        pass

    def enterAlt(self, ctx):
        fresh = self.gram.fresh_nonterm()
        self.rules.append((self.stack[-1], [fresh]))
        self.stack.append(fresh)

    def exitAlt(self, ctx):
        self.stack.pop()

    def enterSeq(self, ctx):
        if len(ctx.children) == 1:
            fresh = self.gram.fresh_nonterm()
            empty = ''
            self.rules.append((self.stack[-1], [fresh]))
            self.stack += [empty, fresh]
        else:
            fresh1 = self.gram.fresh_nonterm()
            fresh2 = self.gram.fresh_nonterm()
            self.rules.append((self.stack[-1], [fresh1, fresh2]))
            self.stack += [fresh2, fresh1]

    def exitSeq(self, ctx):
        self.stack.pop()

    def enterSubseq(self, ctx):
        fresh = self.gram.fresh_nonterm()
        if len(ctx.children) > 1:
            if ctx.children[1].symbol.text == '*':
                self.rules.append((self.stack[-1], [fresh, self.stack[-1]]))
                self.rules.append((self.stack[-1], ['eps']))
            elif ctx.children[1].symbol.text == '?':
                self.rules.append((self.stack[-1], [fresh]))
                self.rules.append((self.stack[-1], ['eps']))
            else:
                self.rules.append((self.stack[-1], [fresh, self.stack[-1]]))
                self.rules.append((self.stack[-1], [fresh]))
        else:
            self.rules.append((self.stack[-1], [fresh]))
        self.stack.append(fresh)

    def exitSubseq(self, ctx):
        self.stack.pop()
        self.stack.pop()

    def enterScoped(self, ctx):
        if len(ctx.children) == 1:
            self.rules.append((self.stack[-1], [ctx.children[0].symbol.text]))
        else:
            fresh = self.gram.fresh_nonterm()
            self.rules.append((self.stack[-1], [fresh]))
            self.stack.append(fresh)

    def exitScoped(self, ctx):
        if len(ctx.children) > 1:
            self.stack.pop()
