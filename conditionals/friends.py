friends = ["Joey", "Chandler", "Ross", "Rachel", "Monica", "Phoebe"]

character_name = input("What's your favorite Friend's character? ")

if character_name in friends:
  print(f"I love {character_name}!")
else:
  print(f"{character_name} is not a Friends main character.")
