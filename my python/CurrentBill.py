#Electricity Bill
#Write a program to calculate electricity bill:
#For first 100 units → ₹5 per unit
#Next 100 units → ₹7 per unit
#Above 200 units → ₹10 per unit



unit=int(input("Enter the units:"))

first=unit*5
next=unit*7
above=unit*10

if unit>0 and unit<=100:
   bill=first
   print(bill)
elif unit>100 and unit<=200:
    bill=first+(next-100)
    print(bill)
elif unit>200:
    bill=first+(next-100)+(above-200)
    print(bill)
else:
    bill=0
    print(bill)
