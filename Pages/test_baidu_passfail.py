import os
import time
import allure
from bases.common import *
import pytest
from selenium.webdriver.common.action_chains import ActionChains
#from data.cases.read_yaml import datas

@allure.epic('测试登录的需求')
@allure.feature('测试百度模块')
class Test_Baidu:

    @allure.title('打开百度浏览器')
    def setup_class(self):
        self.base = Base()
        self.base.openBrower()

    @allure.story('测试登录')
    @allure.severity('critical')
    @allure.description('开始测试登录吧。。。。。。')
    def test_login(self):
        logger.info('测试登录成功的用例')
        self.base.get_url('https://www.baidu.com/')
        self.base.click('id=s-top-loginbtn')
        self.base.input('id=TANGRAM__PSP_11__userName','13918599078')
        self.base.input('id=TANGRAM__PSP_11__password','ywy148013@')
        self.base.click('id=TANGRAM__PSP_11__submit')
        allure.attach(self.base.driver.get_screenshot_as_png(), '用例运行截图', allure.attachment_type.PNG)
        self.base.sleep(3)
        self.base.drag_and_drop_by_x('css=.vcode-spin-button',260,0)
        self.base.sleep(3)

    @allure.story('搜索文本')
    @allure.severity('critical')
    @allure.issue('http://www.126.com')
    def test_search(self):
        with allure.step('搜索文本 '):
            logger.info('输入文本selenium')
            self.base.input('id=kw','selenium')
            logger.info('点击搜索按钮')
            self.base.click('id=su')
            #self.base.add_cookie()
            self.base.sleep(3)
        try:
            logger.info('页面内容....'+self.base.driver.page_source)
            assert 'selenium' in self.base.driver.page_source
        except Exception as e:
           # logger.info(e.args)
            pytest.fail('断言失败')
            allure.attach(self.base.driver.get_screenshot_as_png(), '用例运行截图', allure.attachment_type.PNG)

    @allure.story('登录失败')
    @allure.severity('normal')
    def test_login_failed(self):
        logger.info('测试登录失败的用例')
        with allure.step('打开网页地址'):
            self.base.get_url('https://www.baidu.com/')
        with allure.step('点击链接'):
            self.base.click('id=s-top-loginbtn')
        with allure.step('输入用户名'):
            self.base.input('id=TANGRAM__PSP_11__userName','139185990789')
        with allure.step('输入密码'):
            self.base.input('id=TANGRAM__PSP_11__password','ywy148013@')
        with allure.step('点击提交按钮'):
            self.base.click('id=TANGRAM__PSP_11__submit')
        self.base.sleep(10)
        #self.base.drag_and_drop_by_x('css=.vcode-spin-button',260,0)
      #  try:
        element = self.base.find_element('id=TANGRAM__PSP_11__error')
        self.base.sleep(5)
        with allure.step('附件文本和图片'):
            allure.attach('alert("你好呀！")','弹框',allure.attachment_type.HTML)
            allure.attach(self.base.driver.get_screenshot_as_png(), '用例运行截图', allure.attachment_type.PNG)
        errortext = '用户名或密码有误，请重新输入或找回密码'
        assert element.text == errortext

# pytest.main(['-s','test_baidu_passfail.py','--alluredir','./tmp1'])
# #pytest.main(['-s','test_baidu_datadriver.py','--reruns','2','--alluredir','./tmp'])
# os.system('allure generate ./tmp1 -o ./report1 --clean')