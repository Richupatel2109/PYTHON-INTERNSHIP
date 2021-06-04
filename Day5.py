#class Demo:
    #def myfunction(self):
       #print('This is myfunction class..')

    #def show(self,name):
        #print('value is ',name)

    #def _init__(self,nm):
        #print("this is demo class..")
        #print("name is ",nm)

#d1=Demo('xyz')
#d1.myfunction()
#d1.show("Richu")

#class demo:
    #name=""
    #def func1(self):
        #print('this is normal method..') 
    #def func2(self,name):
        #self.name=name
    #def show(self):
        #print('name is',self.name)
#d1=demo()
#d1.func1()
#d1.func2('richu')
#d1.show()

#class demo:
    #def func1(self):
        #print('This is parent class method')
#class demo1(demo):
    #def func2(self):
        #print('This is child class method') 
#d1=demo1()
#d1.func1()
#d1.func2()


#class demo:
    #def __init__(self):
        #print('This is demo class')
    #def func1(self):
        #print('This is parent class method')
#class demo1(demo):
    #def __init__(self):
        #print('This is demo1 class')
    #def func2(self):
        #print('This is child class method') 
#d1=demo1()
#d1.func1()
#d1.func2()


#class demo:
    #def __init__(self):
        #print('This is demo class')
    #def func1(self):
        #print('This is parent class method')
#class demo1(demo):
    #def __init__(self):
        #print('This is demo1 class')
    #def func2(self):
        #print('This is child class method') 
#class demo2(demo1):
    #def func3(self):
        #print('This is child method of demo2 class')
#d1=demo2()
#d1.func1()
#d1.func2()
#d1.func3()


#class demo:
    #def __init__(self):
        #print('This is demo class')
    #def func1(self):
        #print('This is parent class method')
#class demo1:
    #def __init__(self):
        #print('This is demo1 class')
    #def func2(self):
        #print('This is child class method') 
#class demo2(demo,demo1):
    #def func3(self):
        #print('This is child method of demo2 class')
#d1=demo2()
#d1.func1()
#d1.func2()
#d1.func3()

#class demo:
    #def __init__(self):
        #print('This is demo class')
    #def func1(self):
        #print('This is parent class method')
#class demo1(demo):
    #def __init__(self):
        #print('This is demo1 class')
    #def func2(self):
        #print('This is child class method') 
#class demo2(demo):
    #def func3(self):
        #print('This is child method of demo2 class')
#d1=demo1()
#d1.func1()
#d1.func2()
#d2=demo2()
#d2.func1()
#d2.func3()


class demo:
    def func1(self):
        print('This is demo class')
class demo1(demo):
    def func1(self):
        print('This is demo1 csslass')
d1=demo1()
d1.func1()


