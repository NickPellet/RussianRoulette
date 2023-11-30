import random
import time
barrel = [1, 0, 0, 0, 0, 0]
playerTurn = 1
random.shuffle(barrel)
count = 0
for i in range(0,6):
    print("It is now your turn.")
    playerOption = int(input("Would you like to fire at yourself [1] or the other player [2]? "))
    time.sleep(1)
    if playerOption == 1:
        if barrel[count] == 1:
            print("BANG!")
            time.sleep(1)
            print("The bullet hit you!")
            time.sleep(1)
            print("You lose.")
            time.sleep(1)
            break
        else:
            print("Click...")
            time.sleep(2)
            print("The bullet didn't fire...")
            time.sleep(1)
            count += 1
    elif playerOption == 2:
        if barrel[count] == 1:
            print("BANG!")
            time.sleep(1)
            print("The bullet hit your oppenent!")
            time.sleep(1)
            print("You are the last man standing.")
            time.sleep(1)
            print("Congradulations, you win!")
            
            
            break
        else:
            print("Click...")
            time.sleep(2)
            print("The gun didn't fire.")
            time.sleep(1)
            print("Your opponent is unimmagineably angry at you for trying such a thing.")
            time.sleep(1)
            print("He stands up furiously and takes his revenge upon you.")
            time.sleep(1)
            print("You lose.")
            break
    print("It is your opponent's turn.")
    time.sleep(2)
    if barrel[count] == 1:
        print("Bang!")
        time.sleep(1)
        print("Your opponent fired at himself")
        time.sleep(1)
        print("You are the last man standing!")
        time.sleep(1)
        print("You win!")
        time.sleep(1)
        break            
    else:
        print("Click...")
        time.sleep(2)
        print("The gun didn't fire.")
        time.sleep(1)
        print("Your opponent still stands before you.")
        time.sleep(1)
        count += 1