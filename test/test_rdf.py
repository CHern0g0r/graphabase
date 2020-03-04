from rdflib import Graph, Literal, BNode, RDF, URIRef
from rdflib.namespace import FOAF


def test_simple():
    assert True


def test_parsing():
    g = Graph()
    g.parse("http://www.w3.org/2000/10/swap/test/meet/blue.rdf")
    assert (len(g) == 4)


def test_adding():

    g = Graph()
    donna = BNode()

    g.add((donna, RDF.type, FOAF.Person))
    g.add((donna, FOAF.nick, Literal("donna", lang="foo")))
    g.add((donna, FOAF.name, Literal("Donna Fales")))
    g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))

    assert g.value(donna, FOAF.nick) == Literal("donna", lang="foo")
    assert g.value(donna, FOAF.mbox) == URIRef("mailto:donna@example.org")
    assert len(g) == 4
