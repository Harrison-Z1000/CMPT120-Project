# Introduction to Programming
# Authors: Harrison Zheng, Will Dye, and Brendan Pacheco
# Date: 12/13/2019
# Final Project: This is a text based adventure game.


from player import Player
from locale import Location


def main():
    title()
    name = input("Enter your name: ")
    player_object = Player(name, 0, "MEADOW", 0, [])
    main_game(player_object)


def title():
    # Displays name of the game
    print("                           Vindauga                          \n")
    input("Press ENTER to continue. \n")
    print("Make sure to reach the end of the game using 100 commands or less "
          "in order to win it!\n")
    return


def main_game(player_object):
    print("Your current location is", player_object.location)
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
            location_object = Location(location_list[0], True, False, [])
            if cmd == "BEGIN":
                print(Location.display_description1(location_object))
                print("When prompted, enter the command 'LOOK AROUND' to see "
                      "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[0],
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
                print("Please enter the command 'BEGIN' in order to "
                      "start the adventure!\n")
                continue
        elif player_object.location == location_list[1]:
            location_object = Location(location_list[1], True, False, [])
            if cmd == "WALK TO HUTS":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[1],
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
                print("Please enter the command 'WALK TO HUTS' in order to "
                      "follow the storyline. \n")
                continue
        elif player_object.location == location_list[2]:
            location_object = Location(location_list[2], True, False, [])
            if cmd == "ASCEND MOUNTAINS":
                print(Location.display_description1(location_object))
                print(
                    "When prompted, enter the command 'LOOK AROUND' to see "
                    "what happens next!\n")
                continue
            elif cmd == "LOOK AROUND":
                print(Location.display_description2(location_object,
                                                    player_object.name))
                newPlayerObject = Player.change_location(player_object,
                                                         location_list[2],
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
    # Only runs the next 2 lines if the player makes more than 50 moves
    print("Sorry, you are out of moves.")
    play_again()


def list_commands():
    # Lists all valid commands if the player enters HELP
    print("""\nValid commands are:\n BEGIN\n WALK TO HUTS\n ASCEND MOUNTAINS
 REST IN CAVE\n LEAVE TENT\n KEEP WALKING\n WALK ALONG CREEK\n ENTER BARNHOUSE
 LOOK AROUND\n MAP\n POINTS\n QUIT\n""")
    return


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
    return


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
