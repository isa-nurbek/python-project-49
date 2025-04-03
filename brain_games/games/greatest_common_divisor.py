import math
from random import randint

GAME_RULES = "Find the greatest common divisor of given numbers."


def produce_question_and_answer():
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    
    question = f"{first_number} {second_number}"
    correct_answer = math.gcd(first_number, second_number)

    return question, str(correct_answer)
