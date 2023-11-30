import random
import time
def play():
    print("Welcome. Would you like to hear the rules?")
    rulesChoice = str(input("[Y/N]"))
    if rulesChoice == "Y" or rulesChoice == "y":
        print("The rules of the game are as follows: \nYou will be given a revolver with one in the chamber. \nYou will aim this revolver at yourself. If it fires, you lose. If it does not, then you survive. \nWhile it is against the rules, you may choose to instead aim the gun at the person opposite you instead, but you had better be sure it'll fire. \nIf not, there may be some devastating consequences\n\nNote: For multiplayer, attempting to shoot the other player will result in a \"Free Shot\" if the gun does not fire.\n Accepting the free shot will allow that player to shoot the original player with no punishment.")
        singleOrMulti()
    elif rulesChoice == "N" or rulesChoice == "n":
        singleOrMulti()
    else:
        print("Sorry, that's not an option")
        play()
def singlePlayer():
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
def multiPlayer():
    barrel = [1, 0, 0, 0, 0, 0]
    playerTurn = 1
    random.shuffle(barrel)
    count = 0
    for i in range(0,6):
        print("It is now Player One's turn.")
        playerOption = int(input("Would you like to fire at yourself [1] or Player Two [2]?"))
        time.sleep(2)
        if playerOption == 1:
            if barrel[count] == 1:
                print("BANG!")
                time.sleep(1)
                print("The bullet hit player Two!")
                time.sleep(1)
                print("Player One Wins.")
                time.sleep(1)
                break
            else:
                print("Click...")
                time.sleep(1)
                print("The bullet didn't fire...")
                time.sleep(1)
                count += 1
        elif playerOption == 2:
            if barrel[count] == 1:
                print("BANG!")
                time.sleep(1)
                print("The bullet hit Player Two!")
                time.sleep(1)
                print("Player One wins.")
                time.sleep(1)
                break
            else:
                print("Click...")
                time.sleep(1)
                print("The bullet didn't fire...")
                time.sleep(1)
                print("Player Two now has the option to fire a free shot at Player One.")
                freeShot = str(input("Player Two, would you like to take the free shot? [Y/N] "))
                time.sleep(1)
                if freeShot == "Y" or freeShot == 'y':
                    count += 1
                    if barrel[count] == 1:
                        print("BANG!")
                        time.sleep(1)
                        print("The bullet hit Player One!")
                        time.sleep(1)
                        print("Player Two wins!")
                        break
                    else:
                        print("Click...")
                        time.sleep(1)
                        print("The gun didn't fire...")
                        time.sleep(1)
                        print("The game will continue.")
                        time.sleep(1)
                        count += 1
                elif freeShot == "n" or freeShot == "N":
                    count += 1
        print("It is now Player Two's turn.")
        playerOption = int(input("Would you like to fire at yourself [1] or Player One [2]?"))
        time.sleep(2)
        if playerOption == 1:
            if barrel[count] == 1:
                print("BANG!")
                time.sleep(1)
                print("The bullet hit Player One!")
                time.sleep(1)
                print("Player Two wins.")
                time.sleep(1)
                break
            else:
                print("Click...")
                time.sleep(1)
                print("The bullet didn't fire...")
                time.sleep(1)
                count += 1
        elif playerOption == 2:
            if barrel[count] == 1:
                print("BANG!")
                time.sleep(1)
                print("The bullet hit player One!")
                time.sleep(1)
                print("Player Two wins.")
                time.sleep(1)
                break
            else:
                print("Click...")
                time.sleep(1)
                print("The bullet didn't fire...")
                time.sleep(1)
                print("Player One now has the option to fire a free shot at player Two.")
                freeShot = str(input("Player One, would you like to take the free shot? [Y/N] "))
                time.sleep(1)
                if freeShot == "Y" or freeShot == 'y':
                    count += 1
                    if barrel[count] == 1:
                        print("BANG!")
                        time.sleep(1)
                        print("The bullet hit player Two!")
                        time.sleep(1)
                        print("Player One wins!")
                        break
                    else:
                        print("Click...")
                        time.sleep(1)
                        print("The gun didn't fire...")
                        time.sleep(1)
                        print("The game will continue.")
                        time.sleep(1)
                        count += 1
                elif freeShot == "N" or freeShot == 'n':
                    count += 1
def singleOrMulti():
    print("Singleplayer [1] or multiplayer? [2]")
    playingOption = int(input("[1/2]"))
    if playingOption == 1:
        singlePlayer()
    elif playingOption == 2:
        multiPlayer()
    else:
        print("Sorry, that's not an option.")
        singleOrMulti()
play()