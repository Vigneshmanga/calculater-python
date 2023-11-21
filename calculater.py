print("Enter two digits for operation")
a,b = list(map(int,input().split()))
print("mention what operation do you want to perform")
operation = input()
if (operation == "+") :
    print(a+b)
elif (operation == "-"):
    print(a-b)
elif (operation == "*"):
    print(a*b)
elif (operation == "/"):
    print(a/b)
    