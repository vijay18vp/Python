num1 = int(input("Enter firt number : "))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if(num1 > num2) and (num1 > num3):
    print("num1 is greate than num2 and num3 ")
elif(num2 > num1 ) and (num2 > num3):
    print("num2 is greater than num1 and num3 ")
else:
    print("num3 is greate than num1 and num2 ")        