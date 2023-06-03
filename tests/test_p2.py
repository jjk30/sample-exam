import pytest
from p2_answers import f01, f02, f03, f04, f05


def test_f01():
    assert f01(list(range(10))) not in (42, None)

def test_f02():
    assert f02() not in (42, None)

def test_f03():
    assert f03() not in (42, None)

def test_f04():
    assert f04() not in (42, None)

def test_f05():
    assert f05() not in (42, None)
