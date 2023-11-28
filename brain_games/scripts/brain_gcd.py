#!/usr/bin/env python3
from random import randint
import brain_games.scripts.brain_games
import sys

sys.path.append("/Users/macbook/Desktop/projects/python-project-49/brain_games")

import cli

def main():
    brain_games.scripts.brain_games.main()
    print("Find the greatest common divisor of given numbers.")
    prime_number = [i for i in range(2, 121)]
    flag = True
    for i in range(len(prime_number) - 1):
        for j in range(i, len(prime_number)):
            if prime_number[j] % prime_number[i] == 0:
                prime_number.pop(j)
    print(prime_number)
