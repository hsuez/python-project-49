#!/usr/bin/env python3
import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
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
Correct answer was {correct_answer}.\nLet's try again, {name}!")
            main_flag = False
            break
        print("Correct!")
        n += 1
    if main_flag:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
