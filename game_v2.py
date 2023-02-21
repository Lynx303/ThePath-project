#inside functions

#ask player to start game
def ask_game_start():

    valid_start = ("S","s","start","Start","START")
    start = input(">")

    if start in valid_start:
        pass
    else:
        print("\n")
        print("Please provide valid answer")
        ask_game_start()

#ask player to restart game
def ask_game_restart():

    valid_restart = ("r","R","restart","Restart","RESTART")
    valid_exit = ("e","E","exit","Exit","EXIT")
    restart_request = input(">")
    if restart_request in valid_restart:
        game()
    elif restart_request in valid_exit:
        print("Game ended. To start a new run, please execute original cell again.")
    else:
        print("\n")
        print("Please provide valid answer")
        ask_game_restart()


#STORY
#0
def choice_0(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_1.png'))
        path.append("1")
        encounters.append("Mugger crocodile (Crocodylus palustris)")
        choice_1(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_2.png'))
        path.append("2")
        encounters.append("Indian pangolin (Manis crassicaudata)")
        choice_2(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_0(path, encounters)

#1
def choice_1(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_3.png'))
        path.append("3")
        encounters.append("Bengal monitor (Varanus bengalensis)")
        choice_3(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_4.png'))
        path.append("4")
        encounters.append("Sloth bear (Melursus ursinus)")
        choice_4(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_1(path, encounters)

#3
def choice_3(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_7.png'))
        path.append("7")
        encounters.append("Indian star tortoise (Geochelone elegans)")
        choice_7(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_8.png'))
        path.append("8")
        encounters.append("Indian Peafowl (Pavo cristatus)")
        choice_8(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_3(path, encounters)

#7
def choice_7(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'end_1.png'))
        path.append("E1")
    elif answer == "2":
        display(Image.open(r'end_2.png'))
        path.append("E2")
    else:
        print("\n")
        print("Please provide valid answer")
        choice_7(path, encounters)

#8
def choice_8(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'end_1.png'))
        path.append("E1")
    elif answer == "2":
        display(Image.open(r'end_2.png'))
        path.append("E2")
    else:
        print("\n")
        print("Please provide valid answer")
        choice_8(path, encounters)

#4
def choice_4(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_8.png'))
        path.append("8")
        encounters.append("Indian Peafowl (Pavo cristatus)")
        choice_8(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_9.png'))
        path.append("9")
        encounters.append("King Cobra (Ophiophagus hannah)")
        choice_9(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_4(path, encounters)

#9
def choice_9(path, encounters):
    from IPython.display import display
    from PIL import Image
    import random

    answer = input(">")

    if answer == "1":
        display(Image.open(r'end_3.png'))
        path.append("E3")
    elif answer == "2":
        if random.random() < 0.9:
            display(Image.open(r'end_4.png'))
            path.append("E4")
        else:
            display(Image.open(r'end_5.png'))
            path.append("E5")
    else:
        print("\n")
        print("Please provide valid answer")
        choice_9(path, encounters)

#2
def choice_2(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_5.png'))
        path.append("5")
        encounters.append("Indian leopard (Panthera pardus fusca)")
        choice_5(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_6.png'))
        path.append("6")
        encounters.append("Four-horned antelope (Tetracerus quadricornis)")
        choice_6(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_2(path, encounters)

#5
def choice_5(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_9.png'))
        path.append("9")
        encounters.append("King cobra (Ophiophagus hannah)")
        choice_9(path, encounters)
    elif answer == "2":
        display(Image.open(r'story_10.png'))
        path.append("10")
        encounters.append("Indian python (Python molurus)")
        choice_10(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_5(path, encounters)

#10
def choice_10(path, encounters):
    from IPython.display import display
    from PIL import Image
    import random

    answer = input(">")

    if answer == "1":
        display(Image.open(r'end_6.png'))
        path.append("E6")
        encounters.append("Chital (Axis axis)")
    elif answer == "2":
        if random.random() < 0.5:
            display(Image.open(r'end_7.png'))
            path.append("E7")
        else:
            display(Image.open(r'end_8.png'))
            path.append("E8")
    else:
        print("\n")
        print("Please provide valid answer")
        choice_10(path, encounters)

#6
def choice_6(path, encounters):
    from IPython.display import display
    from PIL import Image
    import time

    answer = input(">")

    if answer == "1":
        display(Image.open(r'story_11.png'))
        path.append("11")
        encounters.append("Indian Elephant (Elephas maximus)")
        time.sleep(0.5)
        display(Image.open(r'end_9.png'))
        path.append("E9")
    elif answer == "2":
        display(Image.open(r'story_12.png'))
        path.append("12")
        encounters.append("Tiger (Panthera tigris)")
        choice_12(path, encounters)
    else:
        print("\n")
        print("Please provide valid answer")
        choice_6(path, encounters)

#12
def choice_12(path, encounters):
    from IPython.display import display
    from PIL import Image

    answer = input(">")

    if answer == "1":
        display(Image.open(r'end_10.png'))
        path.append("E10")
    elif answer == "2":
        display(Image.open(r'end_11.png'))
        path.append("E11")
    else:
        print("\n")
        print("Please provide valid answer")
        choice_12(path, encounters)

#GAME FRAMEWORK
def game():
    import time
    from IPython.display import display
    from PIL import Image

    #Home screen
    display(Image.open(r'story_title.png'))

    time.sleep(0.5)

    #call function to start game
    ask_game_start()

    #define lists for path code and animal encounters
    path = []
    encounters = []

    #Ask for name of the player
    print("\n Please enter your name: \n")
    player = input(">")
    #print(player)

    #Story start
    display(Image.open(r'story_intro.png'))

    time.sleep(0.5)

    #start with first story choice
    choice_0(path, encounters)

    time.sleep(10)
    #End screen
    display(Image.open(r'story_thanks.png'))

    time.sleep(5)

    #print game summary
    print("Thank you for playing " + player + "!")
    print('''
GAME SUMMARY:

Player:''')
    print(player + "\n")

    #print story path
    print("Your story path:")
    final_path = ""
    for step in path:
        final_path = final_path + step + " "
    print(final_path)

    #print animal encounters
    print("\n")
    print("You have encountered the following animals:")
    for encounter in encounters:
        print(encounter)
    print("\n")

    #show story outcome
    end_survive = ["E1", "E2", "E3", "E5", "E6", "E7", "E9", "E11"]

    if any(end in path for end in end_survive):
        print("You survived!\n")
    else:
        print("You died.\n")

    print("Type RESTART to try again or EXIT to end the game")
    time.sleep(0.5)

    ask_game_restart()
