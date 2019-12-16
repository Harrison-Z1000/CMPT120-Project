# Introduction to Programming
# Authors: Harrison Zheng, Will Dye, and Brendan Pacheco
# Date: 12/13/2019
# Final Project: This is a text based adventure game.


from player import Player
from locale import Location
from item import Item


def main():
    title()
    name = input("Enter your name: ")
    player_object = Player(name, 0, "MEADOW", 0, [])
    location_object = Location("MEADOW", True, False, [])
    main_game(player_object, location_object)


def title():
    # Displays name of the game
    print("                           Vindauga                          \n")
    input("Press ENTER to continue. \n")
    print("Make sure to reach the end of the game using 100 commands or less "
          "in order to win it!\n")
    return


def main_game(player_object, location_object):
    print("\nYour current location is", player_object.location)
    while Player.moves_count(player_object, player_object.moves) <= 100:
        # Contains every location in the game
        location_list = ["MEADOW", "VILLAGE", "MOUNTAINS", "FOREST", "BUSHES",
                         "CREEK", "SETTLEMENT", "BARNHOUSE"]
        cmd = input("Enter a command (enter 'HELP' to see a list of valid "
                    "commands): ")
        # The program will still run if the user enters a correct command
        # with lowercase letters
        cmd = cmd.upper()
        if player_object.location == location_list[0]:
            if cmd == "BEGIN":
                print(Location.display_description1(location_object))
                print("When prompted, enter the command 'LOOK AROUND' to see "
                      "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                print("Make sure to SEARCH this location and TAKE any items you find! When you are "
                      "ready to move on, enter the command 'NEXT LOCATION'.\n")
                continue
            elif cmd == "SEARCH":
                location_object.wasSearched = True
                print("\nThere are no items in this location.\n")
                continue
            elif cmd == "TAKE":
                if location_object.wasSearched:
                    print("\nThere are no items here to take!\n")
                    continue
                else:
                    print("\nYou must SEARCH the location before you can take "
                          "any items!\n")
                    continue
            elif cmd == "USE":
                print("\nThere are currently no items in your inventory!\n")
                continue
            elif cmd == "DROP":
                print("\nThere are currently no items in your inventory!\n")
                continue
            elif cmd == "INVENTORY":
                print("\nThere are currently no items in your inventory!\n")
                continue
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            elif cmd == "NEXT LOCATION":
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[0],
                                                         location_object.wasVisited,
                                                         player_object.score)
                location_object = Location(location_list[1], True, False, [Item.get_item(0), Item.get_item(1)])
                main_game(newPlayerObject, location_object)
            else:
                print("Please enter the command 'BEGIN' to "
                      "start the adventure!\n")
                continue
        elif player_object.location == location_list[1]:
            if cmd == "WALK TO HUTS":
                print(Location.display_description1(location_object))
                print("When prompted, enter the command 'LOOK AROUND' to see "
                      "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                print("Make sure to SEARCH this location and TAKE any items you find! When you are "
                      "ready to move on, enter the command 'NEXT LOCATION'.\n")
                continue
            elif cmd == "SEARCH":
                location_object.wasSearched = True
                print("\nAs you walk through Vindauga, two shiny items sitting "
                      "by a tree catch your eyes. One of them is a sword "
                      "and the other is a shield. They may come in handy "
                      "since you will be crossing dangerous terrains.\n")
                continue
            elif cmd == "TAKE":
                if location_object.wasSearched:
                    player_object.inventory, location_object.items = take_item(player_object.inventory, location_object.items)
                else:
                    print("\nYou must SEARCH the location before you can take "
                          "any items!\n")
                continue
            elif cmd == "USE":
                use_item(player_object)
                continue
            elif cmd == "DROP":
                drop_item(player_object.inventory)
                continue
            elif cmd == "INVENTORY":
                display_inventory(player_object.inventory)
                continue
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            elif cmd == "NEXT LOCATION":
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[1],
                                                         location_object.wasVisited,
                                                         player_object.score)
                location_object = Location(location_list[2], True, False, [])
                main_game(newPlayerObject, location_object)
            else:
                print("Please enter the command 'WALK TO HUTS' to see what "
                      "happens in this leg of the journey!\n")
                continue
        elif player_object.location == location_list[2]:
            if cmd == "ASCEND MOUNTAINS":
                print(Location.display_description1(location_object))
                print("When prompted, enter the command 'LOOK AROUND' to see "
                      "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                sword = Item.get_item(0)
                swordCount = player_object.inventory.count(sword)
                # If the player has a sword, they can win the game.
                # Otherwise, they automatically lose.
                if Sword > 0:
                    print(Location.display_description2(location_object,
                                                        player_object.name))
                    newPlayerObject = Player.change_location(player_object,
                                                             location_list[2],
                                                             location_object.wasVisited,
                                                             player_object.score)
                    main_game(newPlayerObject)
                else:
                    print("""\n    Only then do you realize how tall
    the mountains are. As you start climbing, you get the
    feeling that you are being watched. A dark figure suddenly
    brushes past you. A few moments later, you see a beast lunge at you
    with its long claws and full set of razor-like teeth, making you
    wish you had the sword the villager tried to give you earlier.
    Unable to defend yourself, you die on the side of the mountain.
                            GAME OVER\n""")
                    early_exit(player_object.score)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'ASCEND MOUNTAINS' in order "
                      "to follow the storyline. \n")
                continue
        elif player_object.location == location_list[3]:
            location_object = Location(location_list[3], True, False, [])
            if cmd == "REST IN CAVE":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[3],
                                                         location_object.wasVisited,
                                                         player_object.score)
                main_game(newPlayerObject)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'REST IN CAVE' in order to "
                      "follow the storyline. \n")
                continue
        elif player_object.location == location_list[4]:
            location_object = Location(location_list[4], True, False, [])
            if cmd == "LEAVE TENT":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[4],
                                                         location_object.wasVisited,
                                                         player_object.score)
                main_game(newPlayerObject)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'LEAVE TENT' in order to "
                      "follow the storyline. \n")
                continue
        elif player_object.location == location_list[5]:
            location_object = Location(location_list[5], True, False, [])
            if cmd == "KEEP WALKING":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[5],
                                                         location_object.wasVisited,
                                                         player_object.score)
                main_game(newPlayerObject)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'KEEP WALKING' in order to "
                      "follow the storyline. \n")
                continue
        elif player_object.location == location_list[6]:
            location_object = Location(location_list[6], True, False, [])
            if cmd == "WALK ALONG CREEK":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[6],
                                                         location_object.wasVisited,
                                                         player_object.score)
                main_game(newPlayerObject)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'WALK ALONG CREEK' in order "
                      "to follow the storyline. \n")
                continue
        elif player_object.location == location_list[7]:
            location_object = Location(location_list[7], True, False, [])
            if cmd == "ENTER BARNHOUSE":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                player_object = Player.change_location(player_object,
                                                       location_list[7],
                                                       location_object.wasVisited,
                                                       player_object.score)
                input("Press ENTER to continue.\n")
                ending()
                early_exit(player_object.score)
            elif cmd == "HELP":
                list_commands()
                continue
            elif cmd == "MAP":
                game_map()
                continue
            elif cmd == "POINTS":
                print("Your current score is", player_object.score, '\n')
                continue
            elif cmd == "QUIT":
                early_exit(player_object.score)
            else:
                print("Please enter the command 'ENTER BARNHOUSE' in order "
                      "to follow the storyline. \n")
                continue
        else:
            print("Not a valid location.")
    # Only runs the next 2 lines if the player makes more than 100 moves
    print("Sorry, you are out of moves.")
    play_again()


def take_item(player_inventory, location_items):
    # Removes an item from the location and adds it to the player's inventory
    # when they take an item
    itemToTake = input("\nEnter the name of the item you want to take: ")
    itemToTake = change_item_type(itemToTake)
    location_items.remove(itemToTake)
    player_inventory.append(itemToTake)
    print(itemToTake.name, "has been added to your inventory!\n")
    return player_inventory, location_items


def use_item(player_object):
    # Prints a statement and decreases an item's number of uses by one
    itemToUse = input("\nEnter the name of the item you want to use: ")
    itemToUse = change_item_type(itemToUse)
    itemCount = player_object.inventory.count(itemToUse)
    if itemCount > 0:
        if player_object.location == "VILLAGE":
            if itemToUse.name == "Sword":
                print("\nYou take some practice swings with the sword. It "
                      "is a little heavy but feels good in your hand.\n")
                itemToUse.uses -= 1
                return
            elif itemToUse.name == "Shield":
                print("\nYou practice defending yourself with the shield, "
                      "and cannot help but wonder about the emblem on "
                      "the front.\n")
                itemToUse.uses -= 1
                return
            else:
                print("That item is not in your inventory!")
                return
        # elif self.location == location_list[2]:
        #
        # elif self.location == location_list[3]:
        #
        # elif self.location == location_list[4]:
        #
        # elif self.location == location_list[5]:
        #
        # elif self.location == location_list[6]:
        #
        # elif self.location == location_list[7]:
        #
        else:
            return
    else:
        print("That item is not in your inventory!")


def drop_item(player_inventory):
    # Removes an item from the player's inventory
    itemToDrop = input("\nEnter the name of the item you want to drop: ")
    itemToDrop = change_item_type(itemToDrop)
    itemCount = player_inventory.count(itemToDrop)
    if itemCount > 0:
        player_inventory.remove(itemToDrop)
        print(itemToDrop.name, "has been removed from your inventory!\n")
        return player_inventory
    else:
        print("That item is not in your inventory!")


def change_item_type(requestedItem):
    # Converts an item from a string to the actual object
    if requestedItem.upper() == "SWORD":
        requestedItem = Item.get_item(0)
    elif requestedItem.upper() == "SHIELD":
        requestedItem = Item.get_item(1)
    elif requestedItem.upper() == "BERRIES":
        requestedItem = Item.get_item(2)
    elif requestedItem.upper() == "FLASK":
        requestedItem = Item.get_item(3)
    else:
        print("\nInvalid item name.\n")
        return
    return requestedItem


def display_inventory(player_inventory):
    # Displays every item in the player's inventory and its attributes
    if len(player_inventory) > 0:
        i = 0
        while i < len(player_inventory):
            print("Name:", player_inventory[i].name, "\tDescription:", player_inventory[i].description, "\tUses:", player_inventory[i].uses, "\n")
            i += 1
    else:
        print("\nThere are currently no items in your inventory!\n")


def list_commands():
    # Lists all valid commands if the player enters HELP
    print("""\nValid commands are:\n BEGIN\n WALK TO HUTS\n ASCEND MOUNTAINS
 REST IN CAVE\n LEAVE TENT\n KEEP WALKING\n WALK ALONG CREEK\n ENTER BARNHOUSE
 LOOK AROUND\n MAP\n POINTS\n QUIT\n""")


def game_map():
    # Displays a rough map of locations in the game
    print("""
                                         /////////////  |~|  /////  _________
                                    ^    |||||||||||||  |~|  ||||  /         \ 
                                     ^   /////////////  |~|  //// |   NERO'S  |
                                    ^    |||||||||||||  |~|  |||| | SETTLEMENT|
                                    ^    /////////////  |~|  ////  \_________/
                                   ^     |||||||||||||  |~|  ||||||||||||
                  ++++++++++++       ^   //////::::::/  |~|  ////////////
                  +          +      ^    ||||||BUSHES|  |~|  ||||||||||||
                  + VINDAUGA +      ^    //////::::::/  |~|  ////////////
                  +          +    ^      |||||||||||||  |~|  ||||||||||||
                  ++++++++++++     ^     /////////////  |~|  ////////////
                                     ^   |||||||||||||  |~|  ||||||||||||
     ==========                     ^    /////////////  |~|  ////////////
       MEADOW                            |||||||||||||  |~|  ||||||||||||
     ==========                          /////////////  |~|  ////////////
                                                                           """)


def early_exit(score):
    # If the player quits before finishing the game, this displays the
    # copyright statement and their score at the time they quit.
    print("""\n    'Vindauga' was developed by Harrison Zheng
    (Harrison.Zheng1@marist.edu) and Will Dye (George.Dye1@marist.edu) and
    Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!
                                                        Final Score:""", score)
    play_again()


def ending():
    # Displays the epilogue
    print("""    When you wake up, you are sitting in your chair in front of
    your computer. It is now dark outside, but according to the clock,
    you have only been gone for a few hours. Your monitor is showing the
    start screen of Vindauga, but you know that you have gone on enough
    adventures for one day. You eject the disc and put the game away for
    another day. \n""")
    print("""                           The End                           """)


def play_again():
    # Asks the player if they want to play again and restarts the game if
    # they respond "Yes".
    ans = str(input("Play Again? (Yes or No): "))
    if ans[0] == "Y" or "y":
        main()
    else:
        raise SystemExit("Goodbye!")


main()
