import time

docHoward = str("Unknown Man")

traitPoints = 25

playerInventory = []

myName = "Jordan"


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
            choice1B = input(str(
                docHoward) + ": Anything else you want to know? "
                             "\n 1. What are these shops for? "
                             "\n 2. Can we talk about the other things?")
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
                    choice1B = input(str(
                        docHoward) + ": Anything else you want to know? "
                                     "\n 1. What are these shops for? "
                                     "\n 2. Can we talk about the other things?")
                elif choice1B == "2":
                    choice1A = input(str(
                        docHoward) + ": I should talk about other things. Where should I begin? "
                                     "\n 1. Where am I? "
                                     "\n 2. Who are you? "
                                     "\n 3. What is going on?"
                                     "\n 4. That is all. Thanks!")
                    break
        elif choice1A == "2":
            docHoward = str("Doctor Howard")
            print((str(docHoward)) + ": Oh! I am Doctor Howard. Doc Howard for short.")
            time.sleep(2)
            lineSkip()
            print("I used to be a doctor at Mercy Hospital before the outbreak")
            lineSkip()
            time.sleep(3)
            choice1A = input(str(docHoward) + ": That is all you really need to know about me. "
                                              "\n 1. Where am I?"
                                              "\n 2. Who are you?"
                                              "\n 3. What is going on?"
                                              "\n 4. I think that is all I need to know.")
        elif choice1A == "3":
            print(
                (str(docHoward)) + ": There was a virus that started to make people act odd. I have been researching.")
            lineSkip()
            time.sleep(2)
            print(str(
                docHoward) + ": You need to be careful of these people, they may not be able to see well, but their hearing makes up for it.")
            lineSkip()
            time.sleep(3)
            print((str(docHoward)) + ": Something else I don't know if any other states, or even cities were affected.")
            lineSkip()
            time.sleep(3)
            choice1D = input(str(docHoward) + ": Anything else you want to know?"
                                              "\n 1. What do these people do that are so dangerous?"
                                              "\n 2. Is there any way to kill these people?")
            while choice1D == "1" or "2":
                if choice1D == "1":
                    print(str(
                        docHoward) + ": Well the infected people are very violent. They ermm. They Like to eat other .... people.")
                    time.sleep(2)
                    lineSkip()
                    print(str(
                        docHoward) + ": It is like something from a scary movie. Who knew something like this could happen.")
                    choice1D = input(str(docHoward) + ": Anything else you want to know?"
                                                      "\n 1. What do these people do that are so dangerous?"
                                                      "\n 2. Is there any way to kill these people?")
                elif choice1D == "2":
                    print(str(
                        docHoward) + ": From what we know a good hit to the head will take them down. This is the best way to do so.")
                    lineSkip()
                    time.sleep(2)
                    choice1A = input(str(docHoward) + ": I should probably fill you in on some info ehh? Where should I begin?"
                                         "\n 1. Where am I?"
                                         "\n 2. Who are you?"
                                         "\n 3. What is going on?"
                                         "\n 4. That is all I think I need to know.")
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


story1A()
