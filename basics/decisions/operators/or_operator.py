#using or operator
print("what type of adventure should i have")
user = input().lower()

#introducing the if statement
if (user == "scary") or (user == "short"):
  print("Entering the dark forest")
elif (user == "safe") or (user == "long"):
  print("Taking the safe route!")
else:
  print("not sure which route to take")  