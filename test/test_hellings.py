from src.hellings import Graph, Hellings, print_res
# from src.cfg import CFG
from src.weak_cfg import Weak_chom_cfg
import tempfile
from os import path

# raw_graph = """0 a 1
# 1 a 2
# 2 a 0
# 2 b 3
# 3 b 2"""

# graph1 = """0 a 1
# 1 a 2
# 2 b 3
# 3 b 4
# 4 c 5
# 4 b 2
# 2 c 6
# 6 c 7
# 7 c 8"""


def test_graph_reading():
    g = Graph()
    g.read_from_file(path.dirname(__file__) +
                     "/res/graph1.txt")
    v = {0, 1, 2, 3}
    e = {(0, 'a', 1),
         (1, 'a', 2),
         (2, 'a', 0),
         (2, 'b', 3),
         (3, 'b', 2)}
    assert (v == set(g.V))
    assert (e == set(g.E))


def test_print_res():
    d = [('0', 'a', '1'),
         ('1', 'a', '2'),
         ('2', 'a', '0'),
         ('2', 'b', '3'),
         ('3', 'S', '2')]
    testdir = tempfile.gettempdir()
    print_res(path.join(testdir, "o.txt"), d)
    with open(path.join(testdir, "o.txt")) as f:
        line = f.readline()
    assert (line == "3 2\n")


def test_hellings_1():
    gram_file = (path.dirname(__file__) +
                 "/res/gram4.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    ref = {(0, 'A', 1),
           (1, 'A', 2),
           (2, 'A', 0),
           (2, 'B', 3),
           (3, 'B', 2),
           (1, 'S', 3),
           (1, 'S1', 2),
           (0, 'S', 2),
           (0, 'S1', 3),
           (2, 'S', 3),
           (2, 'S1', 2),
           (1, 'S', 2),
           (1, 'S1', 3),
           (0, 'S', 3),
           (0, 'S1', 2),
           (2, 'S', 2),
           (2, 'S1', 3)}
    assert (set(r) == ref)


def test_hellings_2():
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    assert (len(set(res)) == 16)


def test_hellings_3():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    ref = {(0, 5), (1, 8), (0, 8)}
    assert (set(res) == ref)


def test_hellings_4():
    gram_file = (path.dirname(__file__) +
                 "/res/gram1.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    ref = {(1, 2), (0, 3), (1, 3), (2, 3),
           (1, 0), (0, 2), (2, 2), (1, 1),
           (0, 0), (0, 1), (2, 0), (2, 1)}
    assert (set(res) == ref)


def test_hellings_5():
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph2.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    ref = {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
           (5, 5), (6, 6), (7, 7), (8, 8), (0, 1),
           (1, 2), (2, 3), (3, 4), (4, 2), (1, 3),
           (4, 3), (2, 4), (1, 4), (3, 2), (0, 2),
           (0, 3), (0, 4)}
    assert (set(res) == ref)


def test_hellings_6():
    gram_file = (path.dirname(__file__) +
                 "/res/gram3.txt")
    graph_file = (path.dirname(__file__) +
                  "/res/graph1.txt")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    assert (not res)


def test_hellings_empty():
    testdir = tempfile.gettempdir()
    gram_file = (path.dirname(__file__) +
                 "/res/gram2.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(graph_file, 'w') as f:
        f.write("")
    c = Weak_chom_cfg()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    print(g.E)
    r = Hellings(c, g)
    assert (not r)
