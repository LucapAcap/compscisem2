x=int(input("Welcome to the calculator, what's your first number? "))
y=int(input("What is your second number? "))
z=str(input("What operation? "))
if (z=="+"):
    print(x+y)
elif (z=="-"):
    print(x-y)
elif (z=="*"):
    print(x*y)
elif (z=="/"):
    print(x/y)