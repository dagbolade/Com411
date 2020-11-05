print("How many lives cables must i avoid?")
user = int(input())

lives = 0
while lives < user :
  #end = "" is used to join the print strings on different lines
  print("Avoiding...", end="")
  lives = lives + 1
  print("Done! {} live cables avoided!". format(lives))

print("\nAll live cables have been avoided."
)  