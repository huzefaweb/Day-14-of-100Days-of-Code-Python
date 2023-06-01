from game_data import data
import random
from art import logo
from art import vs
from replit import clear

compare_A = random.choice(data)
continuation = True
score = 0
print(logo)
while continuation:
  name = compare_A["name"]
  follower_count = compare_A["follower_count"]
  description = compare_A["description"]
  country = compare_A["country"]
  print(f"Compare A: {name}, {description}, {country}")

  print(vs)

  compare_B = random.choice(data)
  if compare_A == compare_B:
    compare_B = random.choice(data)
  name_b = compare_B["name"]
  follower_count_b = compare_B["follower_count"]
  description_b = compare_B["description"]
  country_b = compare_B["country"]
  print(f"Compare B: {name_b}, {description_b}, {country_b}")

  choice = input("Who has more followers? Type 'A' and 'B': ")
  if choice == "A":
    if follower_count > follower_count_b:
      score += 1
      clear()
      print(logo)
      print(f"You are right current score: {score}")
      compare_A = compare_B
    else:
      clear()
      print(f"Sorry That's wrong. Final score: {score}")
      continuation = False
  else:
    if follower_count < follower_count_b:
      score += 1
      clear()
      print(logo)
      print(f"You are right current score: {score}")
      compare_A = compare_B
    else:
      clear()
      print(f"Sorry That's wrong. Final score: {score}")
      continuation = False
