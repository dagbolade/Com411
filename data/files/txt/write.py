def search(location):
  print("Searching...")
  sections = []
  books = []

  with open(location) as file:
    for line in file:
      if (line.startswith("Sections")):
        data =line.split(":")[1]
        sections.append(data.strip())
      else:
        books.append(line.strip())  
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

