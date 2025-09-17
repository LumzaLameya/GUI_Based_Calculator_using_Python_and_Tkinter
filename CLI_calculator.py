def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("please select operation -\n"
      "1. ADD\n"
      "2. SUBTRACT\n"
      "3. MULTIPLY\n"
      
      "4. DIVIDE\n")

op = int(input("Select an operation(1-4): "))

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if op == 1:
    print(num1,"+",num2,"=",add(num1,num2))

elif op == 2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif op == 3:
    print(num1,"*",num2,"=",mul(num1,num2))

elif op == 4:
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("INVALID INPUT!!")