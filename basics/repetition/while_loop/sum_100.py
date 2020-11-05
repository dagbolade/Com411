def run():
  print("calculating the sum of the first 100 numbers")

  numbers = 1
  total = 0
  while numbers <= 100 :
    total = total + numbers
    numbers = numbers + 1
  print("Done the answer is {}".format(total))