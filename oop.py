#class 
class mobile:
    brand='samsung'    #adding variable
    price='100000'
#object
phone=mobile()
print(phone.brand)    #accessing object



#__init__ constructor

 
class Mobile:
    def __init__(self): 
     print("Constructor called")    
p=Mobile()                           # (called automatically when object is created)



#add method
class user :
    def __init__(self,username,ip):
        self.name=username
        self.ip=ip

    def show(self):
        print(self.name,self.ip)

s=user('dhfk',"28.68.93")           # object
s.show()                            # method call
    

 


 #self keyword
class  example:
     a=10
     def add(self,a):
         print(a)
         print(self.a )
obj=example()
obj.add(20)            #20 10