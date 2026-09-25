import pytest

@pytest.mark.parametrize("n,expected",[(1,2),(3,4)])
class TestClass:
    def test_simple_case(self,n,expected):
        assert n == expected

    def tese_werid_simple_case(self,n,expected):
        assert (n*1)+1 == expected