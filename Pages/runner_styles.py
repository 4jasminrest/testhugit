import os

import pytest

pytest.main(['-s','test_baidu_cookiesstyle.py','--alluredir','./temp3'])
os.system('allure generate ./temp3 -o ./report3 --clean')