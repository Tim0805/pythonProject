tries = 3
while tries != 1:
  y += 1
  tries -= 1
  guess = int(input(f"Try again! You have a total of {tries} tries left! "))
else:
  print(f"You lost! The number was {x}! (q to quit, any key to play again) ")
