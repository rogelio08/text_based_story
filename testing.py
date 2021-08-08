import sys
import time
#I changed this

a = 2
b = 0.2  # slower time between characters getting spaced out
c = 0.08  # quicker time between characters getting printed

def intro():
    print("\n")
    time.sleep(a)
    string_1 = '"Very well, remember to answer truthfully... Or don\'t, either way you\'ll provide valuable data"\n'
    for character in string_1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print("With that the voice leaves you and the lights turn off for a moment\nWhen they turn on again you find a table has appeared")
    time.sleep(a)
    print("On the table you see a key on end of the table and a hammer on the other\nThe voice chimes in again")
    s = '"Please choose the item that has most value to you..."\n'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    first_path = input("which item do you pick? (key = 1 / hammer = 2): ")
    if first_path == '1':
        print()
        path1()
    elif first_path == '2':
        print()
        path2()
    else:
        print("Unknown path detected")

def path1():
    time.sleep(a)
    print("\nDespite how strange and unnerving the situation is, you decided that perhaps the key might be important for something down the line.")
    time.sleep(a)
    print("You rationalize that there has to be some kind of logic as to why you're here and what's the meaning behind all this.")
    time.sleep(a)
    print("After picking up the key the lights turn off and the voice speaks up.")

    s = '"Interesting choice, you have no idea where you are or if that key even fits anywhere yet you still chose it?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()

    s2 = '"Let us find out whether your choice will be the key to freedom or the key to your death."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()

    print("When the lights turn on again the table is gone, but now the room includes two doors.\n")
    time.sleep(a)
    print("The first door appears to have seen better days, mots of its color has faded while several cracks could be seen in the wood.")
    time.sleep(a)
    print("The second door leaves you stunned, you recognize the door as the same one on the front of your home!")
    door_choice = input("\nWhich door do you use the key on? (1/2): ")
    if door_choice == "1":
        print()
        path1_1()
    elif door_choice == '2':
        print()
        path1_2()

def path1_1():
    print("\nWhile the familiar door is calling out to you, you realize that such an obvious choice must be a trap. So going against all your instincts for survival you hesitantely unlock the worn down door and head inside.")
    time.sleep(a)
    print("After exiting the concrete prison you find yourself somewhere damp, dark, and cold. Using your hands to feel around you deduce that you must be in some sort of cave.")
    time.sleep(a)
    print("Realizing that the door is no longer behind you and left with no other options you decide to feel your way to what is hopefully an exit.")
    time.sleep(a)
    print("After wandering around in the dark you notice small beams of light that eventually lead to an opening in the cave, and before you know you're outside in a forest.")
    time.sleep(a)
    print("Out in the distance you notice smoke from a what could be a campfire but at the same time you have no idea if you've actually escaped or not.")
    time.sleep(a)
    print("Armed with the determination to survive, you venture towards the smoke.")

def path1_2():
    print("\nNot wanting to spend another moment in the room you rush over to the familiar door and check to see if they key works.")
    time.sleep(a)
    print("By some miracle the key fits and you're able to open the door\nRushing through the door you find yourself in your own living room, and breathing a sigh of relief.")
    time.sleep(a)
    print("Things however, are not as they seem. You begin to notice that your home is eerily quiet, with no traces of your family anywhere.")
    time.sleep(a)
    print("As you search through your home your fears and only confirmed, none of your family members are anywhere!\nDesperate for answers you go back through the front door but are shocked by the result.")
    time.sleep(a)
    print("Instead of making it back to the isolated room your find yourself in your neighborhood, only there's no neighbors in sight. Moreover the normally busy interstate freeway you live next to is unusually quiet.")
    time.sleep(a)
    print("While trying to process what's happening you realize that if the door was in fact the one to your home how did they key you picked up unlock it if you've never seen a key like it?")
    time.sleep(a)
    print("Trying to remain optimistic, you figure there has to be someone around. And so you you go off in search of survivors that don't exist, forever wandering the hollow shell of the world you once knew.")

def path2():
    time.sleep(a)
    print("\nGiven the situation you're in, you can't rule out the possibility that this is all some kind of twisted game. Thus you reason that it's in your best interest to have some kind of weapon.")
    time.sleep(a)
    print("Besides, who knows if the key is meant to throw you off from choosing a multi-purpose tool? Not to mention you could theoretically open any lock using the hammer if you're smart about it.")
    time.sleep(a)
    print("Feeling satisfied you pick up the hammer, soon after the lights turn off and the voice could be heard again.\n")

    s = '"What an interesting choice, while it\'s clever to be cautious in your position choosing what could be considered a weapon does seem rather barbaric. Though that\'s nothing new to humans."'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()

    s2 = '"You made a bold choice, let\'s find out whether you have the dexterity to justify such an option."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()

    print("Soon the lights turn on and you notice the table and key is gone but you're not interested in that. What has your attention now is the 500 pound apex preadator that occupies the room with.")
    time.sleep(a)
    print("With a low growl, the spontaneous bear is sizng you up. It's at this moment when your adrenaline kicks in and you're given a few breif seconds to form a plan of attack.")
    time.sleep(a)
    print("You narrow down to your options to two choices: 1) Use your adrenaline to take on the bear in a battle to the death or 2) Throw the hammer towards the one lightbulb in the room and use the darkness to hide and wait it out.")
    bear_choice = input("\nHow do you go about dealing with the bear? (1/2): ")
    if bear_choice == '1':
        print()
        path2_1()
    else:
        print()
        path2_2()

def path2_1():
    print("\nDespite feeling panicked and afraid for your life you decide to muster up all the courage you have and challenge the bear for the right to live.")
    time.sleep(a)
    print("With a war cry you rush the bear ad the bear responds with a roar of its own and stands on two feet in order to strike you down.")
    time.sleep(a)
    print("Seeing this you fling yourself to the right in order to dodge the potentially fatal blow and as the bear crashes its paws down and turns to face you, you get in a lucky swing and manage to strike the bear near it's eye.")
    time.sleep(a)
    print("With a roar of pain the bear backs off. You can't believe it, you just might be able to pull this off! Is what you were thinking before you realized that you didn't completely dodge the first attack.")
    time.sleep(a)
    print("Looking down you realize you see an unsightly slash on the left side of your abdomen and while attempting to stop the bleeding the last of your adrenaline fades as the bear recovers.")
    time.sleep(a)
    print("Your last thoughts as you see the bear closing in for the finishing move were about how people who don't consider bears as apex predators have never fought one.")


def path2_2():
    print("\nUnderstanding the fact that under the laws of nature no human could ever beat a grown bear with just a hammer in an enclosed space you decide to use your higher level intelligence to your advantage.")
    time.sleep(a)
    print("As the bear prepares to attack your quickly throw your hammer at the dim lightbulb hanging from the ceiling, shattering it and engulfing the room in darkness.")
    time.sleep(a)
    print("At first your gamble seems to pay off as the bear's roars turn from aggressive to confused at the lack of vision.\nAs you hide in the corner of the now dark room a terrifying thought hits you.")
    time.sleep(a)
    print("Not only are you in a small room but bears don't exactly have to rely on sight alone. Sure enough, the bear begins to compose itself and soon begins sniffing the air.")
    time.sleep(a)
    print("You could only cower in horror and wait for your inevitable death as you curse your own lack of foresight")

print()
print()
print("     #######################")
print("     #                     #")
print("     #     Title Card      #")
print("     #                     #")
print("     #######################")
print()
print()
time.sleep(a)
print("You find yourself in a dim, concrete room with only a single lightbulb hanging from the ceiling")
time.sleep(a)
print("Before you are able to asses your surroundings a monotone voice could be heard")
time.sleep(a)
print()
start_game = input("Would you like to start the game? (Y/N): ")
if start_game == 'n' or start_game == 'N':
    print("Understood, subject #[REDACTED] does not wish to participate in the experiment. Bringing in the next subject...")
elif start_game == 'y' or start_game == 'Y':
    intro()
else:
    print("Answer does not compute, try again")