goal = int(input("What's your goal (number)? "))
checkin = int(input("What's the actual number? "))

if goal == checkin:
  print("You made it!")
elif goal < checkin:
  print("You nailed it!")
else:
  print("You can do it next time!")
