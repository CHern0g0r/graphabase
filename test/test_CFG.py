from src.CFG import CFG
from src.CFG import cnf_to_file
import tempfile
from os import path

rules = ['S a X b X',
         'S a Z',
         'X a Y',
         'X b Y',
         'X eps',
         'X c',
         'Y X',
         'Z Z X']


def test_reduce_long_rules():
    gram = CFG(rules)
    gram.reduce_long_rules()

    for _, expr in gram.rules:
        assert(len(expr) <= 2)


def test_find_eps_prod_nonterm():
    gram = CFG(rules)
    eps_prod_nonterm = gram.find_eps_prod_nonterm()
    eps_prod_nonterm.sort()
    assert(eps_prod_nonterm == ['X', 'Y'])


def test_reduce_eps_rules():
    gram = CFG(rules)
    gram.reduce_eps_rules()
    cnt = 0

    for nonterm, expr in gram.rules:
        if expr == 'eps':
            assert(nonterm == gram.start_nonterm)
            cnt += 1

    assert(cnt <= 1)


def test_reduce_chain_rules():
    gram = CFG(rules)
    gram.reduce_chain_rules()

    for nonterm, expr in gram.rules:
        if len(expr) == 1:
            assert(expr[0] in gram.term)


def test_reduce_multiple_nonterm():
    gram = CFG(rules)
    gram.reduce_long_rules()
    gram.reduce_multiple_nonterm()

    for nonterm, expr in gram.rules:
        if len(expr) == 2:
            assert(expr[0] in gram.nonterm and expr[1] in gram.nonterm)


def test_reduce_useless_nonterm():
    gram = CFG(rules)
    gram.reduce_long_rules()
    gram.reduce_useless_nonterm()
    assert('Z' not in gram.nonterm)

    for nonterm, expr in gram.rules:
        assert(not 'Z' == nonterm)
        assert('Z' not in expr)


def test_to_cnf():
    gram = CFG(rules)
    gram.to_cnf()

    for nonterm, expr in gram.rules:
        assert(len(expr) <= 2)

        if len(expr) == 1:
            assert(expr[0] in gram.term)
        if len(expr) == 2:
            assert(expr[0] in gram.nonterm and expr[1] in gram.nonterm)


def test_cnf_to_file():
    test_dir = tempfile.gettempdir()
    with open(path.join(test_dir, 'in.txt'), 'w') as f:
        f.write('\n'.join(rules))

    cnf_to_file(path.join(test_dir, 'in.txt'),
                path.join(test_dir, 'out.txt'))

    with open(path.join(test_dir, 'out.txt')) as f:
        assert(f is not None)

        new_rules = f.readlines()
        gram = CFG(new_rules)

        for nonterm, expr in gram.rules:
            assert(len(expr) <= 2)

            if len(expr) == 1:
                assert(expr[0] in gram.term)
            if len(expr) == 2:
                assert(expr[0] in gram.nonterm and expr[1] in gram.nonterm)
