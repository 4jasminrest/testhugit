import pytest
import allure
import allure_pytest
from bases.common import *

class Test_paramer:

    def add(self,x,y):
        return x+y
    @pytest.mark.parametrize('addPara',[1,2,3])
    def test_parameter_list(self,addPara):
         print('\n',addPara,end=',')
         #assert self.add(addPara[0],addPara[1])==addPara[2]


    @pytest.mark.parametrize('addPara',[[1,2,3],[1,3,4],[2,2,4]])
    def test_parameter_list_list(self,addPara):
         print('\n',addPara,end=',')
         assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组
    @pytest.mark.parametrize('addPara',(1,2,3))
    def test_parameter_tuple_single(self,addPara):
         print('\n',addPara,end=',')
        # assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组，元素是列表
    @pytest.mark.parametrize('addPara',([1,2,3],[1,3,4],[2,2,4]))
    def test_parameter_tuple_list(self,addPara):
         print('\n',addPara,end=',')
         assert self.add(addPara[0],addPara[1])==addPara[2]

    def setup_class(self):
        print("setup class ............")

    def teardown_class(self):
        print("teardown class............")

    def setup(self):
        print(" setup testcase ............")

    def teardown(self):
        print(" teardown testcase  ............")

def setup_module(self):
    print(" setup module ............")

def teardown_module(self):
    print(" teardown module............")

class Test_paramer1:

    def add(self,x,y):
        return x+y
    @pytest.mark.parametrize('addPara',[1,2,3])
    def test_parameter_list(self,addPara):
         print('\n',addPara,end=',')
         #assert self.add(addPara[0],addPara[1])==addPara[2]


    @pytest.mark.parametrize('addPara',[[1,2,3],[1,3,4],[2,2,4]])
    def test_parameter_list_list(self,addPara):
         print('\n',addPara,end=',')
         assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组
    @pytest.mark.parametrize('addPara',(1,2,3))
    def test_parameter_tuple_single(self,addPara):
         print('\n',addPara,end=',')
        # assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组，元素是列表
    @pytest.mark.parametrize('addPara',([1,2,3],[1,3,4],[2,2,4]))
    def test_parameter_tuple_list(self,addPara):
         print('\n',addPara,end=',')
         assert self.add(addPara[0],addPara[1])==addPara[2]