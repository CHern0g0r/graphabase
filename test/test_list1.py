import my_parser as mp
import os
import tempfile


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


def get_tempfile(content):
    testdir = tempfile.gettempdir()
    path = os.path.join(testdir, 'file.txt')
    with open(path, 'w') as f:
        f.write(content)
    return path


def test_listify1(capsys):
    s = 'connect to "{}";\nlist;'.format(os.path.dirname(__file__) + '/res')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    mp.run_script(tree)
    output = set(filter(lambda x: x.endswith('.txt'),
                        capsys.readouterr().out.split()))
    assert (output == check_output)


def test_listify2(capsys):
    s = 'list "{}";'.format(os.path.dirname(__file__) + '/res')
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    mp.run_script(tree)
    output = set(filter(lambda x: x.endswith('.txt'),
                        capsys.readouterr().out.split()))
    assert (output == check_output)


def test_listify3(capsys):
    tmpdir = tempfile.gettempdir()
    cur_path = os.path.join(tmpdir, 'graphs')
    os.mkdir(cur_path)
    for i in range(5):
        path = os.path.join(cur_path, '{}.txt'.format(str(i)))
        with open(path, 'w') as f:
            f.write("1 a 2")
    s = 'list "{}";'.format(cur_path)
    path = get_tempfile(s)
    tree = mp.parse_from_file(path)
    mp.run_script(tree)
    output = set(filter(lambda x: x.endswith('.txt'),
                        capsys.readouterr().out.split()))
    assert (output == {'{}.txt'.format(i) for i in range(5)})
