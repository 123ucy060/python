#recursion
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
#count(5)
print('phonena hello hello')

#only in main file
if __name__ == "__main__":      # this line is used to print only the main file , not in another file 
    print("I am A file")        #suppose import module as this file in another file , not work after if __name__ == "__main__": 