from weak_cfg import Weak_chom_cfg


class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.labels = {}

    def read_from_file(self, filename):
        with open(filename) as f:
            lines = list(map(lambda x: x.split(), f.readlines()))
        for u, mark, v in lines:
            k = int(u)
            j = int(v)
            if k not in self.V:
                self.V += [k]
            if j not in self.V:
                self.V += [j]
            self.E += [(k, mark, j)]
            if mark not in self.labels:
                self.labels[mark] = []
            self.labels[mark] += [(k, j)]


def Hellings(g, graph: Graph):
    g.to_wcnf()
    m = []
    ret = []

    for rule in g.rules:
        l, r = rule
        if r[0] == "eps":
            for v in graph.V:
                m += [(v, l, v)]
                ret += [(v, l, v)]

        if r[0] in graph.labels:
            for u, v in graph.labels[r[0]]:
                m += [(u, l, v)]
                ret += [(u, l, v)]

    while m:
        v, Ni, u = m.pop(0)
        for w, Nj, pv in ret:
            if v != pv:
                continue
            for rule in g.rules:
                Nk, r = rule
                if len(r) == 1:
                    continue
                if r[0] != Nj or r[1] != Ni:
                    continue
                add = (w, Nk, u)
                if add in ret:
                    continue
                m += [add]
                ret += [add]

        for pu, Nj, w in ret:
            if pu != u:
                continue
            for rule in g.rules:
                Nk, r = rule
                if len(r) == 1:
                    continue
                if r[0] != Ni or r[1] != Nj:
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
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    c.print_cnf(res_file)
    print_res(res_file, r)
