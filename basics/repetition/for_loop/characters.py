# create a program that allows us to display a word character by character.
def run():
  print("what strange markings do you see")
  user = input()

  for index in range(0, len(user), 1):
    print("ind", index, ":" ,user[index]  )