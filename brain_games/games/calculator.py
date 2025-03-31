from random import choice, randint

GAME_RULES = 'What is the result of the expression?'
math_symbols = ['+', '-', '*']


def produce_question_and_answer():
    math_operation = choice(math_symbols)

    first_num = randint(1, 10)
    second_num = randint(1, 10)

    question = f'{first_num} {math_operation} {second_num}'

    if math_operation == "+":
        correct_answer = first_num + second_num
    elif math_operation == "-":
        correct_answer = first_num - second_num
    elif math_operation == "*":
        correct_answer = first_num * second_num
    else:
        raise ValueError('Something went wrong!')

    return question, str(correct_answer)
