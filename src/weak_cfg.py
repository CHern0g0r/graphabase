class Weak_chom_cfg:

    def __init__(self):
        self.rules = set()  # set of (str, [str])
        self.nonterm = set()  # set of str "nonterms names"
        self.cnt_nonterm = 0
        self.start = 'S'

    def print_to_file(self, filename):
        with open(filename, 'w') as f:
            for l, r in self.rules:
                print("{} {}".format(l, " ".join(r)), file=f)

    def read_from_file(self, filename):
        with open(filename) as f:
            lines = list(map(lambda x: x.split(), f.readlines()))
        self.parse_grammar(lines)

    def new_rule(self, l, r):
        self.nonterm.add(l)
        list(map(lambda x: self.nonterm.add(x),
                 filter(lambda y: y.isupper(), r)))
        self.rules.add((l, tuple(r)))

    def parse_grammar(self, lines):
        list(map(lambda x: self.new_rule(x[0], x[1:]), lines))

    def fresh_nonterm(self):
        while "T" + str(self.cnt_nonterm) in self.nonterm:
            self.cnt_nonterm += 1
        self.nonterm.add("T" + str(self.cnt_nonterm))
        if self.cnt_nonterm == 9:
            print("here")
        return "T" + str(self.cnt_nonterm)

    def del_long_rules(self):
        new_rules = set()
        for rule in self.rules:
            l, r = rule
            r = list(r)
            while len(r) > 2:
                fresh = self.fresh_nonterm()
                self.nonterm.add(fresh)
                back = r.pop()
                new_rules.add((l, (fresh, back)))
                l = fresh
            new_rules.add((l, tuple(r)))
        self.rules = new_rules

    def del_chain_rules(self):
        new_rules = set()
        ch_rules = {}
        unch_rules = {}

        for rule in self.rules:
            l, r = rule
            if len(r) == 1 and r[0] in self.nonterm:
                if l not in ch_rules:
                    ch_rules[l] = []
                ch_rules[l] += [r]
            else:
                if l not in unch_rules:
                    unch_rules[l] = []
                unch_rules[l] += [r]

        for nont in self.nonterm:
            q = [nont]
            mark = {nont}

            while q:
                cur = q.pop(0)
                if cur in unch_rules:
                    for r in unch_rules[cur]:
                        new_rules.add((nont, r))
                if cur in ch_rules:
                    for r in ch_rules[cur]:
                        if r[0] not in mark:
                            q.append(r[0])
                            mark.add(r[0])

        self.rules = new_rules

    def del_non_gen_term(self):
        gen_nonterm = set()
        ngen_nonterm = {}
        _rules = {}

        q = []

        for rule in self.rules:
            l, r = rule
            if all(map(lambda x: x.islower(), r)):
                if l not in gen_nonterm:
                    gen_nonterm.add(l)
                    q.append(l)
                if rule not in ngen_nonterm:
                    ngen_nonterm[rule] = set()
            else:
                nonterms = filter(lambda x: x.isupper(), r)
                for i in nonterms:
                    if i not in _rules:
                        _rules[i] = set()
                    _rules[i].add(rule)

                    if rule not in ngen_nonterm:
                        ngen_nonterm[rule] = set()
                    ngen_nonterm[rule].add(i)

        while q:
            cur = q.pop(0)
            if cur not in _rules:
                continue
            for rule in _rules[cur]:
                if rule in ngen_nonterm:
                    ngen_nonterm[rule].remove(cur)
                    if not ngen_nonterm[rule]:
                        left = rule[0]
                        if left not in gen_nonterm:
                            gen_nonterm.add(left)
                            q.append(left)

        self.nonterm = gen_nonterm
        gen_rules = set(filter(lambda x: not ngen_nonterm[x],
                               ngen_nonterm.keys()))
        self.rules = gen_rules

    def del_unreachable(self):
        q = [self.start]
        reachable = {self.start}

        while q:
            cur = q.pop(0)
            for l, r in filter(lambda x: x[0] == cur, self.rules):
                for nont in filter(lambda x: x.isupper(), r):
                    if nont not in reachable:
                        reachable.add(nont)
                        q.append(nont)

        self.nonterm = reachable

        self.rules = set(filter(lambda rule: rule[0] in reachable,
                                self.rules))

    def del_long_term_rules(self):
        new_rules = set()
        term_non = {}

        for rule in self.rules:
            l, r = rule
            new_r = []
            if len(r) < 2:
                new_rules.add(rule)
                continue
            for i in range(2):
                if r[i].islower():
                    if r[i] not in term_non:
                        term_non[r[i]] = self.fresh_nonterm()
                        self.nonterm.add(term_non[r[i]])
                    new_r.append(term_non[r[i]])
                else:
                    new_r.append(r[i])
            new_rules.add((l, tuple(new_r)))

        for t, nt in term_non.items():
            new_rules.add((nt, tuple(t)))
        self.rules = new_rules

    def traverse_start(self):
        new_rules = set()
        new_S = self.fresh_nonterm()

        for l, r in self.rules:
            new_l = l
            new_r = tuple(map(lambda x: x if x != 'S' else new_S, r))
            if l == 'S':
                new_l = new_S
            new_rules.add((new_l, new_r))
        new_rules.add(('S', tuple(new_S)))
        self.rules = new_rules

    def to_wcnf(self):
        self.del_long_rules()
        self.del_chain_rules()
        self.del_non_gen_term()
        self.del_unreachable()
        self.del_long_term_rules()


if __name__ == "__main__":
    c = Weak_chom_cfg()
    c.read_from_file(input("Path to grammar:\n"))
    c.to_wcnf()
    c.print_to_file(input("Path to result:\n"))
