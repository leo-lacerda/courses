c_levels = ["CEO", "CTO", "CMO", "CHRO", "CIO", "CFO", "COO"]

c_level = input("Which c-level? ")

if c_level in c_levels:
  print("It's a common c-level!")
else:
  print("Are you sure this is a c-level? Looks like you're making that up!")
