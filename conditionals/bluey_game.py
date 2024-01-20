bluey_family = ["Bluey", "Bingo", "Chilli", "Bandit"]

character = input("What's the name of a Bluey family member? ")

if character in bluey_family:
    print(f"Yes! {character} is a Bluey family member!")
else:
  print("Game over! That's not a Bluey family mamber!")
