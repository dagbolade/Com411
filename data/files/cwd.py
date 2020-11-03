#check our current working folder/directory before beginning to work with files

import os
#path = os.getcwd()
#print(f"Current Working Folder Path: {path}")

#display the content of this folder
#for file in os.listdir(path):
#print(file)
def cwd():
  path = os.getcwd()
  print(f"The current working folder is {path}")
  print("The folder contains the following:")
  for file in os.listdir(path):
    print(file)

def run():
  print("processing")
  
  cwd()
run()