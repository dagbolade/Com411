#create a program to help Beep and Bop escape the large boulder.

def identify():
  print("What do you see")
  user = input().lower

  if user == "a large boulder":
    print("it is time to run")
  else:
    print("we would be fine")  


def run():
  identify()    