"""
numbers = [1, 2, 3, 4]
names = ["admin", "root", "user"]
mixed = [1, "python", True, 3.14]
empty = []
print(numbers)


#indexing
ports = [22, 80, 443,45,78]

print(ports[0])  # 22
print(ports[1])  # 80

#negative indexing
print(ports[-1])  # 443


#slicing
print(ports[0:3])       # start : end
print(ports[:3])        # : start
print(ports[::2])       # :: step (starting)
print(ports[0:4:2])     # start:end:step (positive-->forward)
print(ports[-1:-4:-2])  # start:end:step (negative-->backward)


#modifying lists
ports = [22, 80, 443]
ports[1] = 8080
print(ports)


#list methods
ports.append(56)         # add one value in last
ports.extend([34,34,56]) # add multiple value
ports.insert(1,67)       # to store the value in specific index
ports.remove(8080)       # remove by value
ports.pop(0)             # remove by index
ports.index(34)          # indentify the index value in the list 
ports.sort()             # asending order
ports.reverse()          # desending order
  
print(ports)    
print(len(ports))  


#loop in list
ports = [22, 80, 443]
for port in ports:
    print(port)

"""
import copy
# list comprehension
squares = [i * i for i in range(5)]
print(squares)

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

 

#nested list
logs = [ #    0              1          2
          ["192.168.1.1", "SUCCESS","completed"],     # 0
          ["192.168.1.2", "FAILED","not completed"]   # 1
]
print(logs[1][0])


#copy
b=copy.deepcopy(logs)  #import copy
print(b)

c=b.copy()             #normal copy
print(c)





#tuple
tuple=(2,4,5,6)        #tuple is not changable ,not modify and immutable
print(tuple[1])


#single element in tuple have must comma
tup=(4,)


#only two method
t = (10, 20, 20, 30)
t.count(20)   # 2
t.index(30)   # 3


#packing and unpacking tuple
tup = (10, 20, 20, 30)
a,b,d,c=tup
print(a)





#set
ips = {"1.1.1.1", "2.2.2.2", "1.1.1.1"}  #set has no duplicate values,mutable
print(ips)


#methods in set

"""
add()	         Add one
update()         Add many
remove()	     Remove (error)
discard()	     Remove (safe)
pop()   	     Remove random
clear()        	 Empty set
union() 	     Combine
intersection()	 Common
difference()	 Unique
"""
a = {22, 80}
b = {80, 443}

print(a | b)  # Union
print(a & b)  # Intersection
print(a-b)    # Difference 22
print(b-a)    # Difference 443

 


#dictionary
user = {
    "username": "admin",
    "ip": "192.168.1.10",         #creating
    "attempts": 5
}

user["attempts"]=7                #modifing
print(user["attempts"])           #accessing


#methods in dictionary
print(user.keys() )    # All keys
print(user.values())   # All values
print(user.items() )   # (key, value) pairs


#loop in dictionary
for i,j in user.items():
    print(i,j)



   