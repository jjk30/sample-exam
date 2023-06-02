import pytest
from short_answers import p01, p02, p03, p04, p05

class TestShort:
    def test_p01(self):
        assert p01(list(range(10))) not in (42, None)

    def test_p02(self):
        assert p02() not in (42, None)

    def test_p03(self):
        assert p03() not in (42, None)

    def test_p04(self):
        assert p04() not in (42, None)

    def test_p05(self):
        assert p05() not in (42, None)
