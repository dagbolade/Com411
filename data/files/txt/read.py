def search(location):
  print("searching")
  
  with open(location) as file:
   for line in file:
    print(f"Looked in {line}")
  print("Done") 

def run():
 location= search("data/files/txt/locations.txt")
run()  


