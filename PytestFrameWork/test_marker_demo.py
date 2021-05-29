import pytest


def test_s1():
    a=3
    b=3
    assert a==b,"oh nooo"
@pytest.mark.login
def test_s2():
    a=43
    b=23
    assert a==b,"On no failed"

def test_newid():
    b=789
    a=3223+b
    assert a==b,"On on fail"

