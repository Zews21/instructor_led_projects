# print the logo
from art import logo
from art import vs
import random
from game_data import data
from replit import clear
# compare function
def compare(follower_countA, follower_countB):
  if follower_countA > follower_countB:
    return "A"
  elif follower_countA < follower_countB:
    return "B"
# print(logo)
score = 0
running= True
clear()
print(logo)
# while running:

person_A = random.choice(data)


person_B = random.choice(data)
while running:
  # randomly pick a person as A
  nameA = person_A["name"]
  follower_countA = person_A["follower_count"]
  descriptionA = person_A["description"]
  countryA = person_A["country"]

  while person_A == person_B:
    person_B = random.choice(data)

  
  print(f"Compare A: {nameA}, a {descriptionA}, from {countryA} ")
  # print the VS
  print(vs)
  # randomly pick a person as B
  nameB = person_B["name"]
  follower_countB = person_B["follower_count"]
  descriptionB = person_B["description"]
  countryB = person_B["country"]
  print(f"Against B: {nameB}, a {descriptionB}, from {countryB} ")
  # take input from the user
  answer = input("Who has more followers? Type 'A' or 'B': ")
    
  # compare the 2 persons
  
  if compare(follower_countA, follower_countB) == answer:
    score += 1
    clear()
    print(logo)
    print(f"You are right! Current score {score}")
    if answer == "A":
      # person_A = person_A
      person_B = random.choice(data)
    elif answer == "B":
      person_A = person_B
      person_B = random.choice(data)
  elif compare(follower_countA, follower_countB) != answer:
    print(logo)
    clear()
    print(f"Sorry, that's wrong. Final score {score}")
    running = False
      
