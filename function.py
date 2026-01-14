"""
def scan_ip():
    print("Scanning IP...")
    print("Scan complete")
scan_ip()


#function with parameter
def user(name):
    print("hello",name)
user("pk")


#multiple parameter
def add(a, b):
    print(a+b)
add(5,10)            #or add (b=5,a=10)


#return value
def add (a,b):
    return a+b
print (add(2,3))


#default parameter
def user(name='john'):  
    print('hi',name)
user()                        
user('arun')



#global and local variable
x=8             #global
def test():
    x = 5       #local
    print(x)
test()
print(x)


 


#*args(variable positional arguments)

def add_numbers(*args):
    total = 0
    for num in args:                        # args is tuple ,only pass a value
        total += num
    return total                            # no compulsory use args, use (*)
    
print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))


#**kwargs(variable keyword arguments)

def user(**kwargs):
    for key,value in kwargs.items():        # kwargs is dictionary, pass a key and value
        print(key,value)                    # use (**)

user(name='pk',age='43')


#Combining Normal + *args + **kwargs
def process_event(event_type, *ips, **meta):
    print("Event:", event_type)
    print("IPs:", ips)
    print("Meta:", meta)

process_event(
    "BRUTE_FORCE",
    "1.1.1.1", "2.2.2.2",
    severity="HIGH",
    tool="WAF"
)


#nested functions
def outer():
    def inner():
        print('inner function')
    inner()
outer()



#recursion
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)
   


nums = [1, 2, 3]
squared = list(map(lambda x: x*x, nums))
print(squared)


nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)

"""
 
