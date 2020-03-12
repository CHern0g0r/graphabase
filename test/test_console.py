import tempfile
# import unittest
import sys
from io import StringIO
from src.consoleapp import Control
from os import path

# str_const = ("<http://bigasterisk.com/foaf.rdf#drewp> " +
#              "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type> " +
#              "<http://xmlns.com/foaf/0.1/Person> .\n" +
#              '<http://bigasterisk.com/foaf.rdf#drewp> ' +
#              '<http://example.com/says> "Hello" .')

str_const = (
    """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:ns0="http://example.com/">

<foaf:Person rdf:about="http://bigasterisk.com/foaf.rdf#drewp">
    <ns0:says>Hello</ns0:says>
</foaf:Person>

</rdf:RDF>
    """
    )


def test_load_local_rdf_file():
    test_dir = tempfile.gettempdir()
    filename = path.join(test_dir, 'demo.nt')
    f = open(filename, 'w')
    f.write(str_const)
    f.close()

    c = Control()
    c.load(filename)
    assert(len(c.aut) == 71)
    assert(c.aut.accepts("http://example.com/says"))


def test_show_edge_labels():
    test_dir = tempfile.gettempdir()
    filename = path.join(test_dir, 'demo.nt')
    f = open(filename, 'w')
    f.write(str_const)
    f.close()

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output
    c = Control()
    c.load(filename)
    c.to_list()
    assert(len(captured_output.getvalue()) == 56)

    captured_output = StringIO()
    sys.stdout = captured_output


def test_intersect_regex():
    test_dir = tempfile.gettempdir()
    in_file_name = path.join(test_dir, 'demo.rdf')
    out_file_name = path.join(test_dir, 'out.dot')
    f = open(in_file_name, 'w')
    f.write(str_const)
    f.close()

    captured_output = StringIO()
    sys.stdout = captured_output

    c = Control()
    c.load(in_file_name)

    c.request("http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
              "-dot", out_file_name)
    of = open(out_file_name, 'r')
    assert(len(of.readlines()) > 2)
    of.close()

    captured_output = StringIO()
    sys.stdout = captured_output

    c.request("http://example.com/says",
              "-dot", out_file_name)
    of = open(out_file_name, 'r')
    assert(len(of.readlines()) > 2)
    of.close()

    captured_output = StringIO()
    sys.stdout = captured_output

    c.request("abacaba",
              "-dot", out_file_name)
    of = open(out_file_name, 'r')
    assert(len(of.readlines()) == 3)
    of.close()

    captured_output = StringIO()
    sys.stdout = captured_output
