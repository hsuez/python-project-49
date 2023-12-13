#!/usr/bin/env python3
from random import randint
import brain_games.scripts.brain_games
import brain_games.scripts.cli_backup
import prompt

def main():
    brain_games.scripts.brain_games.main()
    print("Find the greatest common divisor of given numbers.")
    n = 1
    flag = True
    while n <= 3:
        number1 ,number2 = randint(1, 100), randint(1, 100)
        if number2 == number1:
            while number2 == number1:
                number2 = randint(1, 100)
        print(f'Question: {number1} {number2}')
        answer = prompt.integer('Your answer: ')
        del1, del2 = [1], [1]
        while number1 > 1:
            for i in range(2, number1 + 1):
                if number1 % i == 0:
                    number1 //= i
                    del1.append(i)
                    break
        while number2 > 1:
            for i in range(2, number2 + 1):
                if number2 % i == 0:
                    number2 //= i
                    del2.append(i)
                    break
        correct_answer = 1
        for i in del1:
            for j in del2:
                if i == j:
                    correct_answer *= i
                    del2.remove(j)
                    break
        if answer == correct_answer:
            print('Correct!')
            n += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. correct answer was \'{correct_answer}\'.)\
                Let\'s try again, {brain_games.scripts.cli_backup.name}!')
            flag = False
            break
    if flag == True:
        print(f'Congratulations, {brain_games.scripts.cli_backup.name}!')

if __name__ == "__main__":
    main()
