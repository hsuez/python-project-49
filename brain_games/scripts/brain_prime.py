#!/usr/bin/env python3

import prompt
import brain_games.scripts.brain_games
import brain_games.scripts.cli_backup
from random import randint
from math import sqrt

def predicat(number):
    arr = []
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            arr.append(i)
    return 'yes' if len(arr) == 0 else 'no'

def main():
    brain_games.scripts.brain_games.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 1
    flag = True
    while n < 4:
        number = randint(1, 14)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = predicat(number)
        if answer == correct_answer:
            n += 1
            print('Correct')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {brain_games.scripts.cli_backup.name}!')
            flag = False
            break
    if flag == True:
        print(f'Congratulations, {brain_games.scripts.cli_backup.name}!')
        
        
if __name__ == '__main__':
    main()
