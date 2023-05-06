import sys
import pytest

def test_zhuang(a,b):
    print(a)
    print(b)
    def func():
        print('内部函数，闭包函数 ',a)
    print('外部函数，闭包函数 ',a)
    return func


pytest.main(['-s','test_zhuangshiqi.py'])

