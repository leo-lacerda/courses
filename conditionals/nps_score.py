nps_score = int(input("What's the NPS score (0-100)? "))

if nps_score < 0 or nps_score > 100:
  print("NPS score should be a number from 0 to 100.")
  int(input("What's the NPS score (0-100)? "))
elif nps_score < 70:
  print("Detractor.")
elif nps_score >=90:
  print("Promoter.")
else:
  print("Passive.")
