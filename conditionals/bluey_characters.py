blueys_family = ["Bluey", "Bingo", "Chilli", "Bandit"]
school_friends = ["Winton", "Snickers", "Coco", "Calypso", "The Terriers", "Missy", "Indy", "Jack", "Mrs Retriever", "Honey", "Mackenzie", "Chloe", "Lila"]
blueys_neighbours = ["Judo", "Wendy", "Lucky", "Lucky's Dad"]

character = input("What's the name of the character? ")

if character in blueys_family:
  print(f"{character} is a Bluey's family character!")
elif character in school_friends:
  print(f"{character} is a Bluey's school friend!")
elif character in blueys_neighbours:
  print(f"{character} is a Bluey's neighbour character!")
else:
  print(f"{character} is not a Bluey's character!")
