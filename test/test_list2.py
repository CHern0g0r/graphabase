import my_parser as mp
import os
import tempfile


def get_tempfile(content):
    testdir = tempfile.gettempdir()
    path = os.path.join(testdir, 'file.txt')
    with open(path, 'w') as f:
        f.write(content)
    return path


def test_listify1(capsys):
    s = 'list edges "{}";'.format(os.path.dirname(__file__) + '/res/graph1.txt')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    output = set(listener.edges)
    assert (output == {'a', 'b'})


def test_listify2(capsys):
    s = 'list edges "{}";'.format(os.path.dirname(__file__) + '/res/graph2.txt')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    output = set(listener.edges)
    assert (output == {'a', 'b', 'c'})


def test_listify3(capsys):
    s = 'list edges "{}";'.format(os.path.dirname(__file__) + '/res/graph3.txt')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    output = set(listener.edges)
    assert (output == {'a', 'b', 'c'})


def test_listif4(capsys):
    s = 'list edges "{}";'.format(os.path.dirname(__file__) + '/res/graph4.txt')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    output = set(listener.edges)
    assert (output == {'a', 'b', 'c'})
