def search(filename):
  print("searching...")
  data = {}
  with open(filename) as file:
    for line in file:

      if line.startwith("sections"):
        file = line.split(":")
        section = file[1].strip()
      else:
        section.append(data)
        print("Done!")

def run():
  data = search("data/files/txt/books.txt")   
  with open("data/files/txt/generated.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")     

run()