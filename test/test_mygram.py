from src.cfg import CFG
from os import path

# c = CFG()
#     file_name = str(input())
#     c.read_from_file(file_name)
#     print(c.cyk(input().split()))

# select count ident from string where l ident r minus l r minus gt l ident r div
# nt eq ident nt ident nt alt l r div
# connect to string div


def test_mygram1():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "connect to string div"
    assert (c.cyk(query.split()))


def test_mygram2():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = ""
    assert (c.cyk(query.split()))


def test_mygram3():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "connect to string"
    assert (not c.cyk(query.split()))


def test_mygram4():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "nt eq ident nt ident nt alt l r div"
    assert (c.cyk(query.split()))


def test_mygram5():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "nt eq ident nt ident nt alt l ident r div"
    assert (c.cyk(query.split()))


def test_mygram6():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "nt eq ident nt nt alt l ident r div"
    assert (c.cyk(query.split()))


def test_mygram7():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "eq ident nt nt l ident r div"
    assert (not c.cyk(query.split()))


def test_mygram8():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "select count ident from string where \
        l ident r minus l r minus gt l ident r div"
    assert (c.cyk(query.split()))


def test_mygram9():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "select count ident\nfrom string\nwhere \
        l ident r\nminus l r minus gt l ident r div"
    assert (c.cyk(query.split()))


def test_mygram10():
    c = CFG()
    file_name = "../resources/my_gram.md"
    c.read_from_file(file_name)
    query = "select exists l ident par ident r\nfrom \
        string\nwhere l underline r\nminus nt star l l r r \
            plus ident quest alt l r minus gt l underline r div"
    assert (c.cyk(query.split()))
