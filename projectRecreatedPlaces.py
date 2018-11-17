import time
from projectRecreatedFunctions import lineSkip

docHoward = "Unknown Doctor"
sheriffBanks = "Unknown Sheriff"

vanbanTownsPeopleList = [docHoward, sheriffBanks,]

def docHowardHouse():
    print("You get up and look around.")
    docHowardHouse = input("You can walk into:"
        "\n 1. The Bedroom"
        "\n 2. The Kitchen"
        "\n 3. Outside")
    while docHowardHouse == "1" or "2" or "3":
        if docHowardHouse == "1":
            print("You walk into his bed room and see nothing interesting in here.")
            time.sleep(2)
            lineSkip()
            docHowardHouse = input("You can walk into:"
                                   "\n 1. The Bedroom"
                                   "\n 2. The Kitchen"
                                   "\n 3. Outside")
        elif docHowardHouse == "2":
            print("You walk into the kitchen and see nothing interesting really here just a normal kitchen.")
            time.sleep(2)
            lineSkip()
            print("Maybe you should try outside.")
            time.sleep(1)
            lineSkip()
            docHowardHouse = input("You can walk into:"
                                   "\n 1. The Bedroom"
                                   "\n 2. The Kitchen"
                                   "\n 3. Outside")

        elif docHowardHouse == "3":
            print("You walk outside and see a bright light. You close your eyes and let the adjust to the brightness.")
            lineSkip()
            time.sleep(2)
            break



def outsideVanBan():
    print("You see a small town and a sign that says 'Vanban'")
    time.sleep(2)
    lineSkip()
    placeChoiceOutsideVanBan = input("You can go to several places."
                                     "\n 1. Gunshop"
                                     "\n 2. Market Place"
                                     "\n 3. " + sheriffBanks
                                     "\n 4. " + )


docHowardHouse()

outsideVanBan()