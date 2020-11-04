#user to enter typeof cover
print("What type of cover does the book have?")
cover = input().lower()

if cover == "soft":

  print("The book is soft, is it a perfect bound book")
  
  perfectbound = input()
  
  if perfectbound == "yes":
   print("Soft cover, perfect bound books are very popular!")
  
  else:
    print("Soft covers with coils or stitches are great for short books")
elif cover == "hard":
   
   print("Books with hard covers can be more expensive!")
   
print("Done")

