x=str(input("What kind of line do you want, horizontal or vertical "))
z=str(input("Please choose a character"))
y=int(input("How long would you like the line to be"))
if (x=="vertical"):
    for x in range(0,int(y)):
        print(z)
elif (x=="horizontal"):
    for x in range(0,int(y)):
        print(z, end=",")
