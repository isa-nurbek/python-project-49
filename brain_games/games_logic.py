import prompt

from brain_games.cli import welcome

ROUNDS_COUNT = 3


def run(game):
    name = welcome()
    print(game.GAME_RULES)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.produce_question_and_answer()

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
            break
    else:
        print(f"Congratulations, {name}!")
