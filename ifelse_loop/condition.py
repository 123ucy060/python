"""
1)if 
2)if else
3)elif
4)nested if
5)short hand if else
"""






#if 
num=12
if num>10:
    print('the number is greater than 10')


#if else
num=10
if num%2==0:
    print('even number')
else:
    print('odd number')


#elif
mark=int(input('enter the mark '))

if mark >= 80:
    print('destination')
elif mark >=60:
    print('first class')
elif mark >=40:
    print('pass')
else:
    print("fail")


#nested if
num=int(input('enter the number '))

if num > 0:
    if num>100:
        print('above hundreds value')
    else:
        print('below hundred value')
else:
    print('negative value')


#short hand if else
attempts=7
print("blocked") if attempts > 5 else print('allowed')











"""

#for
for i in range(5):    # stop
    print(i)   

for i in range(1,5):  # start,stop
    print(i)  

for i in range(1,10,2):  # start,stop,step
    print(i) 


#while
attempts=1

while attempts<=3:
    print("login attempt",attempts)
    attempts += 1

#infinte loop
#while True:
 #   print('running...')

#break
for i in range(10):
    if i==5:
        break      #stop
    print(i)


#continue
for i in range(10):
    if i==5:
        continue  #skip
    print(i)


for i in range(4):
    pass  # do nothing , no value printed ,for future use only


#nested loop
for i in range(3):
    for j in range(2):
        print(i,j)

"""