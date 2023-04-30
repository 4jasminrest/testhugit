import os
import yaml
from openpyxl import load_workbook


#获取文件所在的上层完整路径 C:\Users\33196\PycharmProjects\pythonProjectSelenium\data\cases
path = os.getcwd()
#path1 = os.path.dirname(os.path.abspath('cases.yaml')
with open('C:/Users/33196/PycharmProjects/pythonProjectSelenium/data/cases/cases.yaml',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
   # print('datatype',type(datas))
    baidudata = datas['loginBaidu']
    print("ddddddddd",type(baidudata),'-----------',baidudata)




# print(cases.keys())
# print(cases.values())
# print(cases.items())

