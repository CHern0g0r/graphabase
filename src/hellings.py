from cfg import CFG
from grammpy import EPS


class Graph:
    V = []
    E = []
    labels = {}

    def read_from_file(self, filename):
        with open(filename) as f:
            lines = list(map(lambda x: x.split(), f.readlines()))
        for u, mark, v in lines:
            if u not in self.V:
                self.V += [u]
            if v not in self.V:
                self.V += [v]
            self.E += [(u, mark, v)]
            if mark not in self.labels:
                self.labels[mark] = []
            self.labels[mark] += [(u, v)]


def Hellings(grammar, graph):
    g = grammar.to_weak_chomsky_nf()
    m = []

    for rule in g.rules:
        l, r = rule.rule
        if r[0] == EPS:
            for v in graph.V:
                m += [(v, "eps", v)]

        if r[0] in graph.labels:
            for u, v in graph.labels[r[0]]:
                m += [(u, l[0].__name__, v)]

    ret = m.copy()
    while m:
        v, Ni, u = m.pop(0)
        for x, Nj, w in ret:
            if v != w:
                continue
            for rule in g.rules:
                l, r = rule.rule
                Nk = l[0].__name__
                if len(r) == 1:
                    continue
                r1, r2 = r[0].__name__, r[1].__name__
                if r1 != Ni or r2 != Nj:
                    continue
                add = (x, Nk, u)
                if add in ret:
                    continue
                m += [add]
                ret += [add]

        for x, Nj, w in ret:
            if x != u:
                continue
            for rule in g.rules:
                l, r = rule.rule
                Nk = l[0].__name__
                if len(r) == 1:
                    continue
                r1, r2 = r[0].__name__, r[1].__name__
                if r1 != Nj or r2 != Ni:
                    continue
                add = (v, Nk, w)
                if add in ret:
                    continue
                m += [add]
                ret += [add]
    return ret


def print_res(res_file, r):
    with open(res_file, 'a') as f:
        for u, N, v, in r:
            if N == 'S':
                print(" ".join([u, v]), file=f)


if __name__ == "__main__":
    gram_file = str(input())
    graph_file = str(input())
    res_file = str(input())
    c = CFG()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    c.print_cnf(res_file)
    print_res(res_file, r)
