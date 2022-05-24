import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(items, option):
    print_pause("You awaken in a field of flowers, with cold looking "
                "mountains to your right and a cozy cabin to your left.\n")
    print_pause("You suddenly remember your quest! You need to "
                "retrieve " + option + "'s tooth for a witch that "
                "lives near by.\n")
    print_pause("In your hand is nothing but a strange tingling sensation, "
                "a strange thrum beneath the skin. Maybe you should ask the "
                "witch about that...\n")


def cabin(items, option):
    print_pause("You approach the cabin of the witch and knock on the door.\n")
    if "tooth" in items:
        print_pause("The witch opens the door to the cabin, her face set in "
                    "a scowl, which suddenly brightens up when you show her "
                    "what you have. \n")
        print_pause("\"Ah! The tooth of a " + option + "!\" \n")
        print_pause("\"Just what I need to finish my spell! Thank you my "
                    "dear! Here's your reward.\" \n")
        print_pause("The witch smiles as she hands you two pennies...\n")
        print_pause("Maybe this adventuring life isn't what it's cracked up"
                    " to be...\n")
        play_again()
    else:
        print_pause("\"Well? Did you get it? What do you mean your hand is"
                    " tingling you-!\" \n "
                    "\"Oh just give me your hand!-\" \n")
        print_pause("\"Oh! Hmm, well my dear it just seems like you need a"
                    "little magic...\" \n")
        print_pause("Her hand runs over yours as she giggles and there's a "
                    "faint glow there now. Like a weapon primed for use...\n")
        items.append("magic")
    print_pause("You head back the way you came.")
    adventure(items, option)


def mountains(items, option):
    print_pause("The trek up the mountains is an arduous one. But you are "
                "stubborn.\n")
    print_pause("Cresting over one last cliff you see the creature you're"
                " looking for, a " + option + "! And it sees you!\n")
    print_pause("The " + option + " attacks!\n")
    if "magic" not in items:
        print_pause("With nothing but your bare hands you are woefully "
                    "unprepared!\n")
    while True:
        branch2 = input("You only have so many options: run or fight?!\n")
        if branch2 == "fight":
            if "magic" in items:
                print_pause("As the " + option + " charges toward you, you"
                            " look down at your hand knowing "
                            "what you need to do.\n")
                print_pause("You thrust your hand out unleashing the magic "
                            "given to you on the " + option + "!\n")
                print_pause("A crack of thunder and force echos through the "
                            "mountains and sends the creature tumbling end "
                            "over end before slamming against the rock wall "
                            "behind it!\n")
                print_pause("With the creature nullified for now, you set to"
                            " work gathering what the witch had requested.\n")
                print_pause("...")
                print_pause("You drop the tooth into your pouch and hurry to"
                            " leave before the " + option + " wakes up.\n")
                items.append("tooth")
                adventure(items, option)
            else:
                print_pause("You do your best but your bare hands could do"
                            " nothing against the " + option + ".\n")
                print_pause("You are torn limb from limb...\n")
            play_again()
            break
        if branch2 == "run":
            print_pause("You run back as fast as you can, feeling " + option +
                        "'s attack a hair's breath from "
                        "hitting your back!\n")
            print_pause("Luckily, it doesn't appear that you've been "
                        "followed.\n")
        adventure(items, option)
        break


def adventure(items, option):
    print_pause("You find yourself back in the fields.\n")
    while True:
        branch1 = input("Where would you like to go?\n")
        if branch1 == "cabin".lower():
            cabin(items, option)
            break
        if branch1 == "mountains".lower():
            mountains(items, option)
            break


def play_again():
    again = input("Would you like to try one more time? (y/n) \n").lower()
    if again == "y":
        print_pause("Taking you back to the beginning...\n")
        play_game()
    elif again == "n":
        print_pause("See you another time adventurer!\n")
        quit()
    else:
        play_again()


def play_game():
    items = []
    option = random.choice(["dragon", "troll", "goblin", "rust monster",
                            "Manager Bob",
                            "horrifying creature with many mouths",
                            "evil twin"])
    intro(items, option)
    adventure(items, option)


play_game()
