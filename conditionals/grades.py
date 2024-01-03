av1 = float(input("AV1: "))
av2 = float(input("AV2: "))
av3 = float(input("AV3: "))

final_grade = (av1 + av2 + av3) / 3

if final_grade < 0 or final_grade > 10:
  print("You typed some number wrong. Try again, please!") 
elif final_grade < 5:
  print(f"Final grade: {final_grade:.1f} - You've failed!")
elif final_grade < 7:
  print(f"Final grade: {final_grade:.1f} - Not a nice grade, but you're approved.")
elif final_grade < 10:
  print(f"Final grade: {final_grade:.1f} - Congratulations! You're approved!")
else:
  print(f"Final grade: {final_grade:.1f} - Congratulations! You're approved with maximum grade!")
