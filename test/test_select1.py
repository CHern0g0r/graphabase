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
                'gram8.txt',
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
                'gram7.txt',
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


def test_select_mat_1(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query4.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_mat_2(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query5.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_mat_3(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query6.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_mat_4(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query7.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_mat_5(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query8.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_mat_6(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query9.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_mat_7(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query10.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_mat_8(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query11.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 1, 2}])


def test_select_mat_9(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query12.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(0, 8), (1, 8)}])


def test_select_mat_10(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query13.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [8])


def test_select_mat_11(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query14.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [7])


def test_select_mat_12(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query15.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(9, 12), (0, 9), (5, 7), (2, 9), (4, 8)}])


def test_select_mat_13(capsys):
    path = os.path.dirname(__file__) + '/res/matrix_q/query16.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 4, 5}])


def test_select_tensor_1(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query4.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_tensor_2(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query5.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_tensor_3(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query6.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_tensor_4(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query7.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_tensor_5(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query8.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [False])


def test_select_tensor_6(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query9.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_tensor_7(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query10.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [True])


def test_select_tensor_8(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query11.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 1, 2}])


def test_select_tensor_9(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query12.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(0, 8), (1, 8)}])


def test_select_tensor_10(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query13.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [8])


def test_select_tensor_11(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query14.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [7])


def test_select_tensor_12(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query15.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{(9, 12), (0, 9), (5, 7), (2, 9), (4, 8)}])


def test_select_tensor_13(capsys):
    path = os.path.dirname(__file__) + '/res/tensor_q/query16.txt'
    tree = mp.parse_from_file(path)
    listener = mp.run_script(tree)
    assert (listener.query_res == [{0, 4, 5}])
