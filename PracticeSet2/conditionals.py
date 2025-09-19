age = int(input("Enter your age : "))

if(age == 0):
    print("Not a valid age !")
elif(age < 0):
    print("You cannot enter a negative age ")
elif(age >= 18 ):
    print("You can Vote for Rights")
else:
    print("You cant vote ! ")            