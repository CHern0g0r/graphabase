from src.hellings import Graph
import src.tensor_prod as tp
from src.weak_cfg import Weak_chom_cfg
from my_gram_parser import parse_rule
import tempfile
from os import path


def run_test(gram_file, graph_file):
    c = Weak_chom_cfg()
    with open(gram_file) as f:
        lines = f.readlines()
    lines = [(i[0], ' '.join(i[1:])) for i in map(lambda x: x.split(), lines)]
    for left, right in lines:
        rules = parse_rule(left, right, c)
        for left, right in rules:
            c.new_rule(left, right)

    g = Graph()
    g.read_from_file(graph_file)

    res = tp.eval_tensor_cfr(g, lines, c)

    ans = [(edge[0], edge[1])
           for edge in res.edges(data='label')
           if 'S' in edge[2]]

    return ans


def test_rules_to_nx():
    gram_file = (path.dirname(__file__) +
                 "/res/gram1.txt")

    with open(gram_file) as f:
        lines = f.readlines()
    lines = [(i[0], ' '.join(i[1:])) for i in map(lambda x: x.split(), lines)]
    res, b, c = tp.rules_to_nx(lines)

    ref = {('a',), ('eps',), ('b',), ('X',), ('Y',), ('Z',), ('c',)}
    n = len([res.edges[x] for x in res.edges])

    res = {tuple(res.edges[x]['label']) for x in res.edges}

    assert (n == 15)
    assert (ref == res)


def test_tens_prod_1():
    gram_file = (path.dirname(__file__) +
                 "/res/gram4.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(0, 2), (0, 3),
           (1, 2), (1, 3),
           (2, 2), (2, 3)}
    assert (set(ans) == ref)


def test_tens_prod_2():
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")

    ans = run_test(gram_file, graph_file)

    assert (len(set(ans)) == 16)


def test_tens_prod_3():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(0, 5), (1, 8), (0, 8)}
    assert (set(ans) == ref)


def test_tens_prod_4():
    gram_file = (path.dirname(__file__) +
                 "/res/gram1.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(1, 2), (0, 3), (1, 3), (2, 3),
           (1, 0), (0, 2), (2, 2), (1, 1),
           (0, 0), (0, 1), (2, 0), (2, 1)}
    assert (set(ans) == ref)


def test_tens_prod_5():
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


def test_tens_prod_6():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    ans = run_test(gram_file, graph_file)
    assert (not ans)


def test_tens_prod_7():
    gram_file = (path.dirname(__file__) +
                 "/res/gram7.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph4.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(0, 9), (2, 9), (4, 8),
           (5, 7), (9, 12)}
    assert (set(ans) == ref)


def test_tens_prod_8():
    gram_file = (path.dirname(__file__) +
                 "/res/gram8.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")

    ans = run_test(gram_file, graph_file)

    ref = {(1, 8), (0, 8), (0, 5)}
    assert (set(ans) == ref)


def test_tens_prod_empty():
    testdir = tempfile.gettempdir()
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(graph_file, 'w') as f:
        f.write("")
    ans = run_test(gram_file, graph_file)
    assert (not ans)
