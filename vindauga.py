# Introduction to Programming
# Authors: Harrison Zheng and Will Dye and Brendan Pacheco
# Date: 10/27/2019
# Project 2: This is a text based adventure game.


def main():
    title_intro()
    # Sets player to the starting location with a score of 0
    main_game("MEADOW", 0)


def title_intro():
    # Displays name of game
    print("                                                 Vindauga                                                \n")
    input("Press ENTER to continue. \n")
    # Lines 18-22 tell the back story of the game
    print("""    Today looked like it was going to be just like any other day. After listening to teachers lecture about 
    things you do not care the least about for seven and a half hours at school, you finally make it to the safe 
    haven of your room. You start up your computer and insert the game that you just got for your birthday. Suddenly, 
    a blinding white light comes beaming out of your monitor. When you wake up, you find yourself lying in a meadow. 
    You see a worn path that leads to a few huts not too far off in the distance and decide to follow it. \n""")
    return


def main_game(location, score):
    while True:
        print("Your current location is", location)
        print("Your current score is", score)
        cmd = input("Enter a command (enter HELP to see a list of valid commands): ")
        # The program will still run if the user enters a correct command with lowercase letters
        cmd = cmd.upper()
        if location == "MEADOW":
            if cmd == "WALK TO HUTS":
                playerName = input("Enter your name: ")
                print('\n')
                # Lines 38-65 describe the player's progress in the village
                print("""Upon arriving at the village, you see a sign with symbols from a foreign language. A tall, 
                middle-aged man walks by and you decide to ask him some questions. 'Well hello there! You must be new 
                here. What is your name?' You tell him to call you""", playerName,
                      "and ask him where you are. 'It is a pleasure to meet you", playerName + """'. The name of the 
                village is Vindauga. We have a lot to offer here, but we are not nearly as impressive as we used to 
                be,' he says with a sigh. You ask him what happened, thinking that it may give you some clues as to 
                why you are there. 'About three months ago, on a warm and sunny day, a man wearing a black cloak that 
                partially covered a long scar on his face came to Vindauga,' the villager began. 'He asked to see our 
                eldest leader, Mother Agatha, claiming that he had an urgent message to deliver. The Council called 
                for a meeting and there, the stranger told of how the citizens of his village had lost all sense of 
                meaning and only someone as wise as Mother Agatha could show them the light. But she sensed that this 
                man could not be trusted and ordered the guards to escort him out of Vindauga. As the guards marched 
                over to the stranger, he suddenly opened his arms, unleashing a strong gust of wind and revealing a 
                pair of large raven-like wings. Before anyone could regain their balance, he snatched Mother Agatha 
                and flew away. Since then, the Council has been arguing over who should take her place and very 
                little has been done to improve the lives of Vindaugans. As a result, many families, craftsmen, 
                and merchants have left to settle elsewhere. Traders hardly ever come to Vindauga anymore either.' 
                You ask the man where the stranger might have taken Mother Agatha, to which he responds, 'It’s likely 
                that he brought her back to his village, which we suspect sits beyond those mountains.' He points to 
                a mountain range about ten miles out. 'We have sent many soldiers to go look for our beloved Mother 
                Agatha, but none have returned.' With only a hint of nervousness in your voice, you tell the man that 
                you will find Mother Agatha and restore order. You add that it may be the only way to get back to 
                your world. Seeing your determination, the man says 'Very well then. But before you embark on this 
                quest, you will need some supplies.' He runs to a nearby hut and returns a moment later with a sword, 
                a shield, and a couple of canteens filled with water. 'My father gave me this sword and this shield 
                so that I could defend myself and all the things that I love. However, I am sure you will be doing 
                just that in the days to come so please accept this as a humble gift.' Taking the slightly worn, 
                yet sturdy weapons in your hands, you thank him and set a course for the mountains. \n""")
                location_score("MEADOW", True, 5)
            elif cmd == "HELP":
                print('\n')
                print(
                    """Valid commands are:\n WALK TO HUTS\n ASCEND MOUNTAINS\n REST IN CAVE\n REST IN TENT\n ENTER BARNHOUSE\n QUIT\n""")
                continue
            elif cmd == "QUIT":
                print('\n')
                # Displays the copyright statement and the player's score at the time they quit
                print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
                (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!

                                                                                                 Final Score:""", score)
                return
            else:
                print("Please enter the command 'WALK TO HUTS' in order to follow the storyline. \n")
                continue
        elif location == "VILLAGE":
            if cmd == "ASCEND MOUNTAINS":
                print('\n')
                # Lines 86-106 describe player's progress in the mountains
                print("""You reach the foot of the mountains a few hours later as the sun begins to set. Only then do 
                you realize how tall the mountains are. As you start climbing, you get the feeling that you are being 
                watched. A dark figure suddenly brushes past you. You unsheathe the sword that the villager gave you 
                just in time to slash the beast as it lunges at you with its long claws and full set of razor-like 
                teeth. You figure that you should find a place to camp out for the night as there will likely be more 
                beasts hunting. You spot a cave not too far up and quickly climb towards it. Inside, you find a man 
                not much older than yourself sitting by a fire. When he notices you, he quickly reaches for his spear 
                and points it at you. 'Who are you and what do you want?' he says in a menacing tone.""")
                input("My name is (Enter your name) ")
                print("""You tell him that you are on a mission to save Mother Agatha of Vindauga from the stranger 
                who abducted her. 'Oh, so am I,' he says, lowering his spear. You walk over and sit down across from 
                him, the flames of the fire waving in between. 'My name’s Svend. About a week ago, the Council sent 
                me and four others to find Mother Agatha. I was already reluctant because if all the people who went 
                before me could not find her, nevermind make it back to the village, how was I supposed to? As we 
                began walking, I started to think about all the things that I wouldn’t be able to do if I died on 
                this mission; make pottery for the village and travelers, build my own house, find a girl whom I 
                love, and start my own family. Eventually, I decided to tell the other villagers I was traveling with 
                that I needed some time to myself and that they should go on without me.' You tell Svend why you are 
                going on this mission and try to convince him that the whole village is counting on him. He 
                eventually gives in, saying 'If I’m not going to do it myself, then I suppose I could at least 
                protect the person who will.' \n""")
                location_score("VILLAGE", True, 5)
            elif cmd == "HELP":
                print('\n')
                print(
                    """Valid commands are:\n WALK TO HUTS\n ASCEND MOUNTAINS\n REST IN CAVE\n REST IN TENT\n ENTER BARNHOUSE\n QUIT\n""")
                continue
            elif cmd == "QUIT":
                print('\n')
                print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
                (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!

                                                                                                 Final Score:""", score)
                return
            else:
                print("Please enter the command 'ASCEND MOUNTAINS' in order to follow the storyline. \n")
                continue
        elif location == "MOUNTAINS":
            if cmd == "REST IN CAVE":
                print('\n')
                # Lines 126-141 describe player's progress in the forest
                print("""That night, you and Svend take turns sleeping and guarding the cave. The next morning, 
                you two reach the summit of the mountain. From there, you see a vast expanse of trees stretching out 
                into the distance. 'It looks like we still have a long way to go,' says Svend. The descent turns out 
                to be much easier than the ascent. By the time you and Svend enter the forest, however, the sun is 
                beginning to set again. The two of you split up to search for sticks that can be used to make a 
                shelter and a fire. You collect several branches and twigs from the tall trees surrounding you, 
                but stop when you hear a rustle in the leaves above. You grab your sword and your shield as the 
                rustles accompanied by faint chortles grow more and more frequent. Finally, something jumps out of 
                the trees and you swing your sword at it almost too late. It looked like a monkey, but with long 
                fangs, and it was much larger than any monkey you had seen before. Many more of them jump out at you 
                and you slash and block as quick as you can, only barely holding them off. One of them goes straight 
                for your head with its arms outstretched and you think that this is it, you are going to die in this 
                game. At this moment, a spear flies over your head and hits the creature right in the chest. You turn 
                around to see Svend running towards you. 'You were gone for so long, I knew you must have been in 
                trouble. Looks like I didn’t come a second too early.' You and Svend eventually find a safe spot to 
                build a makeshift tent and wait out the night. \n""")
                location_score("MOUNTAINS", True, 5)
            elif cmd == "HELP":
                print('\n')
                print(
                    """Valid commands are:\n WALK TO HUTS\n ASCEND MOUNTAINS\n REST IN CAVE\n REST IN TENT\n ENTER BARNHOUSE\n QUIT\n""")
                continue
            elif cmd == "QUIT":
                print('\n')
                print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
                (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!

                                                                                                 Final Score:""", score)
                return
            else:
                print("Please enter the command 'REST IN CAVE' in order to follow the storyline. \n")
                continue
        elif location == "FOREST":
            if cmd == "REST IN TENT":
                print('\n')
                # Lines 161-169 describe the player's progress at the settlement
                print("""The two of you spend the next morning trying to find a way out of the forest. You constantly 
                scan the trees, making sure that there are no monsters trying to kill you or Svend. Soon, 
                you guys come across some footprints. You suspect that there are other humans nearby and suggest that 
                you guys head in the direction the tracks are pointed. The two of you walk for another two miles and 
                see that there is indeed a settlement with inhabitants. In the center of it sits the largest 
                structure; an old barnhouse with a strange, dark aura around it. You thought to yourself that this 
                must be where the stranger is hiding Mother Agatha. You and Svend slowly approach the structure. A 
                pair of guards wearing bird-like masks and holding long spears stand in front of the entrance. You 
                and Svend sneak up behind them and knock each of them out with a swift blow to the head. \n""")
                location_score("FOREST", True, 5)
            elif cmd == "HELP":
                print('\n')
                print(
                    """Valid commands are:\n WALK TO HUTS\n ASCEND MOUNTAINS\n REST IN CAVE\n REST IN TENT\n ENTER BARNHOUSE\n QUIT\n""")
                continue
            elif cmd == "QUIT":
                print('\n')
                print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
                (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!

                                                                                                 Final Score:""", score)
                return
            else:
                print("Please enter the command 'REST IN TENT' in order to follow the storyline. \n")
                continue
        elif location == "SETTLEMENT":
            if cmd == "ENTER BARNHOUSE":
                print('\n')
                # Lines 189-220 describe the player's progress in the final stage of the game
                print("""Inside the structure, there is a prison cell holding an old, yet majestic, woman wearing a 
                black gown. She must be Mother Agatha, you thought. You and Svend hurry over to let her know that she 
                was saved. But rather than being delighted, she asks in a worried tone, 'You precious younglings, 
                what are your names?'. 'My name is Svend, your Highness,' Svend replied, trying to hide his 
                anxiousness.""")
                playerName = input("Your Highness, please call me (Enter your name) ")
                print("'Head back to Vindauga immediately, Svend and", playerName + """'. If Nero sees you, he will 
                kill both of you without hesitation.' Before you could ask who Nero is, a man in a pitch-black cloak 
                walks through the door. A long scar running across his face is partially covered by the hood of his 
                cloak, just like how the villager had described it to you. 'It’s too late now Agatha, these two kids 
                are already dead to me,' he says in a scratchy voice. Nero opens his big wings and blasts into the 
                air before diving down at you and Svend. You raise your shield to block the strike, but the sheer 
                force of the impact knocks you to the ground. Svend tries to stab at him with his spear, but Nero’s 
                reactions are too quick for him and he yanks the spear out of Svend’s hands and snaps it in half. You 
                and Svend begin inching backward, hoping to buy some time to come up with a last-minute plan. 'I must 
                say I am impressed. The only other time someone did not die on my first blow, they gave me this.' He 
                points to the scar on his face. 'Once I’m done with you rascals, I will have enough souls to extract 
                the source of Agatha’s powers. With it, I, Nero the Soulreaper, will take over this world and spare 
                none who disobey me.' You hang your head in defeat but notice then that your shield is glowing. You 
                look over to Mother Agatha and she gives you a look of encouragement. Suddenly, you knew what you had 
                to do. Nero raises his arm and concentrates his dark energy into his hand. 'Say goodbye fools!' As he 
                sends a beam your way, you leap up and charge at him, holding the glowing shield in front of your 
                body and your sword behind it. The shield has no problem dispersing the beam and once you are in 
                reach, you thrust your sword into Nero’s chest. 'What? How could I have failed?' he utters as he 
                collapses to the ground and disintegrates into thousands of feathers. You and Svend break the lock on 
                Mother Agatha’s cell door. 'That was amazing! You two just saved the world!' says Mother Agatha as 
                she steps out of her cell. You thank her and ask if she might know anything about getting back to 
                your world. 'Ah yes, I know just the spell.' You are filled with joy, but then you realize it means 
                leaving this world behind as well as Svend. 'Don’t worry about me. Just make sure you come back often 
                to visit. I’ll need you to back me up when I tell my friends about his wild journey.' Svend says with 
                tears at the corners of his eyes. The two of you embrace as Mother Agatha chants a long line of 
                phrases. A blinding white beam of light comes down from the sky and lifts you away. \n""")
                ending_copyright()
                # Exits out of the loop and game
                raise SystemExit
            elif cmd == "HELP":
                print('\n')
                print(
                    """Valid commands are:\n WALK TO HUTS\n ASCEND MOUNTAINS\n REST IN CAVE\n REST IN TENT\n ENTER BARNHOUSE\n QUIT\n""")
                continue
            elif cmd == "QUIT":
                print('\n')
                print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
                (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!

                                                                                                 Final Score:""", score)
                return
            else:
                print("Please enter the command 'ENTER BARNHOUSE' in order to follow the storyline. \n")
                continue
        else:
            print("Not a valid location.")


def location_score(location, firstVisit, score):
    # This function handles changing the player's location and score
    # Player only gains 5 points the first time they visit a location in the game
    if location == "MEADOW" and firstVisit:
        newLocation = "VILLAGE"
        newScore = score + 0
        main_game(newLocation, newScore)
    elif location == "VILLAGE" and firstVisit:
        newLocation = "MOUNTAINS"
        newScore = score + 5
        main_game(newLocation, newScore)
    elif location == "MOUNTAINS" and firstVisit:
        newLocation = "FOREST"
        newScore = score + 10
        main_game(newLocation, newScore)
    elif location == "FOREST" and firstVisit:
        newLocation = "SETTLEMENT"
        newScore = score + 15
        main_game(newLocation, newScore)
    else:
        print("You have already been to this location. \n")
    return


def ending_copyright():
    print('\n')
    # Lines 269-274 make up the epilogue
    print("""   When you wake up, you are sitting in your chair in front of your computer. It is now dark outside, 
    but according to the clock, you have only been gone for a few hours. Your monitor is showing the start screen of 
    Vindauga but you know that you have gone on enough adventures for one day. You eject the disc and put the game 
    away for another day. \n""")
    print("""                                                 The End                                                     
                                                                                                     Final Score: 30""")
    print('\n' * 2)
    print("""'Vindauga' was developed by Harrison Zheng (Harrison.Zheng1@marist.edu) and Will Dye 
    (George.Dye1@marist.edu) and Brendan Pacheco (Brendan.Pacheco1@marist.edu). Thank you for playing!""")
    return


main()
