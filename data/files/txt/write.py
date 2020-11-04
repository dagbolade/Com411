def search(location):
  print("Searching...")
  sections = []
  books = []

  with open(location) as file:
    for line in file:
      if (line.startswith("Sections")):
        data =line.split(":")
        sections.append(data[1][:-1])
      else:
        books.append(data[0][:-1])  
  print("Done.")
  return(sections,books)


def save(filename,data):
  print("Saving...")
  with open(filename, "w") as file:
   file.write(f"Sections: {data[0]}")
   file.write(f" Books: {data[1]}")
  print("Done!") 

def run():
 data  = search("data/files/txt/books.txt")
 save("data/files/txt/write.txt", data)

run() 

