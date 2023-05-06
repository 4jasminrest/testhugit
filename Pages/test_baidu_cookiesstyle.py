import os
import time
import allure
import yaml
import sys

#sys.path.append('C:\\Users\\33196\\PycharmProjects\\pythonProjectSelenium\\bases')

from bases.common import *
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from data.cases.read_yaml import datas


@allure.feature('测试百度项目')
class Test_Baidu:
    # pth = os.getcwd()
    # print(pth)
    # sys.path.append(pth + '\\bases')

    def setup_class(self):

        self.base = Base()
       # self.base.openBrower()

    @pytest.fixture()
    def save_screen(self):
        logger.info('fixture开始，测试attach text文件')
        yield
        allure.attach('hello hello hello .....', 'testing attach', attachment_type=allure.attachment_type.TEXT)

    @allure.story('测试百度登录模块')
    @allure.title('正确登录')
    def test_login(self):
        #base = bases()
        #base.openBrower('gc')
        with allure.step('输入百度地址'):
            self.base.get_url('https://www.baidu.com/')
            logger.info('输入登录地址')
        with allure.step('点击登陆文本'):
            self.base.click('//*[@id="s-top-loginbtn"]')
            logger.info('点击登陆文本')

        #self.base.driver.implicitly_wait(10)
        with allure.step('输入用户名'):
            self.base.input('//*[@id="TANGRAM__PSP_11__userName"]','13918599078')
            logger.info('输入用户名13918599078')

        with allure.step('输入密码'):
            self.base.input('//*[@id="TANGRAM__PSP_11__password"]','ywy148013@')
            logger.info('输入密码 ywy148013')

        with allure.step('点击提交'):
            self.base.click('//*[@id="TANGRAM__PSP_11__submit"]')
            logger.info('点击提交 点击提交')
           # allure.attach.file(self.base.driver.get_screenshot_as_file('测试文件.png'),attachment_type=allure.attachment_type.TEXT)
            #allure.attach.file(self.base.save_screen_file(),attachment_type=allure.attachment_type.PNG)
            #self.base.allure_attach()
            # print('.....',file_name,type(file_name))
            #allure.attach.file(self.base.driver.save_screenshot(os.path.join(file_dir, 'HHH{}.png'.format(file_name))),'testpng',attachment_type=allure.attachment_type.PNG)
            #allure.attach('hello hello hello .....','testing attach',attachment_type=allure.attachment_type.TEXT)
           # allure.attach(self.base.driver.get_screenshot_as_png(),'test',attachment_type=allure.attachment_type.PNG)
        logger.info('保存文件')

        logger.info('线程等待')
        time.sleep(5)
        cookie = self.base.driver.get_cookies()
        with open('cookietest.yaml','w',encoding='utf-8') as f:
            logger.info("加载yaml文件")
            yaml.safe_dump(cookie,f)

    # @allure.story('测试百度搜索模块')
    # # @allure.title('搜索selenium')
    # # def test_search(self):
    # #     self.base.input('id=kw','selenium')
    # #     self.base.click('id=su')
    # #     self.base.get_run_png()
    # #
    # #     time.sleep(2)
