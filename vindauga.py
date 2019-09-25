# Introduction to Programming Project 1
# This is a text based adventure game
# Authors: Harrison Zheng and Jeremiah Furia
# Date: 9/24/2019

def main():
    print("Vindauga")       #Displays name of game
    input("Press Enter to continue")
    location = "Meadow"     #Sets player's location to meadow
    score = 0       #Player's score starts at 0
    print("Today looked like it was going to be just like any other day.")          #Lines 11 to 15 tell the back story of the game
    print("After listening to teachers lecture about things you do not care the least about for seven and a half hours at school, you finally make it to the safe haven of your room.")
    print("You start up your computer and insert the game that you just got for your birthday.")
    print("Suddenly, a blinding white light comes beaming out of your monitor. When you wake up, you find yourself lying in a meadow.")
    print("You see a worn path that leads to a few huts not too far off in the distance and decide to follow it.")
    input("Press Enter to continue")
    location = "Village"        #Sets player's location to village
    score = score + 5
    print("Upon arriving at the village, you see a sign with symbols from a foreign language.")         #Lines 19 to 41 describe the player's progress in the village
    print("A tall, middle-aged man walks by and you decide to ask him some questions.")
    print("'Well hello there! You must be new here.'")
    print("You nod politely and ask him where you are.")
    print("'The name of the village is Vindauga. We have a lot to offer, but we are not nearly as impressive as we used to be.'")
    print("he says with a sigh. You ask him what happened, thinking that it may give you some clues as to why you are there.")
    print(" 'About three months ago, on a warm and sunny day, a man wearing a black cloak that partially covered the long scar on his face came to Vindauga,'the villager began.")
    print("He asked to see our eldest leader, Mother Agatha, claiming that he had an urgent message to deliver.")
    print("The Council called for a meeting and there, the stranger told of how the citizens of his village had lost all sense of meaning and only someone as wise as Mother Agatha could show them the light.")
    print("But she sensed that this man could not be trusted and ordered the guards to escort him out of Vindauga.")
    print("As the guards marched over to the stranger, he suddenly opened his arms, unleashing a strong gust of wind and revealing a pair of large raven-like wings.")
    print("Before anyone could regain their balance, he snatched Mother Agatha and flew off. Since then, the Council has been arguing over who should take her place and very little has been done to improve the lives of Vindaugans.")
    print("As a result, many families, craftsmen, and merchants have left to settle elsewhere.")
    print("Traders hardly ever come to Vindauga anymore either.' ")
    print(" You ask the man where the stranger might have taken Mother Agatha, to which he responds.")
    print(" 'It’s likely that he brought her back to his village, which we suspect sits beyond those mountains.' ")
    print("He points to a mountain range about ten miles out.")
    print(" 'We have sent many soldiers to go look for our beloved Mother Agatha, but none have returned.' ")
    print("With only a hint of nervousness in your voice, you tell the man that you will find Mother Agatha and restore order. You add that it may be the only way to get back to your world.")
    print("Seeing your determination, the man says 'Very well then. But before you embark on this quest, you will need some supplies.' ")
    print("He runs to a nearby hut and returns a moment later with a sword, a shield, and a couple of canteens filled with water.")
    print(" 'My father gave me this sword and this shield so that I could defend myself and all the things that I love.")
    print("However, I am sure you will be doing just that in the days to come so please accept this as a humble gift.'Taking the slightly worn, yet sturdy, weapons in your hands, you thank him and set a course for the mountains.")
    input("press enter to continue")
    location = "Mountain"       #sets player's location to mountain
    score = score + 5
    print("You reach the foot of the mountains a few hours later. The sun is setting, but only then do you realize how tall the mountains are.")        #Lines 45 to 58 describe player's progress in the mountain
    print("As you begin the ascent, you get the feeling that you are being watched. A dark figure suddenly brushes past you.")
    print("You unsheath the sword that the villager gave you just in time to slash the beast as it lunges at you with its long claws and full set of razor-like teeth.")
    print("You figure that you should find a place to camp out for the night as there will likely be more beasts hunting. You spot a cave not too far up and quickly climb towards it.")
    print("Inside, you find a man not much older than yourself sitting by a fire. When he notices you, he quickly reaches for his spear and points it at you.")
    print(" 'Who are you and what do you want?' he says in a menacing tone.")
    print("You tell him that you are on a mission to save Mother Agatha of Vindauga from the stranger who took her away.")
    print(" 'Oh, I am too,' he says, lowering his spear. You walk over and sit down across from him, the flames of the fire waving in between.")
    print(" 'My name’s Svend. About a week ago, the Council sent me and four other people to find Mother Agatha.")
    print(" I was already reluctant because if all the people who went before me could not find her, nevermind make it back to the village, how was I supposed to.")
    print("As we began walking, I started to think about all the things that wouldn’t be able to do if I died on this mission; make pottery for the village and travelers, build my own house, find a girl whom I love, and start my own family.")
    print("Eventually, I decided to tell the other villagers I was traveling with that I needed some time to myself and that they should go on without me.' ")
    print("You tell Svend why you are going on this mission and try to convince him that the whole village is counting on him.")
    print("He eventually gives in, saying 'If I’m not going to do it myself, then I suppose I could at least protect the one who will.' ")
    input("press enter to continue")
    location = "forest"     #sets player's location to the forest
    score = score + 5
    print("The next morning, you and Svend reach the summit of the mountain. From there, you see a vast expanse of trees stretching out into the distance.")        #Lines 62 to 71 describe player's progress in the forest
    print(" 'It looks like we still have a long way to go,' says Svend. The descent turns out to be much easier than the ascent.")
    print(" 'By the time you and Svend enter the forest, however, the sun is beginning to set again. The two of you split up to search for sticks that can be used to make a shelter and a fire.")
    print("You collect several branches and twigs from the tall trees surrounding you, but stop when you hear a rustle in the leaves above.")
    print("You grab your sword and your shield as the rustles accompanied by faint chortles grow more and more frequent. Finally, something jumps out of the trees and you swing your sword at it almost too late.")
    print("It looked like a monkey, but with long fangs, and it was much larger than any monkey you had seen before.")
    print("Many more of them jump out at you and you slash and block as quick as you can, only barely holding them off.")
    print("One of them goes straight for your head with its arms outstretched and you think that this is it, you are going to die in this game.")
    print("At this moment, a spear flies over your head and hits the creature right in the chest. You turn around to see Svend running towards you.")
    print(" 'You were gone for so long, I knew you must have been in trouble. Looks like I didn’t come a second too early.' You and Svend eventually find a safe spot to build a makeshift tent and wait out the night.")
    input("press enter to continue")
    location = "settlemet"      #sets player's location to settlement
    score = score + 5



main()





