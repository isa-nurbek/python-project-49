import prompt

from brain_games.cli import welcome

ROUNDS_COUNT = 3


def init_game(game_module):
    name = welcome()
    print(game_module.GAME_RULES)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.produce_question_and_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return
    else:
        print(f"Congratulations, {name}!")
