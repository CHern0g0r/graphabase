import rdflib


def read_graph(path):
    g = rdflib.Graph()
    g.load(path)
    for s, p, o in g:
        return s
