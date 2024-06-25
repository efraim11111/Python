def statusCheck():
    RED = "\033[91m"
    RESET = "\033[0m"
    if(currentweakLVL>weakToDeath/2):
        print(f"{RED}watch ur strangth{RESET}")
    if (currentwaterLVL > waterToDeath / 2):
        print(f"{RED}watch ur water{RESET}")
    if(currentpathLen<currentRoberpathLen*2):
        print(f"{RED}i see u got money{RESET}")
    if(currentwaterSup<3):
        print(f"{RED}i see u got no waterrrr{RESET}")


startRoberPosition = -50

lowPathLen = 10
lowPathDbuff = 1
highPathLen =25
highPathDbuff = 3

waterToDeath = 5
weakToDeath = 5

desartLen = 70

currentwaterSup = 4
currentweakLVL = 0
currentwaterLVL = 0
currentpathLen = 0
currentRoberpathLen = startRoberPosition

player = input("A: drink\n"
               "B: lowspeed\n"
               "C: highSpeed\n"
               "D: rest\n"
               "E: pet ur F gamal\n"
               "Q: kinda Loser\n"
               "Choose an option: ").upper()


while(player != "Q"):


    if player == "A":
        print("you drink water good for u")
        currentwaterSup -= 1
        currentwaterLVL -= 2
    elif player == "B":
        print("u walk 10kl")
        currentweakLVL += lowPathDbuff
        currentwaterLVL += lowPathDbuff
        currentpathLen += lowPathLen
    elif player == "C":
        print("u walk 25kl")
        currentweakLVL += highPathDbuff
        currentwaterLVL += highPathDbuff
        currentpathLen += highPathLen
    elif player == "D":
        print("u took a shit")
        currentweakLVL -= 2
    elif player == "E":
        print(f"""
           You chose: {player}

           Current Status:
           --------------------
           Current Water Supply: {currentwaterSup}
           Current Weak Level: {currentweakLVL}
           Current Water Level: {currentwaterLVL}
           Current Path Length: {currentpathLen}
           Current Rober Path Length: {currentRoberpathLen}
           """)
    elif player :
        print("you type worng u stupid")

    currentRoberpathLen += 10
    statusCheck()

        # Check for invalid values
    if currentwaterSup == 0 or currentweakLVL >= weakToDeath or currentwaterLVL >= waterToDeath or currentRoberpathLen >=currentpathLen:
        print(currentwaterSup)
        print(" Game over!")
        break

        # Prompt the user for the next choice
    player = input("A: drink\n"
                   "B: lowspeed\n"
                   "C: highSpeed\n"
                   "D: rest\n"
                   "E: pet ur F gamal\n"
                   "Q: kinda Loser\n"
                   "Choose an option: ").upper()


