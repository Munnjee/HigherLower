import random
import os
from art import logo, vs
from game_data import data


def get_random():
    """Get random data from data set"""
    return random.choice(data)


def format_data(selected):
    """Format selected data into printable format: name, description and country"""
    name = selected["name"]
    description = selected["description"]
    country = selected["country"]
    return f"{name}, a(n) {description}, from {country}"


def check_response(guess, a_followers, b_followers):
    """Checks user's guess against follower stats and returns True if correct or False if incorrect"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    play = True
    score = 0
    int_a = get_random()

    while play:
        print(logo)
        int_b = get_random()
        if score > 0:
            print(f"You're right! Current score: {score}")

        print("Compare A: " + format_data(int_a))
        print(vs)
        print("Compare B: " + format_data(int_b))

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower = int_a["follower_count"]
        b_follower = int_b["follower_count"]
        is_correct = check_response(answer, a_follower, b_follower)

        if is_correct:
            score += 1
            int_a = int_b
        else:
            play = False

        os.system('clear')

    print(logo)
    print(f"Sorry, that's wrong. Final Score: {score}.")


play_game()