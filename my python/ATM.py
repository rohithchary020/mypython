balance=int(input("GIve your Balance: "))
w_Amount=int(input("GIve a Amount: "))


if w_Amount>balance:
    print("Insufficient Balance")
elif w_Amount<balance:
    if w_Amount%100==0:
     a_balance=balance-w_Amount
     print("your Amount is Eligible for Withdraw")
     print("Available Balance is :",a_balance)
else:
    print("invalid")
