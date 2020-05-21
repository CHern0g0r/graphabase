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

check_output = {'graph2.txt',
                'query4.txt',
                'gram2.txt',
                'gram4.txt',
                'gram3.txt',
                'query5.txt',
                'query10.txt',
                'query7.txt',
                'query1.txt',
                'query8.txt',
                'query3.txt',
                'query9.txt',
                'query6.txt',
                'graph3.txt',
                'query2.txt',
                'gram1.txt',
                'graph1.txt',
                'gram6.txt',
                'graph4.txt',
                'query11.txt',
                'query12.txt',
                'query13.txt',
                'query14.txt',
                'query15.txt',
                'query16.txt'}

named_pattern1 = {('T0', ('T1', 'T2')),
                  ('N', ('T0',)),
                  ('T1', ('T3',)),
                  ('T4', ('T5',)),
                  ('T3', ('a',)),
                  ('T5', ('N',)),
                  ('T2', ('T4',))}

named_pattern3 = {('T7', ('T8', 'T7')),
                  ('T10', ('eps',)),
                  ('T4', ('eps',)),
                  ('T0', ('T1', 'T2')),
                  ('Z', ('T12',)),
                  ('T1', ('T3', 'T1')),
                  ('T10', ('T11', 'T10')),
                  ('T6', ('b',)),
                  ('T5', ('T7',)),
                  ('N', ('T9',)),
                  ('T9', ('T10',)),
                  ('T14', ('k',)),
                  ('T3', ('a',)),
                  ('T13', ('T14',)),
                  ('T1', ('eps',)),
                  ('T4', ('T6',)),
                  ('T7', ('T8',)),
                  ('T12', ('T13',)),
                  ('T11', ('Z',)),
                  ('T8', ('c',)),
                  ('N', ('T0',)),
                  ('T2', ('T4', 'T5'))}


def get_tempfile(content):
    testdir = tempfile.gettempdir()
    path = os.path.join(testdir, 'file.txt')
    with open(path, 'w') as f:
        f.write(content)
    return path


def test_connect():
    path = get_tempfile('connect to "res";')
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.path == "res")


def test_list(capsys):
    s = 'connect to "{}";\nlist;'.format(os.path.dirname(__file__) + '/res')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    mp.run_script(tree)
    output = set(filter(lambda x: x.endswith('.txt'),
                        capsys.readouterr().out.split()))
    assert (output == check_output)


def test_named_pattern1():
    s = 'N = a N;'
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.gram.rules == named_pattern1)


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
    assert (53 == len(listener.gram.rules))


def test_named_pattern3():
    s = 'N = a* b? c+ | Z*;\nZ = k;'
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.gram.rules == named_pattern3)


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


def test_select_7(capsys):
    path = os.path.dirname(__file__) + '/res/query10.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_8(capsys):
    path = os.path.dirname(__file__) + '/res/query11.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 1, 2}])


def test_select_9(capsys):
    path = os.path.dirname(__file__) + '/res/query12.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(0, 8), (1, 8)}])


def test_select_10(capsys):
    path = os.path.dirname(__file__) + '/res/query13.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [8])


def test_select_11(capsys):
    path = os.path.dirname(__file__) + '/res/query14.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [7])


def test_select_12(capsys):
    path = os.path.dirname(__file__) + '/res/query15.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(9, 12), (0, 9), (5, 7), (2, 9), (4, 8)}])


def test_select_13(capsys):
    path = os.path.dirname(__file__) + '/res/query16.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 4, 5}])
