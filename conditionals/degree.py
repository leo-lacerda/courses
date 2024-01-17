bachelor_degree = 2000
master_degree = 3500
phd = 6000

your_degree = input("What's your degree (BD, MD or PhD)? ")

if your_degree == "BD":
  print(f"Your salary will be US${bachelor_degree}.")
elif your_degree == "MD":
  print(f"Your salary will be US${master_degree}.")
elif your_degree == "PhD":
  print(f"Your salary will be US${phd}.")
else:
  print("That's not a degree.")
