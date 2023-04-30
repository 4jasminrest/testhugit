#import pytest
#import allure
#import allure_pytest
#from bases.common import *
#
# class Fruit():
#     def __init__(self, name):
#         self.name = name
#         self.cubed = False
#
#     def cube(self):
#         self.cubed = True
#
#
# class FruitSalad():
#     def __init__(self, *fruit_bowl):
#         self.fruit = fruit_bowl
#         self._cube_fruit()
#
#     def _cube_fruit(self):
#         for fruit in self.fruit:
#             fruit.cube()
#
#
# @pytest.fixture()
# def fruit_bowl():
#     return [Fruit("apple"), Fruit("banana")]
#
#
# def test_fruit_salad(fruit_bowl):
#     fruit_salad = FruitSalad(*fruit_bowl)
#     assert all(fruit.cubed for fruit in fruit_salad.fruit)
import allure
import pytest
import os


@pytest.fixture()
def first_entry():
    print('before yield:first_entry')
    yield 'a'
    print('after yield:first_entry')

   # return "a"

@pytest.fixture()
def order(first_entry):
    print('before yield:order')
    yield
    print('after yield:order')

   # return [first_entry]

def test_order(order):
    print('test_order')

data = [(1,2),(3,4),(5,6)]
@pytest.fixture(params=data,ids=['a:{},b:{}'.format(a,b) for a,b in data])
def order1(request):
    return request.param

@allure.story('测试fixture函数')
@allure.severity('normal')
@allure.description('测试fixture函数，测试函数调用fixture函数，返回值转给测试函数。测试函数执行之前先执行fixture函数')
def test_order1(order1):
    print('order....', order1)
   # with allure.step('测试步骤'):


#if __name__=='__main__':
pytest.main(['test_example_fixture.py', '-s', '--alluredir', './tmp2'])
#os.system('allure generate ./tmp2 -o ./report2 --clean')