import sys
import pytest
'''
被@修饰的函数名作为装饰函数的参数传入，如果@是闭包函数，被修饰的函数的参数列表作为内部函数的参数传入。
内部函数的返回值作为被修饰函数的返回值。
闭包函数只有在return函数名时才会去执行内部函数，否则不会执行内部函数

如果有多个@修饰函数，从上到下依次执行，当进入被修饰函数调用时，需要去检查其他的@修改函数，只有当所有的修改函数都执行完场后，
才进入被修改函数内部去执行，后执行的会覆盖之前的执行结果，被修改函数只允许执行一次。

func1是被修改的函数
outer是修改函数

'''
def outer(f):
    print('outer.....',f)
    #print(b)
    def inter(a,b):
        print('inter内部函数，闭包函数 ',a)
        f(a,b)
        print('f之后,return之前，inter内部函数，闭包函数 ', a)
        return 'inter',a,b
    print('outer，闭包函数之后语句 ')
    return inter

def outer1(f):
    print('outer1.....',f)
    #print(b)
    def inter1(*args,**kwargs):
    #def inter1(a, b):
        print('inter1内部函数，闭包函数 ',args)
        f(args,kwargs)
        print('f之后,return之前，inter1内部函数，闭包函数 ', kwargs)
        return 'inter1',args,kwargs
    print('outer1，闭包函数之后语句 ')
    return inter1

@outer1
@outer
def func1(a,b=2):
    print(',,,,{}+{}...'.format(a,b),type(a),type(b))


a1 = func1(2,3)
print('....a1..',a1)


