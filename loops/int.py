while True:
  try:
    x = int(input("What's x value? "))
    break
  except ValueError:
    print("x is not an integer. Try again:")
    
print(f"{x} is a integer!")
