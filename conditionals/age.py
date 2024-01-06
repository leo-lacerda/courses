yo = 40
how_old = int(input("How old are you? "))
age_difference = 0

if how_old > 40:
  age_difference += (how_old - yo)
  print(f"Hey, boomer! You're {age_difference} years older than me!")
elif how_old < 40:
  age_difference += (yo - how_old)
  print(f"You're {age_difference} years younger than me!")
else:
  print("Welcome to my life!")
