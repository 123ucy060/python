#hi new update 
#encapsulation (safe )           access only inside the class
"""
class BankAccount:
    def __init__(self):
        self.__balance = 0                                # private variable(access only inside the class)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance


# ---- PROGRAM EXECUTION ----

# Create a bank account object
account = BankAccount()

# Deposit money
account.deposit(500)
account.deposit(300)

# Check balance
print("Current Balance:", account.get_balance())



#public and protected
class BankAccount:
    def __init__(self, name, balance):
        self.name = name                     # public   (access anywhere)
        self._balance = balance              # protected  (access inside class and subclasses)

    def show_balance(self):
        print("Balance:", self._balance)

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)

account = SavingsAccount("Arun", 5000)

account.show_balance()
account.deposit(2000)
account.show_balance()






#inheritance
#single inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()






#multiple inheritance
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Coding")

c = Child()
c.skill1()
c.skill2()
c.skill3()
  






#multilevel inheritance

class Grandfather:
    def land(self):
        print("Grandfather's land")

class Father(Grandfather):
    def house(self):
        print("Father's house")

class Son(Father):
    def bike(self):
        print("Son's bike")

s = Son()
s.land()
s.house()
s.bike()







#hierarchical inheritance
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def area(self):
        print("Circle area")

class Square(Shape):
    def area(self):
        print("Square area")

c = Circle()
s = Square()

c.draw()
c.area()

s.draw()
s.area()






#hybrid inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()

"""






#polymorphism   (same function,same method and different behaviour based on object)

#method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
d = Dog()

a.sound()
d.sound()
 





#method overloading
class Math:
    def add(self, a, b=0, c=0):
        print(a + b + c)

m = Math()
m.add(5)
m.add(5, 10)
m.add(5, 10, 15)





#duck typing 


#no parent-child relationship
#same method name in different classes
#if it walks like a duck and quacks like a duck, it's a duck
#we focus on what an object can do instead of class type

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)







#abstraction
""" Abstract Class Rules

Abstract class cannot create object

Must contain at least one abstract method

Child class must implement abstract methods

"""

from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod              
    def scan(self):
        pass

class PortScanner(Scanner):
    def scan(self):
        print("Scanning open ports...")

scanner = PortScanner()
scanner.scan()
