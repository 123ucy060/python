print("alue")
print(45)
print("result",5)

print("python","cyber",'security',sep="-",end="!!!")  # end--> cursor on same line ,so waiting for next print
print('success')

#variable
name="arun"
role="developer"
print(name,'\n',role,sep='')                  #print has auto space so used sep to remove default space
print(f"hi {name} your are appointed as {role}") #professional way print

value='print'  #initial assingment
value=5.6  #reassignment
print(value) #so print reassignment value


#naming conventions
user_name='hello'  #variable used for snake case
MyClass=''         #classes used for pascel case or upper camel case
CONST_VAL='3'      #constant used for upper case


#data types
count=5               #integer
cpu_storage=73.5      #float
user_name='admin'     #string
login=True,False,None #boolean ,start with capital letter
status=bool(1)        #true
status=bool(0)        #false
print(type(count))


#taking user input
a=input('enter the number')
b=input('enter the number')
print(a+b)       #this statement does not add the number ,it just concate the two input, they think its string,so typecasting is requried


#typecasting
a=int(input('enter the number '))
b=int(input('enter the number '))
print(a+b)

 
# Arithmetic operators
"""
+  addition
-  subtraction
*  multiplication
/  division
%  modulus(remainder)
** power
"""


#Assignment operators
"""
x = 10

x += 5   # x = x + 5
x -= 2
x *= 2
x /= 4

"""


#comparison operator

x = 10

print(x == 10)   # True
print(x != 5)    # True
print(x > 7)     # True
print(x < 20)    # True
print(x >= 10)   # True
print(x <= 8)    # False


#logical operator
"""
and -> both are true
or  -> anyone true
not -> opposite
"""


#recursion
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
#count(5)