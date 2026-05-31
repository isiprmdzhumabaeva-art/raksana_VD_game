import random
from math import gcd

from VD_games.engine import run_game

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    answer = gcd(num1, num2)

    question = f"{num1} {num2}"
    return question, answer


def main():
    run_game(generate_round, DESCRIPTION)


if __name__ == "__main__":
    main()
