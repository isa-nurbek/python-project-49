from random import randint

GAME_RULES = "What number is missing in the progression?"


def produce_question_and_answer():
    progression = []

    progression_length = 10
    start = randint(1, 10)
    step = randint(1, 10)

    for _ in range(progression_length):
        progression.append(start)
        start += step

    hidden_position = randint(0, len(progression) - 1)
    correct_answer = progression[hidden_position]

    progression[hidden_position] = ".."
    progression = " ".join([str(item) for item in progression])
    question = f"{progression}"

    return question, str(correct_answer)
