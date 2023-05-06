import pytest
import os
#pytest.main(['-s','test_baidu_datadriver.py','test_loginTaobao.py','--alluredir','./tmp'])
pytest.main(['-s','-q','test_baidu_passfail.py','--alluredir','./tmp1'])
#pytest.main(['-s','test_baidu_datadriver.py','test_loginTaobao.py','--alluredir','./tmp'])
#pytest.main(['-s','test_baidu_datadriver.py','--reruns','2','--alluredir','./tmp'])
#os.system('allure generate ./tmp1 -o ./report1 --clean')
#os.system('allure server ./tmp1')
