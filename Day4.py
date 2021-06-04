#FUNCTIONS IN PYTHON-


#no-arguement,no-retuntype

#def myfunction(name):
     #print('Hello world')
     #myfunction()
     #myfunction()


#with argument and return satement

#def myfunction(name):
     #print('name is :',name)
#myfunctiom('Richu')


#with argument and return satement

#def myfunction(name):
     #print('Hello world')
     #return name
#name=myfunction('Richu')
#print('value is ',name)


#multiple return statement

#def myfunction():
    ##name='Richu'
    #n1=10
    #return name,n1
#name,n1=myfunction()
#print('Name is',name)
#print('n1 is',n1)
 


 #simple argument

#def calsum(n1,n2):
    #print(n1+n2)
#calsum(10,20)

#default argument

#def calsum(n1=100,n2=200):
    #print(n1+n2)
#calsum(10,20)
#calsum()


#def calsum(n1,n2):
    #print(n1+n2)
#calsum(n2=10,n1=20)

#def sum(*n1):
    #sum=0
    #for i in n1:
        #sum=sum+i
    #print('ans is',sum)
#sum(10,20)
#sum(10,20,30)

#def myfunction(**arg):
     #for i,j in arg.items():
         #print(i,j)
#myfunction(name='richu',nm='hello')


#def myfunction(**arg):
     #for i,j in arg.items():
         #print(j)
#myfunction(name='richu',nm='hello')
 


import demo
name=demo.myfunction('richu')
print('name is',name)