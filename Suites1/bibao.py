#*********************************简单的闭包******************
def fun1(a,b=0):
    print(' fun1函数')
    print(a)
    print(b)
    #print(' fun1函数')
    def func2():
        print('func2是func1的内部函数，')
        print(a,b,c)
        return (a,b,c)  #返回值作为外部函数的返回值
    c=2
    return func2()   # return将调用func2(), 如果写return func2不执行，一定要带()


# if __name__=='__main__':
#     print(fun1(1,3))
'''打印结果：
 fun1函数
1
3
func2是func1的内部函数，
1 3 2
(1, 3, 2)

Process finished with exit code 0
'''

#*********************************装饰器@******************
def dec(f):
    print('dec闭包函数')
    f(1,2)

@dec
def fun2(a,b):
    print('修饰函数func')
    return a+b

if __name__=='__main__':
    print(fun2(1,3))

