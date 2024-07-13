
import random
from art import logo

print(logo)
print('Welcome to the number guessing game!')

 
def pick_number():
  print("I'm thinking of a number between 1 and 100.")
  return random.randint(1, 100)

number = pick_number()

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  remaining_attempts = 10
  print(f"You have {remaining_attempts} attempts remaining to guess the number.")
elif difficulty == 'hard':
  remaining_attempts = 5
  print(f"You have {remaining_attempts} attempts remaining to guess the number.")

guess = int(input("Make a guess: "))
while guess != number and remaining_attempts > 1:
  if guess > number:
    print("Too high.Try again.")
    remaining_attempts -= 1
    print(f"You have {remaining_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
  elif guess < number:
    print("Too low.Try again.")
    remaining_attempts -= 1
    print(f"You have {remaining_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

if remaining_attempts == 1:
  print("You didn't guess the number :(")
  print(f"It was {number}")
if guess == number:
  print("Yay you guessed the number!!!!")
