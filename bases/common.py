import datetime
import os.path
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime as dt
from utils.log_util import logger


class Base:

    def __init__(self):
        self.driver = None
        #self.driver.implicitly_wait(10)
    '''
    闭包函数的应用
    '''
    def run_time(f):
        def cal_time(*args,**kwargs):
            time1= time.time()
            r = f(*args,**kwargs)
            time2=time.time()
            print('执行操作: {}-所需时间: {} s'.format(f.__name__,round((time2-time1),4)))
            return r
        return cal_time

    def get_screen(f):
        def screen(*args,**kwargs):
            r = f(*args,**kwargs)
            driver1 =args[0].driver
            filename = int(time.time())
            #driver1.get_screenshot_as_file('../images/'+f.__name__+'screenshot-%s.png'%filename)
            file_dir = os.path.join(os.path.dirname(__file__), 'images\\screens')
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            driver1.get_screenshot_as_file(os.path.join(file_dir, 'test-{}.png'.format(str(time.time()))))
            return r
        return screen

    def attach_file(f):
        def screen(*args,**kwargs):
            r = f(*args,**kwargs)
            driver1 =args[0].driver
            filename = int(time.time())
            #driver1.get_screenshot_as_file('../images/'+f.__name__+'screenshot-%s.png'%filename)
            file_dir = os.path.join(os.path.dirname(__file__), 'images\\screens')
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            allure.attach('测试添加file','测试测试测试测试',attachment_type=allure.attachment_type.TEXT)
            #driver1.get_screenshot_as_file(os.path.join(file_dir, 'test-{}.png'.format(str(time.time()))))
            return r
        return screen

    @pytest.fixture()
    def allure_attach(self):
        yield
        file_name = dt.now().strftime('%Y%m%d%H%M%S')
        allure.attach(self.driver.get_screenshot_as_png(), file_name, attachment_type=allure.attachment_type.PNG)

    def find_element(self,locator):
        element = None
        self.element = None
        locator1 = locator[locator.find("=")+1:]
        print(locator1)
        if locator.startswith("xpath"):
            element = self.driver.find_element(By.XPATH,locator1)
        elif locator.startswith("id"):
            element =self.driver.find_element(By.ID,locator1)
        elif locator.startswith(("css")):
            element = self.driver.find_element(By.CSS_SELECTOR,locator1)
        elif locator.startswith("tag"):
            element = self.driver.find_element(By.TAG_NAME,locator1)
        elif locator.startswith("name"):
            element = self.driver.find_element(By.NAME,locator1)
        elif locator.startswith("link"):
            element = self.driver.find_element(By.LINK_TEXT,locator1)
        elif locator.startswith("part"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT,locator1)
        else:
            element = self.driver.find_element(By.XPATH,locator)
        self.element = element

        if element:
            self.driver.execute_script('arguments[0].style="background: purple"',element)
        return element

    @run_time
    def openBrower(self,br="gc"):
        if  br=="gc":
            self.driver = webdriver.Chrome()
        elif br == "ff":
            self.driver = webdriver.Firefox()
        elif br == "ie":
            self.driver = webdriver.Ie()
        else:
            print("no browers!")
        self.driver.implicitly_wait(5)

    @run_time
    def click(self,locator):
        element = self.find_element(locator)
        element.click()

    @run_time
    def input(self,locator,value):
        element = self.find_element(locator)
        element.send_keys(value)

    #@allure_attach
    @run_time
    def get_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    # @allure_attach
    @run_time
    def switch_info_iframe(self, locator):
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)

    @run_time
    def get_text(self,locator):
        element = self.find_element(locator)
        text = element.text
        return text

    def get_size(self,locator):
        element = self.find_element(locator)
        size1 = element.size
        return size1

    def get_location(self,locator):
        element = self.find_element(locator)
        location1 = element.location
        return location1

    def sleep(self,num):
        time.sleep(num)

    @run_time
    def scroll_to_window_js(self):
        self.driver.execute_script('window.scrollTo(1000,0)')

    @run_time
    def scroll_to_element_id(self,id):
        js = "var q=document.getElementById(id).scrollTop=10000"
        self.driver.execute_script(js)

    #拖动到可见的元素去
    @run_time
    def scroll_to_element(self,locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def element_is_display_locator(self,locator):
        flag = False
        try:
            element = self.find_element(locator)
            flag = element.is_displayed()
        except Exception as e:
            flag = False
        return flag

    def element_is_display(self,element):
       # element = self.find_element(locator)
        return element.is_displayed()

    def element_is_enable(self, locator):
        element = self.find_element(locator)
        return element.is_enabled()

    # 切换到指定frame，可用id属性或name属性定位
    @run_time
    def switch_to_frame(self,id):
        self.driver.switch_to.frame(id)

    # 切换回主页面，跳出frame
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def cal_distance(self, locator):
        # 拖动控件宽度
        element = self.find_element(locator)
        # 返回字典，包含height，width
        background_size = element.size
        # 计算水平移动位移
        distance = background_size['width']
        return distance

    """
    size:获取大小
    location():获取“位置”的方法
    perform(): 执行鼠标操作
    """
    def drag_and_drop_by_x(self,locator,x,y):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        #action执行操对滚动条执行移动作
        action.move_to_element(element).perform()
        time.sleep(3)
        action.click_and_hold(element).perform()
        time.sleep(3)
        action.drag_and_drop_by_offset(element,x,y).perform()

    #移动方块上，按住方块不放，移动一定距离, 作用没有drag明显
    #@get_screen
    def move_to_hold_drag(self,locator,x,y):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        #action执行操对方块执行移动作
        action.move_to_element(element).perform()
        action.click_and_hold(element).perform()
        action.move_by_offset(x,y).perform()
        #action.perform()

    def add_cookie(self):
        cookie = self.driver.get_cookies()
        #print("coookes/...........",cookie)
        #添加自定义Cookie信息，可通过该方法进行免登录
        self.driver.add_cookie(cookie)

    def save_screen_file(self):
        #base_path = os.path.dirname(os.path.abspath(__file__))
        file_dir = os.path.join(os.path.dirname(__file__), 'images\\screens')
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = dt.now().strftime('%Y%m%d%H%M%S')
        #print('.....',file_name,type(file_name))
        self.driver.save_screenshot(os.path.join(file_dir,'HHH{}.png'.format(file_name)))



    def close(self):
        self.driver.quit()
