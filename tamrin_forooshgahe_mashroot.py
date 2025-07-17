amount=55000
if amount>50000:
    amount=int(amount-(amount*(20/100)))
    print(amount)
elif 20000<amount<50000:
     amount=int(amount-(amount*(10/100)))
     print(amount)
else :
    print(amount)


