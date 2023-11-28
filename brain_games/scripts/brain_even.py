#!/usr/bin/env python3
import prompt
import random
import sys
import brain_games

sys.path.append("/Users/macbook/Desktop/projects/python-project-49/brain_games")

import cli


def main():
    brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    main_flag = True
    while n < 3 and main_flag:
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = 'no' if number % 2 == 1 else 'yes'
        if (answer != correct_answer):
            print(f"'{answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\nLet's try again, {cli.name}!")
            main_flag = False
            break
        print("Correct!")
        n += 1
    if main_flag:
        print(f"Congratulations, {cli.name}!")


if __name__ == "__main__":
    main()
