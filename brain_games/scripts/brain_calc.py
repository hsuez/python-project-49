#!/usr/bin/env python3
from random import randint
import brain_games.scripts.brain_games
import prompt
import sys
import brain_games.scripts.cli_backup

def calculation():
    brain_games.scripts.brain_games.main()
    print("What is the result of the expression?")
    n = 0
    flag = True
    operation = ["+", "-", "*"]
    while n < 3:
        oper = operation[randint(1, 100) % 3]
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        print(f"Question: {number1} {oper} {number2}")
        answer = prompt.string("Your answer: ")
        if oper == "+":
            correct_answer = number1 + number2
        elif oper == "-":
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2
        n += 1
        if answer != str(correct_answer):
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'.')
            flag = False
            break
    if flag:
        print(f'Congratulations, {brain_games.scripts.cli_backup.name}!')
    else:
        print('Let\'s try again!')


if __name__ == "__main__":
    calculation()
