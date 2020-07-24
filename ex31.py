print("""You enter a dark room with 2 door.
Do you go through the door #1 or #2?""")

door = input(">")

if door=="1":
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake")
    print("2.Scream at bear")

    bear = input(">")

    if bear=="1":
        print("The bear eats your face off. good job!")
    elif bear=="2":
        print("The bear eats your legs off.good job!")
    else:
        print(f"well doing {bear} is probably better.")
        print("bear runs away")

elif door==2:
    print("You stare into the endless abyss at cthulu's retina.")
    print("1.blueberries")
    print("2. yellow jackets clothespins")
    print("3.understading revolves yelling melofies")

    insanity = input(">")

    if insanity == '1' or insanity =='2':
        print("your body survives powered by a mind of jello.")
        print("Good job")
    else:
        print("he insanity rots your eyes into a pool")
        print("good job")

else:
    print("you stumb around fall on knife and die.")
