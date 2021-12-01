import random


def introduction():
    print("In this program we will generate a bunch of random shit")

#14
subject = ["dog", "cat", "rat", "man", "vampire", "centaur", "ghoul", "snake", "crocodile", "jedi", "robot", "rabbit", "mongoose", "duckling", "moose", "flobberworm", "jellyfish"]
#17
adjective = ["rabid", "flesh-eating", "musty", "suicidal", "philosophical", "foolish", "jumpy", "power-hungry", "retarded", "deceitful", "elegant", "repulsive", "collosal", "genius"]
#17
weapon = ["lightsaber", "blaster", "gun", "pistol", "sniper-rifle", "stinky banana", "severed jawbone", "spear", "harpoon", "grenade-launcher", "bazooka", "sword", "old breadstick", "mouldy bagette", "half-eaten head of lettuce", "rubber chicken", "teddy bear"]
#12
colour = ["red", 'orange', 'blue', "lilac", "gold", "purple", "yellow", "silver", "black", "green", "dark green", "brown"]
#6
vehicle = ["car", "ice-cream truck", "pegasus", "spaceship", "pirate ship", "submarine", "WWII panzer", "hoverbike", "broomstick"]
#9
food = ["cheeseburgers", "noodles", "ice-cream", "human brains", "calf liver", "alien excretion", "pizza", "nachos", "grapefruits"]
#8
drink = ["water", "petroleum", "miso soup", "fanta", "coca-cola", "liquid gold", "blue milk", "laundry detergent", "dark soy sauce", "vinegar", "cheeto dust", "the blood of virgins", "pelican broth", "Hydrochloric acid", "300 year old wine", "rum"]
#9
family = ["uncle", "aunt", "grandfather", "grandmother", "older brother", "annoying sister", "great-great-great grandfather", "best friend", "worst enemy"]


def randomPicker():

    global randomSubject
    randomSubject = random.choice(subject)

    global randomAdjective
    randomAdjective = random.choice(adjective)

    global randomWeapon
    randomWeapon = random.choice(weapon)

    global randomColour
    randomColour = random.choice(colour)

    global randomVehicle
    randomVehicle = random.choice(vehicle)

    global randomSubjectTwo
    randomSubjectTwo = random.choice(subject)

    global randomAdjectiveTwo
    randomAdjectiveTwo = random.choice(adjective)

    global randomFood
    randomFood = random.choice(food)

    global randomDrink
    randomDrink = random.choice(drink)

    global randomFamily
    randomFamily = random.choice(family)



def randomSentence():

    prompt = random.randint(1,7)

    if prompt == 1:
        print("A story about a", randomAdjective, randomSubject, "wielding a", randomWeapon, "who fights against a", randomAdjectiveTwo, randomSubjectTwo)
    if prompt == 2:
        print("You ride a", randomVehicle, "leaking", randomDrink,  "with a", randomAdjective, randomSubject, "who likes to eat", randomFood)
    if prompt == 3:
        print("A", randomAdjective, randomSubject, "who plans to ban", randomFood,", is running for president against a", randomAdjectiveTwo, randomSubjectTwo)
    if prompt == 4:
        print("You have to duel to the death against a", randomAdjective, randomSubject, "using only a", randomWeapon)
    if prompt == 5:
        print("You are being forced to drink", randomDrink, "by a very", randomAdjective, randomSubject)
    if prompt == 6:
        print("You are on a diet where you can only eat", randomColour, randomFood, ", but you are being forced to lick a", randomWeapon, "by a", randomSubject)
    if prompt == 7:
        print("You are gifted a", randomColour, randomVehicle, "by your", randomAdjective, randomFamily)
    print("")


def repeater():
    repeat = input("Do you want to create another prompt? 'yes' or 'no': ")
    if repeat == 'yes':
        print("")
        main()
    elif repeat == 'no':
        quit()
    else:
        print("type yes or no")
        repeater()

def main():
    randomPicker()
    randomSentence()
    repeater()

main()