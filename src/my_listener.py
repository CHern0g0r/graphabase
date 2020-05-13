from antlr_parser.GramListener import GramListener
from graphviz import Digraph
from antlr4.tree.Tree import TerminalNodeImpl


class CustomListener(GramListener):
    def __init__(self):
        self.dot = Digraph()
        self.cur = 0

    def add_edge(self, ctx, label):
        self.dot.node(str(id(ctx)), label)
        if ctx.children is None:
            return
        for child in ctx.children:
            if type(child) is TerminalNodeImpl:
                self.dot.node(str(id(child)), child.symbol.text)
            self.dot.edge(str(id(ctx)), str(id(child)))

    def enterFull_script(self, ctx):
        self.add_edge(ctx, 'full_script')

    # Enter a parse tree produced by GramParser#script.
    def enterScript(self, ctx):
        self.add_edge(ctx, 'script')

    def enterStatement(self, ctx):
        self.add_edge(ctx, 'statement')

    def enterSelect(self, ctx):
        self.add_edge(ctx, 'select')

    def enterObj(self, ctx):
        self.add_edge(ctx, 'obj')

    def enterUnit(self, ctx):
        self.add_edge(ctx, 'unit')

    def enterWhere_expr(self, ctx):
        self.add_edge(ctx, 'where_expr')

    def enterVert_expr(self, ctx):
        self.add_edge(ctx, 'vertex_expr')

    def enterNamed_pattern(self, ctx):
        self.add_edge(ctx, 'named_pattern')

    def enterPattern(self, ctx):
        self.add_edge(ctx, 'pattern')

    def enterAlt(self, ctx):
        self.add_edge(ctx, 'alt')

    def enterSeq(self, ctx):
        self.add_edge(ctx, 'seq')

    def enterSubseq(self, ctx):
        self.add_edge(ctx, 'subseq')

    def enterScoped(self, ctx):
        self.add_edge(ctx, 'scoped')
