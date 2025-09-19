# for loops in Python 
for i in range (1 , 11):
    print(i)

#While loops in python
i = 0 
while i < 10:
    print(i , "Vijay")
    i = i + 1
#printing list using loops 
l = ["Vijay" , "znozxeee" , "pretty" , "workHard"]

#method1 
i = 0 
while( i < len(l)):
    print(l[i])
    i += 1 

#method2 
for i in l:
    print(i)
#it executes when for loop exhausts 
else:
    print("Done Bro ! ")    