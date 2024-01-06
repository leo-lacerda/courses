cynefin = ["Clear", "Complicated", "Complex", "Chaotic"]
  
cynefin_context = input("What's the Cynefin context? ")

if cynefin_context in cynefin:
  print("This is a Cynefin context.")
else:
  print("This is not a Cynefin context.")
