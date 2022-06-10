print("You enter a dark room with three doors.  Do you go through door #1, door #2, or door #3")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.  What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print("Well, doing {} is probably better.  Bear runs away.".format(bear))

elif door == "2":
    print("You stare into the endless abyss at Cthuhlu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.  Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.  Good job!")

elif door=="3":
  print("Water floods in through the door")
  print("1. Swim out of the door")
  print("2. Try to open another door")
  answer = input("> ")
  if answer == "1":
      print("You swim to the surface there is nothing but ocean for miles but you survive, good job!")
  if answer == "2":
      print("The other doors are locked, you drown.")

else:
    print("You stumble around and fall on a knife and die.  Good job!")