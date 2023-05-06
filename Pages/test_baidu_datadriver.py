import os
import sys
import allure
from bases.common import *
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from data.cases.read_yaml import datas

@allure.feature('测试百度')
class Test_Baidu:

    def setup_class(self):
        self.base = Base()
        #self.base.openBrower()

    @allure.story("百度用例")
    @allure.severity('normal')
    @pytest.mark.parametrize('testcases',datas['loginBaidu'])
    def test_baidu(self,testcases):
        try:
            allure.dynamic.title(testcases['title'])
            allure.dynamic.description(testcases['description'])
        except Exception as e:
            pass
        datas = testcases['cases']
        for case in datas:
            listcase = list(case.values())
            with allure.step(listcase[0]):
                func = getattr(self.base,listcase[1])
                value = listcase[2:]
                func(*value)
        #self.base.get_run_png()
     #
    # @pytest.mark.parametrize('testcases',datas['loginTaobao'])
    # def test_taobao(self,testcases):
    #     datas = testcases['cases']
    #     for case in datas:
    #         listcase = list(case.values())
    #        # print("casessss.......",listcase)
    #         func = getattr(self.base,listcase[1])
    #         value = listcase[2:]
    #         func(*value)

    # @allure.story("淘宝登录")
    # @pytest.mark.parametrize('testcases',datas)
    # def test_taobao(self,testcases):
    #     for key in datas:
    #         print('keyyy....',key)
    #         for valuep in datas[key]:
    #             #print('valuep....', valuep,'@@@')
    #             for listcase in valuep['cases']:
    #                 list1 = list(listcase.values())
    #                 print('.......',list1)
    #                 func = getattr(self.base, list1[1])
    #                 value = list1[2:]
    #                 func(*value)
