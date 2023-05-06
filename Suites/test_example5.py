import pytest


def sum(x,y):
    return x+y

class Test_Sum:

    @pytest.mark.parametrize('x,y,z',[
        [1,1,2],
        [2,3,4],
        [3,4,7]
    ])
    def test_sum(self,x,y,z):
    #    print(2+3)
        assert  sum(x,y)==z


