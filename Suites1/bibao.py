def dec(f):
    print('dec闭包函数')
    f(1,2)

def fun1(a,b=0):
    print(' fun1函数')
    print(a)
    print(b)
    #print(' fun1函数')
    def func2(c):
        print('func2是func1的内部函数，')
        print(c)
    c=2
    return func2
#
# @dec
# def fun2(a,b):
#     print('修饰函数func')
#     return a+b

if __name__=='__main__':
    fun1(1,3)

