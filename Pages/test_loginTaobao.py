import time
from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By
from bases.common import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_Taobao:

    def setup_class(self):
       # self.driver = webdriver.Chrome()
       # self.driver.implicitly_wait(10)
       self.base = Base()
       #self.driver = None

    def test_login(self):
        #self.base.openBrower('gc')
        self.base.get_url("http://www.taobao.com")
        self.base.click('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
        self.base.input('//*[@id="fm-login-id"]','jasmine123055')
        self.base.input('//*[@id="fm-login-password"]','838586hu')
        self.base.click('//*[@id="login-form"]/div[4]/button')
        # //*[@id="baxia-dialog-content"]
        flag = self.base.element_is_display_locator('//*[@id="baxia-dialog-content"]')

        if flag:
            self.base.switch_to_frame('baxia-dialog-content')
            #获取滚动条的大小，滚动条大小 {'height': 32, 'width': 300}，滚动条位置 {'x': 0, 'y': 0}
           # background = self.base.find_element('//*[@id="nc_1__scale_text"]/span')
            #flag = base1.element_is_display(background)
           # print('fag....',flag)
            #distance = background.size
            #action = ActionChains(self.base.driver)
            drag_distance = self.base.cal_distance('//*[@id="nc_1__scale_text"]/span')
            self.base.drag_and_drop_by_x('//span[@id="nc_1_n1z"]',300,0)
           # print("滚动条大小", drag_distance)
            #scrollTar = self.base.find_element('//span[@id="nc_1_n1z"]')

            #action.click_and_hold(scrollTar).perform()
           # action.move_by_offset(300,0).perform()
           # tar_location = scrollTar.location
           # print("滚动条大小", scrollTar.size)
           # print("滚动条位置", scrollTar.location)
            #base1.scroll_to_id()
            #开始拖动
          #  x_location = tar_location["x"]
          #  y_location = tar_location["y"]
            # 验证正确
            #action.drag_and_drop_by_offset(scrollTar,drag_distance,0).perform()
            # action.move_to_element(scrollTar)
            # action.click_and_hold(scrollTar)
            # action.move_by_offset(300,0)
            # action.perform()
           # action.drag_and_drop_by_offset(scrollTar,300,0).perform()
        time.sleep(10)


