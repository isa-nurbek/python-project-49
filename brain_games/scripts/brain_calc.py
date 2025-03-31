from random import choice, randint

import prompt

from cli import welcome


def main():
    name = welcome()
    print('What is the result of the expression?')

    for _ in range(3):
        math_symbols = ['+', '-', '*']
        math_random_symbol = choice(math_symbols)
        
        first_num = randint(1, 10)
        second_num = randint(1, 10)

        print(f"Question: {first_num} {math_random_symbol} {second_num}")
        answer = prompt.string('Your answer: ')

        if math_random_symbol == '+':
            correct_answer = first_num + second_num
        elif math_random_symbol == '-':
            correct_answer = first_num - second_num
        elif math_random_symbol == '*':
            correct_answer = first_num * second_num
        else:
            raise ValueError('Something went wrong!')
            
        if answer == str(correct_answer):
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
