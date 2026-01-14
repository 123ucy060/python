#import whole module (built-in module)
import math                                #each module has specific items
print(math.sqrt(16))




#Import Specific Items in the module
from math import sqrt, pi
print(sqrt(25))




#import with alias                        
import datetime as dt           #alias is a nickname of module, for example datetime as dt 
print(dt.date.today())          
#or
import datetime                 #without alias means mention full name datetime
print(datetime.date.today())  


#creating own module 
import example                  # example.py is a one of the program file , we will use file as module
example.count(4)



#import from a package
from easy.Basics import count
count(5)
"""
From package easy
go into module function
get function count
"""




import os

print(os.getcwd())        # current directory
print(os.listdir())      # files in directory
 
