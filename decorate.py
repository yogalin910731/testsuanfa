#闭包函数
#函数嵌套函数
#函数返回函数
#函数间有参数引用

#需要装饰器上带参数的话多嵌套一层就可以
def halo(*args,**kwargs):
    print (args)  #元祖，不可变序列，其中的元素是不能修改的，除非整体重新赋值，不能增删，访问速度快，列表不能作为字典类型中的键，而元组是可以的。
    print (kwargs["fang"]) #字典
    def testlog(demotest):#demotest对应着demo方法
        print("this is testlog beginning")
        def innertest(*args,**kwargs): #傀儡函数
            print("this is beforeexcute")
            result = demotest(*args,**kwargs)#这是方法传参
            print ("this is afterexcute")
            return result
        return innertest
    return testlog

@halo("带参数",fang=111) #装饰器传参的话多嵌套一层
def demo(testdate,pro):
    print(testdate,pro)
    print ("this is demo")

demo("123","456")

#单例模式
