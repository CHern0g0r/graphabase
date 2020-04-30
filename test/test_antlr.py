import os
import tempfile
from src.my_parser import parse_from_file


def test_parse_from_file1():
    path = os.path.dirname(__file__) + '/res/query1.txt'
    res = parse_from_file(path)
    assert (res)


def test_parse_from_file2():
    path = os.path.dirname(__file__) + '/res/query2.txt'
    res = parse_from_file(path)
    assert (res)


def test_parse_from_file3():
    path = os.path.dirname(__file__) + '/res/query3.txt'
    res = parse_from_file(path)
    assert (res)


def test_parse_from_file4():
    path = os.path.dirname(__file__) + '/res/query1.txt'
    with open(path) as f:
        text = f.read()
    testdir = tempfile.gettempdir()
    new_path = os.path.join(testdir, 'file.txt')
    with open(new_path, 'w') as f:
        f.write(text[:-2])
    res = parse_from_file(new_path)
    assert (not res)


def test_parse_from_file5():
    path = os.path.dirname(__file__) + '/res/query3.txt'
    with open(path) as f:
        text = f.read()
    testdir = tempfile.gettempdir()
    new_path = os.path.join(testdir, 'file.txt')
    with open(new_path, 'w') as f:
        f.write(text[:-10])
    res = parse_from_file(new_path)
    assert (not res)


def test_parse_from_file6():
    path = os.path.dirname(__file__) + '/res/query2.txt'
    testdir = tempfile.gettempdir()
    ans_path = os.path.join(testdir, 'res.txt')
    parse_from_file(path, ans_path)
    with open(ans_path) as f:
        lines = f.readlines()
    assert (len(lines) == 61)
