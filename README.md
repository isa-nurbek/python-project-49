### Hexlet Tests and Linter Status:
[![Actions Status](https://github.com/isa-nurbek/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/isa-nurbek/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0236135eb91986f6964b/maintainability)](https://codeclimate.com/github/isa-nurbek/python-project-49/maintainability)

# Brain Games

**Brain Games** is a collection of five console games inspired by popular mobile apps designed to train your brain. Each game presents a series of questions that must be answered correctly. If you provide three correct answers, you win the game. However, a single incorrect answer ends the game and gives you the option to try again.

## Games Included:

1. **Calculator** – Solve arithmetic expressions.
2. **Progression** – Find the missing number in a numerical sequence.
3. **Even Number** – Determine whether a number is even.
4. **Greatest Common Divisor (GCD)** – Find the greatest common divisor of two numbers.
5. **Prime Number** – Determine if a number is prime.

Test your logic and math skills with **Brain Games**!

---

# Game: "Calculator"  

## Description  
The goal of the **Calculator** game is to solve simple mathematical expressions. The player is presented with a randomly generated arithmetic expression, such as `35 + 16`, and must provide the correct answer.  

## Gameplay  
When the game starts, the user is greeted and asked for their name. Then, the game begins presenting mathematical expressions to solve. The player must input the correct result. If the answer is correct, the game continues with another question.  

Example game session:  

```bash
$ make brain-calc

Welcome to the Brain Games!  
May I have your name? Sam  
Hello, Sam!  
What is the result of the expression?  
Question: 4 + 10  
Your answer: 14  
Correct!  
Question: 25 - 11  
Your answer: 14  
Correct!  
Question: 25 * 7  
Your answer: 175  
Correct!  
Congratulations, Sam!  
```

## Rules  
- The game includes three arithmetic operations: `+` (addition), `-` (subtraction), and `*` (multiplication).  
- Both numbers and operations are selected randomly.  
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.  

Example of an incorrect answer:  

```bash
Question: 25 * 7  
Your answer: 145  
'145' is wrong answer ;(. Correct answer was '175'.  
Let's try again, Sam!  
```

## Installation & Running
To play the game, install the required dependencies and run the following command:
```
$ make brain-calc
```

## Demo
[![Demo for Calculator game](https://asciinema.org/a/bdOugBFgGm4HASXZWZfrsNX5K.svg)](https://asciinema.org/a/bdOugBFgGm4HASXZWZfrsNX5K)  
Click the link above to watch the demo in Asciinema!

Enjoy solving math problems with the Calculator game!

---

# Game: "Brain Even"

## Description
The goal of the **Brain Even** game is to test the player's ability to determine whether a number is even or odd.

## Rules
1. The player is presented with a random number.
2. They must answer **"yes"** if the number is even, or **"no"** if the number is odd.
3. If the player answers correctly, they proceed to the next question.
4. If the player answers incorrectly, the game ends with a failure message.
5. To win, the player must correctly answer **three consecutive** questions.
6. Any input that does not match **"yes"** or **"no"** exactly (e.g., "y" instead of "yes") will be treated as incorrect.

## Example Gameplay
```
$ make brain-even

Welcome to the Brain Games!
May I have your name? Bill
Hello, Bill!
Answer "yes" if the number is even, otherwise answer "no".

Question: 15
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!
```

```
$ make brain-even

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".

Question: 15
Your answer: no
Correct!

Question: 6
Your answer: yes
Correct!

Question: 7
Your answer: no
Correct!

Congratulations, Sam!
```

## Installation & Running
To play the game, install the required dependencies and run the following command:
```
$ make brain-even
```

## Demo
[![Demo for Brain Even game](https://asciinema.org/a/XCJQY1Wyx8v6xOvDd5efrwUiD.svg)](https://asciinema.org/a/XCJQY1Wyx8v6xOvDd5efrwUiD)  
Click the link above to watch the demo in Asciinema!

Enjoy the game and test your number skills!
