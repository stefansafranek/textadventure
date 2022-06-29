# Initialize the player

print("You awaken from a long slumber and see a hooded figure sitting next to a campfire.")
pname = input("The figure turns to you and asks you: 'Ah, so you finally woke up! Tell me: What is your name? ")

location = "campfire"

print("So you are " + pname + ". Huh... I once knew someone with your name. Good memories come to mind.")

north = "a small village"
south = "a cave of wolves"
west = "a well"
east = "a dog"

direction = input("So let me give you a lay of the land, " + pname + ". To the north is " + north + ". To the south is " + south + ". I wouldn't go there if I were you. To the west is  " + west + ". and to the east is " + east + ". Where do you want to go?")

if direction == "north":
    location = "village"
    print("You are in a small village. There is nobody here. Maybe they all left for a nice round of Bingo?")
elif direction == "south":
    location = "cave of wolves"
    print("The figure was right. There are a lot of wolves and they seem to be hungry. RIP.")
elif direction == "west":
    print("You see a well. There seems to be a hand coming out of it. You grab it. Bad Idea. RIP.")
elif direction == "west":
    print("You see a cure doggo.")
    choice = input("Do you pet him?")
    if choice == "yes":
        print("Congratulations! You won the game!!")
    elif choice == "no":
        print("You monster. The dog now saddened decides to go into the woods and be sad there. You lose. Horribly.")
else: 
    print("Come again?")
