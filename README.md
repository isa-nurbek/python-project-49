[![Actions Status](https://github.com/isa-nurbek/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/isa-nurbek/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0236135eb91986f6964b/maintainability)](https://codeclimate.com/github/isa-nurbek/python-project-49/maintainability)

# Brain Games

**Brain Games** is a collection of five console games inspired by popular mobile apps designed to train your brain. Each game presents a series of questions that must be answered correctly. If you provide three correct answers, you win the game. However, a single incorrect answer ends the game and gives you the option to try again.

## Games Included

1. **Calculator** – Solve arithmetic expressions.
2. **Progression** – Find the missing number in a numerical sequence.
3. **Even Number** – Determine whether a number is even.
4. **Greatest Common Divisor (GCD)** – Find the greatest common divisor of two numbers.
5. **Prime Number** – Determine if a number is prime.

Test your logic and math skills with **Brain Games**!

---

## Game: "Calculator"  

### Description  

The goal of the **Calculator** game is to solve simple mathematical expressions. The player is presented with a randomly generated arithmetic expression, such as `35 + 16`, and must provide the correct answer.  

### Rules  

- The game includes three arithmetic operations: `+` (addition), `-` (subtraction), and `*` (multiplication).  
- Both numbers and operations are selected randomly.  
- To win, the player must correctly answer **three consecutive** questions.
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.  

### Gameplay  

When the game starts, the user is greeted and asked for their name. Then, the game begins presenting mathematical expressions to solve. The player must input the correct result. If the answer is correct, the game continues with another question.  

### Example Gameplay  

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

Example of an **incorrect answer**:  

```bash
Question: 25 * 7  
Your answer: 145  
'145' is wrong answer ;(. Correct answer was '175'.  
Let's try again, Sam!  
```

### Installation & Running

To play the game, install the required dependencies and run the following command:

```plaintext
make brain-calc
```

### Demo

[![Demo for Calculator game](https://asciinema.org/a/bdOugBFgGm4HASXZWZfrsNX5K.svg)](https://asciinema.org/a/bdOugBFgGm4HASXZWZfrsNX5K)  
Click the link above to watch the demo in Asciinema!

Enjoy solving math problems with the Calculator game!

---

## Game: "Arithmetic Progression"

### Description

The goal of the **Progression** game is to identify the missing number in an arithmetic progression.

### Rules

- The player is shown a sequence of numbers forming an arithmetic progression.
- One number in the sequence is replaced by two dots (`..`).
- The player must guess the missing number.
- The length of the progression is randomly determined but is always at least 5 numbers (recommended length is 10).
- The position of the missing element changes randomly each round.
- To win, the player must correctly answer **three consecutive** questions.
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.

### Example Gameplay

```plaintext
$ make brain-progression

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?

Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!

Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!

Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!

Congratulations, Sam!
```

Example of an **incorrect answer**:

```plaintext
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 1
'1' is wrong answer ;(. Correct answer was '15'.
Let's try again, Sam!
```

### Installation & Running

To play the game, install the required dependencies and run the following command:

```plaintext
make brain-progression
```

### Demo

[![Demo for Progression game](https://asciinema.org/a/o8vENv6ZlStkCNEJBtHMXsXhO.svg)](https://asciinema.org/a/o8vENv6ZlStkCNEJBtHMXsXhO)  
Click the link above to watch the demo in Asciinema!

Have fun solving progressions and sharpening your logic!

---

## Game: "Brain Even"

### Description

The goal of the **Brain Even** game is to test the player's ability to determine whether a number is even or odd.

### Rules

- The player is presented with a random number.
- They must answer **"yes"** if the number is even, or **"no"** if the number is odd.
- If the player answers correctly, they proceed to the next question.
- To win, the player must correctly answer **three consecutive** questions.
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.
- Any input that does not match **"yes"** or **"no"** exactly (e.g., "y" instead of "yes") will be treated as incorrect.

### Example Gameplay

```plaintext
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

Example of an **incorrect answer**:

```plaintext
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

### Installation & Running

To play the game, install the required dependencies and run the following command:

```plaintext
make brain-even
```

### Demo

[![Demo for Brain Even game](https://asciinema.org/a/XCJQY1Wyx8v6xOvDd5efrwUiD.svg)](https://asciinema.org/a/XCJQY1Wyx8v6xOvDd5efrwUiD)  
Click the link above to watch the demo in Asciinema!

Enjoy the game and test your number skills!

---

## Game: "Greatest Common Divisor (GCD)"

### Description

The goal of the **GCD** game is to find the greatest common divisor (GCD) of two randomly generated numbers.

### Rules

- The player is presented with two random numbers.
- They must calculate and input the greatest common divisor of these numbers.
- If the player answers correctly, they proceed to the next question.
- To win, the player must correctly answer **three consecutive** questions.
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.

### Example Gameplay

```plaintext
$ make brain-gcd

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.

Question: 25 50
Your answer: 25
Correct!

Question: 100 52
Your answer: 4
Correct!

Question: 3 9
Your answer: 3
Correct!

Congratulations, Sam!
```

Example of an **incorrect answer**:

```plaintext
Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!
```

### Installation & Running

To play the game, install the required dependencies and run the following command:

```plaintext
make brain-gcd
```

### Demo

[![Demo for GCD game](https://asciinema.org/a/f7SbhMTIsVwGoyXlMgbJIYPdv.svg)](https://asciinema.org/a/f7SbhMTIsVwGoyXlMgbJIYPdv)  
Click the link above to watch the demo in Asciinema!

Enjoy the game and test your number skills!

---

## Game: "Prime Number"

### Description

The goal of the **Prime Number** game is to test whether the player can determine if a given number is prime.

### Rules

- The player is shown a single number.
- They must answer **"yes"** if the number is prime, or **"no"** if it is not.
- If the player answers correctly, they proceed to the next question.
- To win, the player must correctly answer **three consecutive** questions.
- If the player provides an incorrect answer, the correct result is displayed, and the game ends.

### Example Gameplay

```plaintext
$ make brain-prime

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".

Question: 7
Your answer: yes
Correct!

Question: 13
Your answer: yes
Correct!

Question: 3
Your answer: yes
Correct!

Congratulations, Sam!
```

Example of an **incorrect answer**:

```plaintext
Question: 9
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Sam!
```

### Installation & Running

To play the game, install the required dependencies and run the following command:

```plaintext
make brain-prime
```

### Demo

[![Demo for Prime Number game](https://asciinema.org/a/HMkRY3JXksfK1hLzXgGIunbym.svg)](https://asciinema.org/a/HMkRY3JXksfK1hLzXgGIunbym)  
Click the link above to watch the demo in Asciinema!

Enjoy the game and test your number skills!
