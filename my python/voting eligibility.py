name = input("Enter name: ")
gender = input("Enter gender: ")
age = int(input("Enter age: "))
if age>18 and gender=="female":
    print("eligiblr to vite")
elif age>=60:
    print("eligible to vote")
elif age>=30 and gender=="male":
    print("eligible to vote")
else:
    print("not eligible to vote")
    

