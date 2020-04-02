from grammpy import Grammar, Nonterminal, Rule, EPS
from grammpy.transforms import ContextFree
from grammpy.exceptions import NotParsedException
from grammpy.parsers import cyk


class CFG:
    grammar = None
    symb = {}
    nonterms = {}
    terms = {}
    rules = []
    cnt = 0

    def __init__(self):
        self.grammar = None
        self.symb = {}
        self.nonterms = {}
        self.terms = {}
        self.rules = []
        self.cnt = 0

    def parse_grammar(self, lines):
        for line in lines:
            rule = []
            left = line[0]
            right = line[1:]

            if left.islower():
                return None

            if left not in self.nonterms:
                self.nonterms[left] = self.new_nonterm(left)
                self.symb[left] = left

            rule = list(map(self.rule_right_part, right))

            self.rules.append(self.new_rule(self.nonterms[left], rule))

        self.grammar = Grammar(terminals=self.terms.keys(),
                               nonterminals=self.nonterms.values(),
                               rules=self.rules,
                               start_symbol=self.nonterms['S'])

    def to_chomsky_nf(self):
        if self.grammar is None:
            return None
        return ContextFree.transform_to_chomsky_normal_form(self.grammar)

    def rule_right_part(self, expr):
        if expr == "eps":
            return EPS
        elif expr.islower():
            if expr not in self.terms:
                self.terms[expr] = expr
                self.symb[expr] = expr
            return expr
        else:
            if expr not in self.nonterms:
                self.nonterms[expr] = self.new_nonterm(expr)
                self.symb[expr] = expr
            return self.nonterms[expr]

    def cyk(self, q):
        g = ContextFree.prepare_for_cyk(self.grammar)
        try:
            cyk(g, q)
        except NotParsedException:
            return False
        return True

    def new_nonterm(self, s):
        class Nonterm(Nonterminal):
            pass
        Nonterm.__name__ = s
        return Nonterm

    def new_rule(self, l_s, r_s):
        class MyRule(Rule):
            pass

        MyRule.__name__ = l_s.__name__
        MyRule.rule = ([l_s], r_s)
        return MyRule

    def read_from_file(self, filename):
        with open(filename) as f:
            lines = list(map(lambda x: x.split(), f.readlines()))
        self.parse_grammar(lines)

    def new_term_name(self):
        while ("T" + str(self.cnt)) in self.symb:
            self.cnt += 1
        return "T" + str(self.cnt)

    def term_to_string(self, term):
        if term == EPS:
            return "eps"
        if type(term) is str:
            return term
        if term.__name__ in self.symb:
            return self.symb[term.__name__]

        self.symb[term.__name__] = self.new_term_name()
        return self.symb[term.__name__]

    def print_rule(self, rule, f):
        left, right = rule
        left = self.term_to_string(left[0])
        right = " ".join(list(map(self.term_to_string, right)))
        print(left, right, file=f)

    def print_cnf(self, filename=None):
        cnf = self.to_chomsky_nf()
        with open(filename, 'w') as f:
            list(map(lambda rule: self.print_rule(rule.rule, f), cnf.rules))


if __name__ == "__main__":
    c = CFG()
    file_name = str(input())
    c.read_from_file(file_name)
    print(c.cyk(input().split()))
