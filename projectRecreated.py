'''
Created on Oct 20, 2018

@author: Jordan Deuley
'''

import random
import time
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication ([])
dlg = uic.loadUi("ProjectRecreated.ui")
app.exec()

docHoward = str("Unknown Man")

traitPoints = 25

playerInventory = []

def lineSkip():
    print("")


def wakeUp():
    print(str(docHoward) + ": Hello?")
    lineSkip()
    time.sleep(2)
    print(str(docHoward) + ": ......")
    lineSkip()
    time.sleep(2)
    print(str(docHoward) + ": Wake up!")
    lineSkip()
    time.sleep(3)


def userName():
    print(str(docHoward) + ": About time you woke up.")
    lineSkip()
    time.sleep(2)
    playerName = input(str(docHoward) + ": So what is your name? ")
    if playerName == "B3T4 T3ST3R":
        print("No you can't be him/her?")
        print("You are a Beta Tester!")
        print("Here take your stuff.")
    lineSkip()
    time.sleep(1)
    print("......")
    time.sleep(1)
    lineSkip()
    print("Your name is " + playerName + "? That is an odd name.")
    time.sleep(3)
    return playerName


def createStrength():
    createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    if createStrength.isdigit() == True:
        while createStrength.isdigit() == True:
            if int(createStrength) > 10 or int(createStrength) < 0:
                print("ERROR 1")
                print("You used too many points")
                createStrength = input("How strong would you say you are? From a scale 1-10." + "You have " + str(traitPoints) + " trait points remaining. ")
            elif int(createStrength) <= 10 and int(createStrength) <= traitPoints:
                print("Excellent.")
                break
            elif int(createStrength) > 10 or int(createStrength) > traitPoints:
                print("You can't beat the system, try again")
                createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
    elif createStrength.isdigit() == False:
        while createStrength.isdigit() == False:
            print("ERROR 2")
            print("User input error.")
            createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(traitPoints) + " trait points remaining. ")
            if createStrength.isdigit() == False:
                print("You can't beat the system, try again")
                createStrength = input("How strong would you say you are? From a scale 1-10. " + "You have " + str(
                    traitPoints) + " trait points remaining. ")
    return createStrength


def createSpeed():
    createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(
        traitPoints) + " trait points remaining. ")
    if createSpeed.isdigit() == True:
        while createSpeed.isdigit() == True:
            if int(createSpeed) > 10 or int(createSpeed) < 0:
                print("ERROR 1")
                print("You used too many points")
                createSpeed = input("How fast would you say you are? From a scale 1-10." + "You have " + str(
                    traitPoints) + " trait points remaining. ")
            elif int(createSpeed) <= 10 and int(createSpeed) <= traitPoints:
                print("Excellent.")
                break
            elif int(createSpeed) > 10 or int(createSpeed) > traitPoints:
                print("You can't beat the system, try again")
                createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(
                    traitPoints) + " trait points remaining. ")
    elif createSpeed.isdigit() == False:
        while createSpeed.isdigit() == False:
            print("ERROR 2")
            print("User input error.")
            createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(
                traitPoints) + " trait points remaining. ")
            if createSpeed.isdigit() == False:
                print("You can't beat the system, try again")
                createSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(
                    traitPoints) + " trait points remaining. ")
    return createSpeed


def createSmarts():
    createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(
        traitPoints) + " trait points remaining. ")
    if createSmarts.isdigit() == True:
        while createSmarts.isdigit() == True:
            if int(createSmarts) > 10 or int(createSmarts) < 0:
                print("ERROR 1")
                print("You used too many points")
                createSmarts = input("How smart would you say you are? From a scale 1-10." + "You have " + str(
                    traitPoints) + " trait points remaining. ")
            elif int(createSmarts) <= 10 and int(createSmarts) <= traitPoints:
                print("Excellent.")
                break
            elif int(createSmarts) > 10 or int(createSmarts) > traitPoints:
                print("You can't beat the system, try again")
                createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(
                    traitPoints) + " trait points remaining. ")
    elif createSmarts.isdigit() == False:
        while createSmarts.isdigit() == False:
            print("ERROR 2")
            print("User input error.")
            createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(
                traitPoints) + " trait points remaining. ")
            if createSmarts.isdigit() == False:
                print("You can't beat the system, try again")
                createSmarts = input("How smart would you say you are? From a scale 1-10. " + "You have " + str(
                    traitPoints) + " trait points remaining. ")
    return createSmarts


def createStats():
    createStats = int(userSmarts) + int(userSpeed) + int(userStrength)
    return createStats


def story1A():
        global docHoward
        print((docHoward) + ": So " + "..... " + myName + " .......")
        lineSkip()
        time.sleep(2)
        print((docHoward) + ": .....")
        time.sleep(1)
        lineSkip()
        choice1A = input(str(docHoward) + ": I should probably fill you in on some info ehh? Where should I begin?"
            "\n 1. Where am I?"
           "\n 2. Who are you?"
            "\n 3. What is going on?"
            "\n 4. I am good I already know what is happening")
        while choice1A == "1" or "2" or "3" or "4":
            if choice1A == "1":
                print("Where am I?")
                print((str(docHoward)) + ": You are in the amazing state we call: Arkansas.")
                lineSkip()
                time.sleep(4)
                print((str(
                    docHoward)) + ": We have a small little town, it does't have much. Just a market, gun store, and a couple of little houses.")
                lineSkip()
                choice1B = input(str(docHoward) + ": Anything else you want to know? \n 1. What are these shops for? \n 2. Can we talk about the other things?")
                while choice1B == "1" or "2":
                    if choice1B == "1":
                        print((str(
                            docHoward)) + ": Ahh okay. We use our market place to trade important items. You can meet everyone there.")
                        lineSkip()
                        time.sleep(3)
                        print((str(docHoward)) + ": The gun shop is run by Sheriff Banks.")
                        lineSkip()
                        time.sleep(2)
                        print(str(docHoward) + ": I recommend you go by the gun shop after you get done talking to me.")
                        lineSkip()
                        time.sleep(3)
                        choice1B = input(str( docHoward) + ": Anything else you want to know? \n 1. What are these shops for? \n 2. Can we talk about the other things?")
                    elif choice1B == "2":
                        choice1A = input(str(docHoward) + """: I should talk about other things.- Where should I begin? \n 1. Where am I? \n 2. Who are you? \n 3. What is going on? \n""")
                        break
            elif choice1A == "2":
                docHoward = str("Doctor Howard")
                print((str(docHoward)) + ": Oh! I am Doctor Howard. Doc Howard for short.")
                time.sleep(2)
                lineSkip()
                print("I used to be a doctor at Mercy Hospital before the outbreak")
                lineSkip()
                time.sleep(3)
                choice1A = input(str(docHoward) + """: That is all you really need to know about me. \n 1. Where am I? \n 2. Who are you? \n 3. What is going on? \n""")
            elif choice1A == "3":
                print((str(docHoward)) + ": There was a virus that started to make people act odd. I have been researching.")
                lineSkip()
                time.sleep(2)
                print(str(docHoward) + ": You need to be careful of these people, they may not be able to see well, but their hearing makes up for it.")
                lineSkip()
                time.sleep(3)
                print((str(docHoward)) + ": Something else I don't know if any other states, or even cities were affected.")
                lineSkip()
                time.sleep(3)
                choice1D = input(str(docHoward) + ": Anything else you want to know? \n "
                                                  "1. What do these people do that are so dangerous? \n "
                                                  "2. Is there any way to kill these people?")
                while choice1D == "1" or "2":
                    if choice1D == "1":
                        print(str(docHoward) + ": Well the infected people are very violent. They ermm. They Like to eat other .... people.")
                        time.sleep(2)
                        lineSkip()
                        print(str(docHoward) + ": It is like something from a scary movie. Who knew something like this could happen.")
                    elif choice1D == "2":
                        print(str(docHoward) + ": From what we know a good hit to the head will take them down. This is the best way to do so.")
                        lineSkip()
                        time.sleep(2)
            elif choice1A.lower() == "4":
                while choice1A.lower() == "4":
                    choice1ALeave = input(str(docHoward) + ": Are you sure, I mean you just got here? Y/N")
                    if choice1ALeave.lower() == "y":
                        lineSkip()
                        print(str(docHoward) + ": Well if you must go, please take your stuff.")
                        lineSkip()
                        time.sleep(3)
                        print("You recieved: 20 Coin")
                        lineSkip()
                        time.sleep(2)
                        playerInventory.append("20 Coin")
                        lineSkip()
                        time.sleep(1)
                        print(str(docHoward) + ": Go by the gun shop and see Sheriff Banks")
                        lineSkip()
                        time.sleep(2)

userStrength = createStrength()

print("Your Strength is " + userStrength + ".")

traitPoints = (traitPoints - int(userStrength))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userSpeed = createSpeed()

print("Your Speed is " + userSpeed + ".")

traitPoints = (traitPoints - int(userSpeed))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userSmarts = createSmarts()

print("Your Smarts is " + str(userSmarts) + ". ")

traitPoints = (traitPoints - int(userSmarts))

print("You have " + str(traitPoints) + " remaining")

lineSkip()

userStats = createStats()

traitPointsStrength = traitPoints + int(userStrength)
traitPointsSpeed = traitPoints + int(userSpeed)
traitPointsSmarts = traitPoints + int(userSmarts)

changeStats = input(
    "Would you like to change your stats? Type Y for yes and N for no. If you select No you cannot go back. ")
if changeStats.lower() == "y":
    while changeStats.lower() == "y":
        changeChoiceStats = input(
            "What stat would you like to change. Please do S for Strength, A for Speed, and I for Smarts. ")
        if changeChoiceStats.lower() == "s":
            while changeChoiceStats.lower() == "s":
                userStrength = input(
                    "How strong are you? From a scale 1-10. " + str(traitPointsStrength) + " trait points remaining. ")
                if userStrength.isdigit() == True:
                    while userStrength.isdigit() == True:
                        if int(userStrength) > 10 or int(userStrength) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userStrength = input(
                                "How strong would you say you are? From a scale 1-10." + "You have " + str(
                                    traitPointsStrength) + " trait points remaining. ")
                        elif int(userStrength) <= 10 and int(userStrength) <= traitPointsStrength:
                            print("Your new Strength is " + userStrength)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = ""
                                print(changeChoiceStats)
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()
                                break
                        elif int(userStrength) > 10 or int(userStrength) > traitPointsStrength:
                            print("You can't beat the system, try again")
                            userStrength = input(
                                "How strong would you say you are? From a scale 1-10. " + "You have " + str(
                                    traitPointsStrength) + " trait points remaining. ")
                        elif userStrength.isdigit() == False:
                            while userStrength.isdigit() == False:
                                print("ERROR 2")
                                print("User input error.")
                                userStrength = input(
                                    "How strong would you say you are? From a scale 1-10. " + "You have " + str(
                                        traitPointsStrength) + " trait points remaining. ")
        elif changeChoiceStats.lower() == "a":
            while changeChoiceStats.lower() == "a":
                userSpeed = input(
                    "How fast are you? From a scale 1-10. " + str(traitPointsSpeed) + " trait points remaining. ")
                if userSpeed.isdigit() == True:
                    while userSpeed.isdigit() == True:
                        if int(userSpeed) > 10 or int(userSpeed) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userSpeed = input("How fast would you say you are? From a scale 1-10." + "You have " + str(
                                traitPointsSpeed) + " trait points remaining. ")
                        elif int(userSpeed) <= 10 and int(userSpeed) <= traitPointsSpeed:
                            print("Your new Speed is " + userSpeed)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = input(
                                    "What stat would you like to change. Please do S for Strength, A for Speed, and I for Smarts. ")
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()
                                break
                        elif int(userSpeed) > 10 or int(userSpeed) > traitPointsSpeed:
                            print("You can't beat the system, try again")
                            userSpeed = input("How fast would you say you are? From a scale 1-10. " + "You have " + str(
                                traitPointsSpeed) + " trait points remaining. ")
                        elif userSpeed.isdigit() == False:
                            while userSpeed.isdigit() == False:
                                print("ERROR 2")
                                print("User input error.")
                                userSpeed = input(
                                    "How fast would you say you are? From a scale 1-10. " + "You have " + str(
                                        traitPointsSpeed) + " trait points remaining. ")
                                if userSpeed.isdigit() == False:
                                    print("ERROR 2")
                                    print("User input error.")
                                    userSpeed = input(
                                        "How fast would you say you are? From a scale 1-10. " + "You have " + str(
                                            traitPointsSpeed) + " trait points remaining. ")
        elif changeChoiceStats.lower() == "i":
            while changeChoiceStats.lower() == "i":
                userSmarts = input(
                    "How smart are you? From a scale 1-10. " + str(traitPointsSmarts) + " trait points remaining. ")
                if userSmarts.isdigit() == True:
                    while userSmarts.isdigit() == True:
                        if int(userSmarts) > 10 or int(userSmarts) < 0:
                            print("ERROR 1")
                            print("You used too many points")
                            userSmarts = input(
                                "How smart would you say you are? From a scale 1-10." + "You have " + str(
                                    traitPointsSmarts) + " trait points remaining. ")
                        elif int(userSmarts) <= 10 and int(userSmarts) <= traitPointsSmarts:
                            print("Your new Strength is " + userSmarts)
                            changeStats = input("Would you like to change another stat? Type Y for yes and N for no.")
                            if changeStats.lower() == "y":
                                changeChoiceStats = input(
                                    "What stat would you like to change. Please do S for Strength, A for Smarts, and I for Smarts. ")
                                break
                            elif changeStats.lower() == "n":
                                print("Okay let's get started.")
                                lineSkip()
                                time.sleep(1)
                                print("......")
                                lineSkip()
                                break
                        elif int(userSmarts) > 10 or int(userSmarts) > traitPointsSmarts:
                            print("You can't beat the system, try again")
                            userSmarts = input(
                                "How smart would you say you are? From a scale 1-10. " + "You have " + str(
                                    traitPointsSmarts) + " trait points remaining. ")
                        elif userSmarts.isdigit() == False:
                            while userSmarts.isdigit() == False:
                                print("ERROR 2")
                                print("User input error.")
                                userSmarts = input(
                                    "How smart would you say you are? From a scale 1-10. " + "You have " + str(
                                        traitPointsSmarts) + " trait points remaining. ")
                                if userSmarts.isdigit() == False:
                                    print("ERROR 2")
                                    print("User input error.")
                                    userSmarts = input(
                                        "How smart would you say you are? From a scale 1-10. " + "You have " + str(
                                            traitPointsSmarts) + " trait points remaining. ")
elif changeStats.lower() == "n":
    print("Okay let's get started.")
    lineSkip()
    time.sleep(1)
    print("......")
    lineSkip()
else:
    print("Uhh. Can you repeat that?")
    changeStats = input(
        "Would you like to change your stats? Type Y for yes and N for no. If you select No you cannot go back. ")

time.sleep(1)

wakeUp()

myName = userName()

story1A()
