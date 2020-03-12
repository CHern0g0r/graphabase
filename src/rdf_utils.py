from rdflib import Graph


def read_graph(path):
    g = Graph()
    g.load(path)
    return g


def get_labels(g: Graph):
    for s, p, o in g:
        yield p


# graph_to_dfa(read_graph(
#     "/home/chernogor/Workspace/Python/graphabase/resources/test_copy.rdf"))
