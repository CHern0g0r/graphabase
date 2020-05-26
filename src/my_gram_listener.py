from antlr_regex.RuleListener import RuleListener
from weak_cfg import Weak_chom_cfg


class MyRuleListener(RuleListener):
    def __init__(self, left, gram: Weak_chom_cfg):
        self.l_rule = left
        self.gram = gram
        self.rule = None
        self.rules = []
        self.stack = []

    def enterPattern(self, ctx):
        self.stack.append(self.l_rule)

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
            print(self.stack)
            self.stack.pop()
