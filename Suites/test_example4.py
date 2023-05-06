import pytest


class Test_S:
    def setup(self):
        print("setup wwwwwwwwwwwwww")

    def setup_class(self):
        print("setupggggggg class")

    @pytest.fixture()
    def mysetup(self):
        print("开始前。。。。。。")
        yield
        print("结束后。。。。。。")

    def test_01(self):
        print(" test 01 ********************")

    # fixture先于setup执行的，yield后面的后于teardown
    def test_02(self,mysetup):
        print(" test 02 ********************")

    def test_03(self):
        print(" test 03 ********************")

    def teardown(self):
        print(" teardownwwwwwwwwww    ")

    def teardown_class(self):
        print(" teardown classfffffffffffff")
