discount=0.1
quantity=2000
rate=5

if quantity>1000:
    total=(quantity*rate)-(quantity*rate*discount)
    print(total)
else:
    total=(quantity*rate)
    print(total)
