from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def produce_question_and_answer():
    number = randint(1, 10)
    question = f'{number}'

    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer
