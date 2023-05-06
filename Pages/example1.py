from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By

class Comm:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get("http://www.taobao.com")
        self.driver.find_element(By.XPATH,'//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
        print("login ok")

    def search(self):
        self.driver.get("http://www.taobao.com")
        input_phone = self.driver.find_element(By.XPATH,'//*[@id="q"]')
        input_phone.send_keys("nova9")
        self.driver.find_element(By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button').click()
        print("search ok")


if __name__=="__main__":
    comm = Comm()
    comm.search()
    comm.login()


