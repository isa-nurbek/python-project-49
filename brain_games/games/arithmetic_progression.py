from random import randint

GAME_RULES = "What number is missing in the progression?"


def produce_question_and_answer():
    progression_length = 10
    start = randint(1, 10)
    step = randint(1, 10)
    progression = list(range(start, start + step * progression_length, step))

    hidden_position = randint(0, len(progression) - 1)
    correct_answer = progression[hidden_position]

    progression[hidden_position] = ".."
    question = " ".join(map(str, progression))

    return question, str(correct_answer)
