import json
import random
import datetime


def get_score_list():
    with open("score_list.json", "r") as score_list_file:
        score_list = json.loads(score_list_file.read())
        # print("Top scores:" + str(score_list))
    return score_list


def get_top_scores(score_list):
    return sorted(score_list, key=lambda k: k['attempts'])[:3]


def print_score_list(score_list):
    for score_dict in score_list:
        print("player_name " + score_dict["player_name"] +
              ", secret_number " + str(score_dict["secret_number"]) +
              ", " + str(score_dict["attempts"]) + " attempts" +
              ", date: " + score_dict["date"] +
              ", wrong_guesses " + str(score_dict["wrong_guesses"])
              )


def play_game(score_list):
    attempts = 0
    secret = random.randint(1, 30)
    wrong_guesses = []

    player_name = str(input("Enter your name: "))

    while True:
        guess = int(input("Guess the secret number between 1 and 30: "))
        attempts = attempts + 1

        if guess == secret:
            score_list.append({"player_name": player_name, "secret_number": secret, "attempts": attempts,
                               "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})

            with open("score_list.json", "w") as score_list_file:
                score_list_file.write(json.dumps(score_list))

            print("You have guessed it - congratulations! Its number:" + str(secret))
            print("Attempts needed:" + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct. Try something smaller")
        elif guess < secret:
            print("Your guess is not correct. Try something bigger")

        wrong_guesses.append(guess)
