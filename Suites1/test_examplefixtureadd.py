import pytest
import allure

class Test_fight:
    @pytest.fixture()
    def determine_text(self,a):
        if not (isinstance(a,int) or isinstance(a,float)):
            return f'不是整数或浮点数{a}'
        if a < -99 or a > 99 :
            return f'超出范围{a}'
        else:
            return 'OK'

    @pytest.mark.parametrize('a,b',[[1,2],[2,3],[3,'r',],[100,100]])
    def test_add(self,a,b,determine_text):
        print(determine_text)
        if determine_text == "OK":
            #if determine_text == "OK":
            print(str(a+b))
            # else:
            #     print(f'{determine_text}')
        else:
            print(f'{determine_text}')


    # def add(self,a,b):
    #     if self.determine_text(a) == "OK":
    #         if self.determine_text(b) == "OK":
    #             return  a+b
    #         else:
    #             return f'[b]不符合条件,{self.determine_text(b)}'
    #     else:
    #         return f'[a]不符合条件,{self.determine_text(a)}'
    #
    # @pytest.mark.parametrize('data',[[1,2,3],[2,3,5],[3,'r','error'],[100,100,'error']])
    # def test_add(self,data):
    #     sum = self.add(data[0],data[1])
    #     #assert sum == data[2]
    #     print('sum...',sum)

