num1=float(input("enter the num1: "))
num2=float(input("enter the num2: "))
operator=input("enter the operator: ")
 
if operator == "+":
    print(f"addition of two numbers is:{num1+num2}")
elif operator == "-":
        print(f"substraction of two numbers is:{num1-num2}",)
elif operator == "*":
      print(f"mul of two numbers is:{num1*num2}")
elif operator == "/":
      print(f"division of two numbers is:{num1/num2}")     
else:
      print("invalid operator")