import os

import pytest

#pytest.main(["-s","test_example1.py","test_example2.py"])#逐个函数写进去 ok
#pytest.main(["test_example1.py","test_example2.py"]) #逐个函数写进去
#失败用例重跑，没有失败的不用重跑，使用参数"--reruns",后面指定数据,如 "3"
#pytest.main(["-s","test_example1.py","--reruns","3"])
#多进程，使用参数"-n",后面指定数据,如 "2"
#pytest.main(["-s","test_example4.py"])

pytest.main(["-s","test_example5.py","-s",'--alluredir','./result'])
os.system('allure generate ./result -o ./report --clean')