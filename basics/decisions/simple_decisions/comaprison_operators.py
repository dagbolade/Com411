print("please enter your first number")
fnum = int(input())

print("please enter your second number")
snum = int(input())

#using comparison operator to know which one is the smallest
if fnum < snum :
  print("The first number is smallest")
elif snum < fnum :
  print("The second number is the smallest")
else:
  print("Both numbers are equal")
  
print("Done!")  