#class 
class mobile:
    brand='samsung'    #adding variable
    price='100000'
#object
phone=mobile()
print(phone.brand)    #accessing object



#__init__ constructor

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Mobile("Samsung", 15000)
phone2 = Mobile("Apple", 70000)

print(phone1.brand )
print(phone2.brand, phone2.price)



#add method
class user :
    def __init__(self,username,ip):
        self.name=username
        self.ip=ip

    def show(self):
        print(self.name,self.ip)

s=user('dhfk',"28.68.93")           # object
s.show()                            # method call
    

 