# break the looop whenever needed
for i in range(100):
    if(i == 2):
        break
    print(i)

# similarly in continue 
for i in range(80):
    if(i == 45): # here skips the value of 45 
        continue
    print(i)    