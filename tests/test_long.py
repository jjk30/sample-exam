import pytest
from long_answers import ArrayList

class TestLong:
    def test_long_p1(self):
        l = ArrayList()
        assert l.foo('bar')
