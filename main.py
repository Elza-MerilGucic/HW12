from functions import *


score_list = get_score_list()

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection == "A":
        play_game(score_list)
    elif selection == "B":
        score_list = get_top_scores(score_list)
        print_score_list(score_list)
    else:
        break
