#code to help beep look for his spare battery
print("\nI am looking for my battery?")
print("\nWhere should i look?")
user =  input().lower()

#using the if statement
if user == "in the bedroom":
  print("\nwhere in the bedroom should i look?")
  #creating another variable for input on where to look
  user_bedroom = input().lower()
  if user_bedroom == "under the bed":
    print("\nFound some shoes but no battery")
  else:
    print("\nFound some mess but no battery.")

#creating another if statement on where to look if not found in the bedroom
elif user =="in the bathroom":
  print("\nwhere in the bathroom should i look?")
  #creating a seperate variable
  user_bathroom = input().lower()
  if user_bathroom == "in the bathtub":
    print("\nFound a rubber duck but no battery")
  else:
    print("\nFound a wet surface but no battery.")

elif user == "in the lab":    
  print("\nWhere in the lab should I look?")
  user_lab = input()
  if user_lab ==  "on the table":
    print("\n\nYes! I found my battery!")
  else:
    print("Found some tools but no battery.")  
#creating a else statement    
else:
  print("\nI do not know where that is but I will keep looking.")    
