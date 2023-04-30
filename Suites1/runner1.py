import os

import pytest

#pytest.main(["-s","test_example1.py","test_example2.py"])#逐个函数写进去 ok
#pytest.main(["test_example1.py","test_example2.py"]) #逐个函数写进去
pytest.main(['test_example_fixture.py','-s','--alluredir','./tmp1'])
os.system(('allure generate ./tmp1 -o ./report1 --clean'))
