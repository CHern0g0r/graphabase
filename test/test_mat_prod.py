from src.hellings import Graph
import src.mat_prod as mp
from src.weak_cfg import Weak_chom_cfg
import tempfile
import numpy as np
from os import path


def run_test(gram_file, graph_file):
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = mp.eval_cfr(g, c)

    n = len(g.V)
    ans = []
    for i in range(n):
        for j in range(n):
            if r['S'][i, j]:
                ans += [(i, j)]
    return ans


def test_matrix_from_graph():
    g = Graph()
    g.read_from_file(path.dirname(__file__) +
                     "/res/graph1.txt")
    c = Weak_chom_cfg()
    c.read_from_file(path.dirname(__file__) +
                     "/res/gram4.txt")
    res = mp.matrix_from_graph(g, c)
    examp = {}
    examp['A'] = np.zeros((4, 4), dtype=bool)
    examp['A'][0, 1] = True
    examp['A'][1, 2] = True
    examp['A'][2, 0] = True
    examp['S'] = np.zeros((4, 4), dtype=bool)
    examp['B'] = np.zeros((4, 4), dtype=bool)
    examp['B'][2, 3] = True
    examp['B'][3, 2] = True
    examp['S1'] = np.zeros((4, 4), dtype=bool)
    for i in res:
        assert np.array_equal(examp[i], res[i].toarray())


def test_mat_prod_1():
    gram_file = (path.dirname(__file__) +
                 "/res/gram4.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(0, 2), (0, 3),
           (1, 2), (1, 3),
           (2, 2), (2, 3)}
    assert (set(ans) == ref)


def test_mat_prod_2():
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    ans = run_test(gram_file, graph_file)

    assert (len(set(ans)) == 16)


def test_mat_prod_3():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")
    ans = run_test(gram_file, graph_file)

    ref = {(0, 5), (1, 8), (0, 8)}
    assert (set(ans) == ref)


def test_mat_prod_4():
    gram_file = (path.dirname(__file__) +
                 "/res/gram1.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(1, 2), (0, 3), (1, 3), (2, 3),
           (1, 0), (0, 2), (2, 2), (1, 1),
           (0, 0), (0, 1), (2, 0), (2, 1)}
    assert (set(ans) == ref)


def test_mat_prod_5():
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
           (5, 5), (6, 6), (7, 7), (8, 8), (0, 1),
           (1, 2), (2, 3), (3, 4), (4, 2), (1, 3),
           (4, 3), (2, 4), (1, 4), (3, 2), (0, 2),
           (0, 3), (0, 4)}
    assert (set(ans) == ref)


def test_mat_prod_6():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    ans = run_test(gram_file, graph_file)
    assert (not ans)


def test_mat_prod_empty():
    testdir = tempfile.gettempdir()
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(graph_file, 'w') as f:
        f.write("")
    ans = run_test(gram_file, graph_file)
    assert (not ans)
