# Dipesh-Kumawat-Guess-Gaming
Step 1: Project Planning
The purpose of this project is to build a Python program that generates a random number between 1 and 100, asks the user to guess the number, and provides feedback on whether their guess was too high or too low. The program should keep track of the number of guesses it takes the user to find the correct answer and display it at the end of the game.
Features:
•	Generate a random number between 1 and 100
•	Receive user input for the guess
•	Provide feedback on whether the guess was too high or too low
•	Keep track of the number of guesses it takes the user to find the correct answer
•	Allow the user to quit the game at any time
Program flow and interface:
•	The program starts by generating a random number between 1 and 100.
•	The user is prompted to enter their guess.
•	The program compares the user's guess to the randomly generated number and provides feedback on whether the guess was too high or too low.
•	If the user's guess is correct, the program displays the number of guesses it took to find the correct answer.
•	If the user wants to quit the game, they can do so at any time.
Step 2: Code & Comments
2.1. Import necessary libraries
We need to import the random library to generate a random number.
import random
2.2. Generate a random number
We need to generate a random number between 1 and 100. We can do this using the randint() function from the random library.
# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
	
2.3. Ask the user for their guess
We need to ask the user for their guess using the input() function and store it in a variable.
# Ask the user to guess the number
guess = input("Guess the number between 1 and 100: ")

2.4. Compare the user's guess to the random number and provide feedback
We need to compare the user's guess to the random number and provide feedback on whether the guess was too high or too low. We can do this using an if statement.
# Compare the user's guess to the random number and provide feedback
if int(guess) == random_number:
    print("Congratulations! You guessed the number.")
elif int(guess) < random_number:
    print("Your guess was too low. Try again.")
else:
    print("Your guess was too high. Try again.")

2.5. Keep track of the number of guesses
We need to keep track of the number of guesses it takes the user to find the correct answer. We can do this using a counter variable and increment it every time the user makes a guess.
# Keep track of the number of guesses
num_guesses = 1

# Loop until the user guesses the correct number
while int(guess) != random_number:
    # Ask the user to guess the number again
    guess = input("Guess again: ")
    
    # Compare the user's guess to the random number and provide feedback
    if int(guess) == random_number:



Conclusion
This project was created as a final Project of K.I Seminar for University of Duisburg Essen , which provides a fun and engaging way to learn and practice Python programming concepts. By following the steps outlined in this project, you can create a simple game that demonstrates how to generate random numbers, receive user input, and provide feedback to the user.









