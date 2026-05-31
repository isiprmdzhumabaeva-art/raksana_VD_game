import random

import prompt


def main():
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        correct = "yes" if number % 2 == 0 else "no"

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
