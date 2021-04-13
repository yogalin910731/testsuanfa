
#方法1
# import time
# class Singleton:
#     def testyoga(self):
#         print(111)
# test = Singleton()
#
# if __name__ == '__main__':
#     print(id(test))
#     time.sleep(2)
#     print(id(test))

#方法2

# def singleton(cls):
#     testdic={}
#     def singletontest(*args,**kwargs):
#         if cls not in testdic:
#             testdic[cls]=cls(*args, **kwargs)
#         return testdic[cls]
#     return singletontest
#
# @singleton
# class testyoga(object):
#     a=0
#     def __init__(self,x=0):
#        self.a = x
#        print ("this is 初始化方法.a的值为："+str(self.a))
#
# A1=testyoga(1)
# print(id(A1))
# A2=testyoga(2)
# print(id(A2))
# print("______________________")
# print(id(testyoga(1)))
# print(id(testyoga(2)))

#方法4   基于__new__方法实现的单例模式
import  threading
class Singleton(object):

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if  not hasattr(cls,"_instance"):
            with threading.Lock():
                Singleton._instance=super().__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)

