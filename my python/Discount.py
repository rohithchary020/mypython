amount=float(input(" Enter the price : "))
percentage1=20
percentage2=10
discount1= (percentage1 /100)* amount
discount2= (percentage2 /100)* amount
final_price1=(amount)-(discount1)
final_price2=(amount)-(discount2)
if amount>5000:
    print("Your price is:",final_price1)
elif amount>3000:
    print("Your price is:",final_price2)
else:
    print("no discount for that price range")