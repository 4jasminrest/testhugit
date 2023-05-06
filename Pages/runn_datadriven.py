import pytest
import os
#pytest.main(['-s','test_baidu_datadriver.py','test_loginTaobao.py','--alluredir','./tmp'])
pytest.main(['-s','test_baidu_datadriver.py','--alluredir','./tmp'])
#pytest.main(['-s','test_baidu_datadriver.py','test_loginTaobao.py','--alluredir','./tmp'])
#pytest.main(['-s','test_baidu_datadriver.py','--reruns','2','--alluredir','./tmp'])
os.system('allure generate ./tmp -o ./report --clean')