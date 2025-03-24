from random import randint

import prompt

from cli import welcome


def is_even(num):
    return num % 2 == 0


def main():
    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 10)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
