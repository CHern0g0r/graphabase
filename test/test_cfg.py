from src.cfg import CFG
from grammpy import EPS
import tempfile
from os import path
import re


lines = [['S', 'a', 'X', 'b', 'X'],
         ['S', 'a', 'Z'],
         ['X', 'a', 'Y'],
         ['X', 'b', 'Y'],
         ['X', 'eps'],
         ['X', 'c'],
         ['Y', 'X'],
         ['Z', 'Z', 'X']]

cnf_lines = ["Z Z X",
             "X eps",
             "T0 X T0",
             "T0 a",
             "T0 T0 X",
             "X c",
             "T0 b",
             "S T0 T0",
             "X T0 Y",
             "S T0 Z",
             "X T0 Y",
             "Y X"]


def test_rule_right_part():
    c = CFG()
    assert(c.rule_right_part("asdf") == "asdf")
    assert(c.rule_right_part("ASDF").__name__ == "ASDF")
    assert(c.rule_right_part("eps") == EPS)


def test_new_nonterm():
    c = CFG()
    assert (c.new_nonterm("asdf").__name__ == "asdf")
    assert (c.new_nonterm("adsf").__qualname__
            ==
            "CFG.new_nonterm.<locals>.Nonterm")


def test_new_rule():
    c = CFG()
    rule = c.new_rule(c.new_nonterm("adsf"), "asdf")
    assert (rule.__name__ == "adsf")
    assert (rule.__qualname__ == "CFG.new_rule.<locals>.MyRule")
    assert (rule.rule[0][0].__name__ == "adsf")
    assert (rule.rule[0][0].__qualname__ == "CFG.new_nonterm.<locals>.Nonterm")
    assert (rule.rule[1] == "asdf")


def test_new_term_name():
    c = CFG()
    c.symb = {'a': None, 'b': None}
    assert (c.new_term_name() not in c.symb)
    c.symb = {'T0': None, 'T1': None, 'T2': None}
    assert (c.new_term_name() not in c.symb)


def test_term_to_string():
    c = CFG()
    nonterm = c.new_nonterm("zxcv")
    nonterm1 = c.new_nonterm("zxcvs")
    assert (c.term_to_string(EPS) == "eps")
    assert (c.term_to_string("asdf") == "asdf")
    assert (c.term_to_string(nonterm) == "T0")
    c.symb["T0"] = ""
    assert (c.term_to_string(nonterm1) == "T1")


def test_parse_grammar():
    c = CFG()
    s = {'c', 'X', 'Z', 'S', 'b', 'a', 'Y'}
    c.parse_grammar(lines)
    assert (set(c.symb.keys()) == s)
    assert (len(c.nonterms) == 4)
    assert (len(c.terms) == 3)
    assert (len(c.rules) == 8)


def test_input():
    c = CFG()
    testdir = tempfile.gettempdir()
    test_keys = {'b', 'X', 'Z', 'c', 'Y', 'T0', 'a', 'S'}
    with open(path.join(testdir, 'input.txt'), 'w') as f:
        for i in cnf_lines:
            f.write(i + '\n')
    c.read_from_file(path.join(testdir, 'input.txt'))
    assert (len(c.grammar.rules) == 11)
    assert (c.symb.keys() == test_keys)
    assert (len(c.rules) == 12)
    assert (len(c.terms) == 3)
    assert (len(c.nonterms) == 5)


def test_output():
    c = CFG()
    testdir = tempfile.gettempdir()
    # with open(path.join(testdir, 'input.txt'), 'w') as f:
    #     for i in cnf_lines:
    #         f.write(i + '\n')
    # c.read_from_file(path.join(testdir, 'input.txt'))
    c.parse_grammar(lines)
    c.print_cnf(path.join(testdir, 'output.txt'))

    with open(path.join(testdir, 'output.txt')) as f:
        lines1 = map(lambda x: re.sub("\n", "", x), f.readlines())

    assert (set(lines1) == set(cnf_lines))
