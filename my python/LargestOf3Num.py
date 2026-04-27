#Largest of Three Numbers
#Take three numbers as input and print the largest using nested if



a=float(input("enter a value : "))
b=float(input("enter b value : "))
c=float(input("enter c value : "))

if a>b:
    if a>c:
        print("A is largest")
    else:
        print("invalid")
if b>c:
    if b>a:
        print("b is largest")
    else:
        print("invalid")
if c>a:
    if c>b:
        print("c is largest")
    else:
        print("invalid")
else:
    print("equal numbers weather not to say largest value")


