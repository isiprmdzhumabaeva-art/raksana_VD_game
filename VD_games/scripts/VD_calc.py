import random

from VD_games.engine import run_game

DESCRIPTION = "What is the result of the expression?"


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f"{num1} {operator} {num2}"
    return question, answer


def main():
    run_game(generate_round, DESCRIPTION)


if __name__ == "__main__":
    main()
