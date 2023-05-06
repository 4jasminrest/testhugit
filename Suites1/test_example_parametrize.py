import pytest
import sys
import allure
#import request
import allure_pytest
#from bases.common import *  #加了sys.path.append，此引入不需要了，否则jenkins报错找不到bases

class Test_paramer:

    #sys.path.append('C:\\Users\\33196\\PycharmProjects\\pythonProjectSelenium\\bases')
    def add(self,x,y):
        return x+y

    @pytest.fixture()
    def verify_type(self,a):
        if not (isinstance(a,int) or isinstance(a,float)):
            return '不是数字'
        elif a < -99 or a >99:
            return '超出范围'
        else:
            return "满足条件"
    #
    # def verify(self,a,b,c,verify_type):
    #     if verify_type() == '满足条件':
    #         if self.add(a,b) == c:
    #             return '{}+{} = {},结果相等'.format(a,b,c)
    #         else:
    #             return '{}+{} = {},结果不相等'.format(a,b,c)
    #     elif verify_type == '超出范围':
    #         return '{}，超出范围'.format(a)
    #     elif verify_type == '不是数字':
    #         return '{}，不是数字'.format(a)
    #     else

    @pytest.mark.parametrize('addPara',[1,2,3],ids=['st1','sts','st3'])
    def test_parameter_list(self,addPara):
         print('\n',addPara,'type2',type(addPara),end=',')
         #assert self.add(addPara[0],addPara[1])==addPara[2]


    @pytest.mark.parametrize('addPara',[[1,2,3],[1,3,4],[2,2,4]],ids=['list1','list2','list3'])
    def test_parameter_list_list(self,addPara):
         print('\n',addPara,end=',')
         assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组
    @pytest.mark.parametrize('addPara',(1,2,3),ids=('tt1','tt2','tt3'))
    def test_parameter_tuple_single(self,addPara):
         print('\n',addPara,end=',')
        # assert self.add(addPara[0],addPara[1])==addPara[2]

    #使用元组，元素是列表
    @pytest.mark.parametrize('addPara',[[1,2,3],[1,3,4],[2,2,4]],ids=['tp1','tp2','tp3'])
    def test_parameter_tuple_list(self,addPara):
        with allure.step('传递参数是....'):
            print('\n',addPara,end=',')
        #with allure.step('传递参数是{}....'.format(addPara)):
        with allure.step('验证结果....'):
            assert self.add(addPara[0],addPara[1])==addPara[2]


pytest.main(['test_example_parametrize.py', '-s', '--alluredir', './tmp2'])