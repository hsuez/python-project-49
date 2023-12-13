#!/usr/bin/env python3

import prompt
import brain_games.scripts.brain_games
import brain_games.scripts.cli_backup
from random import randint

def main():
    brain_games.scripts.brain_games.main()
    print('What number is missing in the progression?')
    n = 1
    flag = True
    while n < 4:
        step, a1, an = randint(1, 5), randint(1, 20), randint(1, 8)
        arr = [a1 + step * i for i in range(1, 10)]
        print('Question: ', end="")
        for i in arr:
            if i == arr[an]:
                print('...', end=" ")
            elif i == arr[-1]:
                print(i)
            else:
                print(i, end=" ")
        answer = prompt.integer('Your answer: ')
        if answer == arr[an]:
            print('Correct!')
            n += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{arr[an]}\'.')
            print(f'Let\'s try again, {brain_games.scripts.cli_backup.name}!')
            flag = False
            break
    if flag == True:
        print(f'Congratulations, {brain_games.scripts.cli_backup.name}!')

if __name__ == "__main__":
    main()
