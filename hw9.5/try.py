
loserCount =10
yoniLength = 69
wornguess = input("enter num")

while(loserCount>0):
    if(int(wornguess) == yoniLength):
        break
    loserCount -=1
    wornguess = input("enter num")

if(loserCount == 0):
    print("loser")
else:
    print("winner")



