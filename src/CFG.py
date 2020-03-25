class CFG:
    def __init__(self, rules):
        self.rules = []
        self.nonterm = []
        self.term = ['eps']
        self.start_nonterm = 'S'

        for rule in rules:
            nonterm = rule.split()[0]
            expr = rule.split()[1:]
            self.add_rule(nonterm, expr)

    # def print_rules(self):
    #     for nonterm, expr in self.rules:
    #         print(nonterm, "->", ' '.join(expr))

    # def print_term(self):
    #     print("Terminals:", end=' ')
    #     for terminal in self.term:
    #         print(terminal, end=' ')
    #     print()

    # def print_nonterm(self):
    #     print("Nonterm:", end=' ')
    #     for nonterm in self.nonterm:
    #         print(nonterm, end=' ')
    #     print()

    def add_rule(self, nonterm, expr):
        if (nonterm, expr) in self.rules:
            return
        self.rules.append((nonterm, expr))
        if nonterm not in self.nonterm:
            self.nonterm.append(nonterm)
        for symb in expr:
            if symb[0].isupper():
                if symb not in self.nonterm:
                    self.nonterm.append(symb)
            else:
                if symb not in self.term:
                    self.term.append(symb)

    def del_rule(self, nonterm, expr):
        self.rules.remove((nonterm, expr))

    def new_non_term(self):
        i = 0
        while 'A' + str(i) in self.nonterm:
            i += 1
        return 'A' + str(i)

    def reduce_long_rules(self):
        for nonterm, expr in self.rules:
            if len(expr) <= 2:
                continue

            last = nonterm

            for symb in expr[:len(expr) - 2]:
                new_nonterm = self.new_non_term()
                self.add_rule(last, [symb, new_nonterm])
                last = new_nonterm

            self.add_rule(last, expr[len(expr) - 2:])
            self.del_rule(nonterm, expr)

    def find_eps_prod_nonterm(self):

        eps_producing_nonterm = []

        for nonterm, expr in self.rules:
            if expr == ['eps']:
                eps_producing_nonterm.append(nonterm)

        some_left = True
        while some_left:
            some_left = False

            for nonterm, expr in self.rules:
                if nonterm in eps_producing_nonterm:
                    continue
                if all(symb in eps_producing_nonterm for symb in expr):
                    eps_producing_nonterm.append(nonterm)
                    some_left = True

        return eps_producing_nonterm

    def reduce_eps_rules(self):

        eps_producing_nonterm = self.find_eps_prod_nonterm()

        for nonterm, expr in self.rules:
            if len(expr) == 1:
                if expr[0] in eps_producing_nonterm:
                    self.add_rule(nonterm, ['eps'])
                continue

            if expr[0] in eps_producing_nonterm:
                if expr[1] in eps_producing_nonterm:
                    self.add_rule(nonterm, ['eps'])
                    self.add_rule(nonterm, [expr[0]])
                    self.add_rule(nonterm, [expr[1]])
                else:
                    self.add_rule(nonterm, [expr[1]])
            elif expr[1] in eps_producing_nonterm:
                self.add_rule(nonterm, [expr[0]])

        flag = False
        for nonterm, expr in self.rules:
            if expr == ['eps']:
                flag = True
                self.del_rule(nonterm, expr)

        if flag:
            new_s = self.new_non_term()
            self.add_rule(new_s, ['eps'])
            self.add_rule(new_s, [self.start_nonterm])
            self.start_nonterm = new_s

    def dfs(self, u, used, edges):
        used.append(u)
        for v in edges[u]:
            if v not in used:
                used = self.dfs(v, used, edges)
        return used

    def reduce_chain_rules(self):

        edges = {}

        for nonterm in self.nonterm:
            edges[nonterm] = []

        for nonterm, expr in self.rules:
            if len(expr) == 1 and expr[0] in self.nonterm:
                edges[nonterm].append(expr[0])

        reachable = {}

        for nonterm in self.nonterm:
            reachable[nonterm] = self.dfs(nonterm, [], edges)

        for nonterm in self.nonterm:
            for chain_nonterm in reachable[nonterm]:
                for nonterm, expr in self.rules:
                    if nonterm == chain_nonterm:
                        if len(expr) > 1 or expr[0] in self.term:
                            self.add_rule(nonterm, expr)

        for nonterm, expr in self.rules.copy():
            if len(expr) == 1 and expr[0] in self.nonterm:
                self.del_rule(nonterm, expr)

    def reduce_useless_nonterm(self):

        producing_nonterm = []

        for nonterm, expr in self.rules:
            if len(expr) == 1:
                if expr[0] in self.term:
                    producing_nonterm.append(nonterm)

            if len(expr) == 2:
                if expr[0] in self.term and expr[1] in self.term:
                    producing_nonterm.append(nonterm)

        some_left = True

        while some_left:
            some_left = False
            for nonterm, expr in self.rules:
                if nonterm in producing_nonterm:
                    continue

                if all(symb in producing_nonterm or
                       symb in self.term for symb in expr):
                    producing_nonterm.append(nonterm)
                    some_left = True

        np_nonterm = []

        for nonterm in self.nonterm:
            if nonterm not in producing_nonterm:
                np_nonterm.append(nonterm)

        for nonterm, expr in self.rules.copy():
            if nonterm in np_nonterm or any(symb in np_nonterm
                                            for symb in expr):
                self.del_rule(nonterm, expr)

        for nonterm in np_nonterm:
            self.nonterm.remove(nonterm)

    def reduce_multiple_nonterm(self):

        for nonterm, expr in self.rules.copy():
            if len(expr) == 1:
                continue

            if expr[0] in self.term:
                new_nonterm = self.new_non_term()
                self.add_rule(new_nonterm, expr[0])
            else:
                new_nonterm = expr[0]

            if expr[1] in self.term:
                new_nonterm1 = self.new_non_term()
                self.add_rule(new_nonterm1, expr[1])
            else:
                new_nonterm1 = expr[1]

            self.del_rule(nonterm, expr)
            self.add_rule(nonterm, [new_nonterm, new_nonterm1])

    def to_cnf(self):
        self.reduce_long_rules()
        self.reduce_eps_rules()
        self.reduce_chain_rules()
        self.reduce_useless_nonterm()
        self.reduce_multiple_nonterm()


def cnf_to_file(infile, outfile):
    with open(infile, "r") as in_file:
        rules = in_file.readlines()
    gram = CFG(rules)
    gram.to_cnf()
    with open(outfile, "w") as out_file:
        for nonterm, expr in gram.rules:
            out_file.write(nonterm + " " + ' '.join(expr) + '\n')
