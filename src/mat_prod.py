from weak_cfg import Weak_chom_cfg
from hellings import Graph
from scipy.sparse import csr_matrix
# import numpy as np


def matrix_from_graph(graph: Graph, gram: Weak_chom_cfg):
    r = {nont: [] for nont in gram.nonterm}
    c = {nont: [] for nont in gram.nonterm}
    data = {nont: [] for nont in gram.nonterm}
    n = len(graph.V)
    for i, mark, j in graph.E:
        for left, right in filter(lambda x:
                                  len(x[1]) == 1 and x[1][0] == mark,
                                  gram.rules):
            r[left] += [i]
            c[left] += [j]
            data[left] += [True]
    for left, right in filter(lambda x: len(x[1]) == 1 and x[1][0] == 'eps',
                              gram.rules):
        for i in range(n):
            r[left] += [i]
            c[left] += [i]
            data[left] += [True]

    return {nont: csr_matrix((data[nont], (r[nont], c[nont])),
                             shape=(n, n),
                             dtype=bool) for nont in gram.nonterm}


def eval_cfr(graph: Graph, gram: Weak_chom_cfg):
    gram.to_wcnf()
    matrices = matrix_from_graph(graph, gram)
    rules = set(filter(lambda rule: len(rule[1]) == 2, gram.rules))

    flag = True
    while flag:
        flag = False
        for left, (r1, r2) in rules:
            tmp = matrices[left] + (matrices[r1] * matrices[r2])
            if (tmp != matrices[left]).nnz > 0:
                matrices[left] = tmp
                flag = True
    return matrices


def handle_ans(res, n):
    ans = []
    for i in range(n):
        for j in range(n):
            if res['S'][i, j]:
                ans += [(i, j)]
    return ans


if __name__ == '__main__':
    # gram_file = input()
    gram_file = "/home/chernogor/Workspace/TFL/graphabase/test/res/gram4.txt"
    # graph_file = input()
    graph_file = "/home/chernogor/Workspace/TFL/graphabase/test/res/graph1.txt"
    c = Weak_chom_cfg()
    g = Graph()
    c.read_from_file(gram_file)
    g.read_from_file(graph_file)
    res = eval_cfr(g, c)
    print(handle_ans(res, len(g.V)))
