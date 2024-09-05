
for i in range(1,100):
    x =2
    prime =True

    while x * x <= i:
        if i % x == 0:
            prime=False
        x+=1

    if prime and i > 1:
        print(i)