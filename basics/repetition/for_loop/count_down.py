def run():

  print("How far are we from the cave")
  user = int(input())
 
  for count in range(user, 0, -1):
   print(count, "Steps remaining")