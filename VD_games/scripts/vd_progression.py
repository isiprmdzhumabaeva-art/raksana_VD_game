import random

from VD_games.engine import run_game

DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [str(start + i * step) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(progression)
    return question, answer


def main():
    run_game(generate_round, DESCRIPTION)


if __name__ == "__main__":
    main()
