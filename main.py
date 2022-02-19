# Boolean if, elifs and else

#Beaufort Wind Scale

print("Welcome to the Beaufort Wind Scale Ready Reckoner")

wind_speed = int(input("Enter Wind Speed (mph): "))

b0 = ("Beaufort Scale 0 - Calm")
b1 = ("Beaufort Scale 1 - Light Air")
b2 = ("Beaufort Scale 2 - Light Breeze")
b3 = ("Beaufort Scale 3 - Gentle Breeze")
b4 = ("Beaufort Scale 4 - Moderate Breeze")
b5 = ("Beaufort Scale 5 - Fresh Breeze")
b6 = ("Beaufort Scale 6 - Strong Breeze ")
b7 = ("Beaufort Scale 7 - Near Gale ")
b8 = ("Beaufort Scale 8 - Gale")
b9 = ("Beaufort Scale 9 - Strong Gale")
b10 = ("Beaufort Scale 10 - Storm")
b11 = ("Beaufort Scale 11 -Violent Storm")
b12 = ("Beaufort Scale 12 -Hurricance")

if wind_speed <1:
  print(b0)
elif wind_speed <4:
  print(b1)
elif wind_speed <8:
  print(b2)
elif wind_speed <13:
  print(b3)
elif wind_speed <19:
  print(b4)
elif wind_speed <25:
  print(b5)
elif wind_speed <32:
  print(b6)
elif wind_speed <39:
  print(b7)
elif wind_speed <47:
  print(b8)
elif wind_speed <54:
  print(b9)
elif wind_speed <64:
  print(b10)
elif wind_speed <73:
  print(b11)
else:
  print(b12)


