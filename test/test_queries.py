import os
import tempfile
import my_parser as mp
from weak_cfg import Weak_chom_cfg


listed = '''graph2.txt
query4.txt
gram2.txt
gram4.txt
gram3.txt
query1.txt
query3.txt
graph3.txt
query2.txt
gram1.txt
graph1.txt
gram6.txt
'''


def get_tempfile(content):
    testdir = tempfile.gettempdir()
    path = os.path.join(testdir, 'file.txt')
    with open(path, 'w') as f:
        # print(content, file=f)
        f.write(content)
    return path


def test_connect():
    path = get_tempfile('connect to "res";')
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.path == "res")


# def test_list(capsys):
#     s = 'connect to "{}";\nlist;'.format(os.path.dirname(__file__) + '/res')
#     path = get_tempfile(s)
#     tree = mp.parse_from_file(path)
#     mp.run_script(tree)
#     assert (listener.query_res == listed)


def test_named_pattern1():
    s = 'N = a N a b;'
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    rules = {('N', ('a', 'N', 'a', 'b'))}
    assert (listener.gram.rules == rules)


def test_named_pattern2():
    path = os.path.dirname(__file__) + '/res/gram1.txt'
    with open(path) as f:
        lines = f.readlines()
    data = list(map(lambda y: [y[0]] + ['='] + y[1:] + [';'],
                map(lambda x: x.split(), lines)))
    s = '\n'.join(map(lambda x: ' '.join(x), data))
    new_path = get_tempfile(s)
    tree = mp.parse_from_file(new_path)
    listener = mp.run_script(tree)
    c = Weak_chom_cfg()
    c.read_from_file(path)
    assert (c.rules == listener.gram.rules)


def test_select_1(capsys):
    path = os.path.dirname(__file__) + '/res/query4.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_2(capsys):
    path = os.path.dirname(__file__) + '/res/query5.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_3(capsys):
    path = os.path.dirname(__file__) + '/res/query6.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_4(capsys):
    path = os.path.dirname(__file__) + '/res/query7.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_5(capsys):
    path = os.path.dirname(__file__) + '/res/query8.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_6(capsys):
    path = os.path.dirname(__file__) + '/res/query9.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])
