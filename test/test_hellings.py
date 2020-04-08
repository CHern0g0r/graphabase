from src.hellings import Graph, Hellings, print_res
from src.cfg import CFG
import tempfile
from os import path

raw_graph = """0 a 1
1 a 2
2 a 0
2 b 3
3 b 2"""

graph1 = """0 a 1
1 a 2
2 b 3
3 b 4
4 c 5
4 b 2
2 c 6
6 c 7
7 c 8"""

raw_gram = """S A B
S A S1
S1 S B
A a
B b"""

gram1 = """S S a S
S S b S
S eps"""

gram2 = [['S', 'T'],
         ['S', 'P'],
         ['T', 'X', 'Y'],
         ['X', 'a', 'X', 'b'],
         ['X', 'a', 'b'],
         ['Y', 'c', 'Y'],
         ['Y', 'c'],
         ['P', 'V', 'W'],
         ['V', 'a', 'V'],
         ['V', 'a'],
         ['W', 'b', 'W', 'c'],
         ['W', 'b', 'c']]

res = {('0', 'A', '1'),
       ('1', 'A', '2'),
       ('2', 'A', '0'),
       ('2', 'B', '3'),
       ('3', 'B', '2'),
       ('3', 'S', '0'),
       ('2', 'S1', '0'),
       ('2', 'S', '1'),
       ('3', 'S1', '1'),
       ('3', 'S', '2'),
       ('2', 'S1', '2'),
       ('2', 'S', '0'),
       ('3', 'S1', '0'),
       ('3', 'S', '1'),
       ('2', 'S1', '1'),
       ('2', 'S', '2'),
       ('3', 'S1', '2')}


def test_graph_reading():
    g = Graph()
    testdir = tempfile.gettempdir()
    with open(path.join(testdir, "input.txt"), 'w') as f:
        f.write(raw_graph)
    g.read_from_file(path.join(testdir, "input.txt"))
    v = {'0', '1', '2', '3'}
    e = {('0', 'a', '1'),
         ('1', 'a', '2'),
         ('2', 'a', '0'),
         ('2', 'b', '3'),
         ('3', 'b', '2')}
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
    testdir = tempfile.gettempdir()
    gram_file = path.join(testdir, "gram.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(gram_file, 'w') as f:
        f.write(raw_gram)
    with open(graph_file, 'w') as f:
        f.write(raw_graph)
    c = CFG()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    assert (set(r) == res)


def test_hellings_2():
    testdir = tempfile.gettempdir()
    gram_file = path.join(testdir, "gram.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(gram_file, 'w') as f:
        f.write(gram1)
    with open(graph_file, 'w') as f:
        f.write(raw_graph)
    c = CFG()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    assert (len(set(res)) == 16)


def test_hellings_3():
    testdir = tempfile.gettempdir()
    gram_file = path.join(testdir, "gram.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(gram_file, 'w') as f:
        f.write("\n".join(map(lambda x: " ".join(x), gram2)))
    with open(graph_file, 'w') as f:
        f.write(graph1)
    c = CFG()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    assert (not res)


def test_hellings_empty():
    testdir = tempfile.gettempdir()
    gram_file = path.join(testdir, "gram.txt")
    graph_file = path.join(testdir, "graph.txt")
    with open(gram_file, 'w') as f:
        f.write("\n".join(map(lambda x: " ".join(x), gram2)))
    c = CFG()
    c.read_from_file(gram_file)
    g = Graph()
    g.read_from_file(graph_file)
    r = Hellings(c, g)
    res = [(a, c) for a, b, c in r if b == 'S']
    assert (not res)
