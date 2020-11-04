print("please enter the first whole number")
fnum = int(input())

print("please enter the second whole number")
snum = int(input())

print("please enter the third whole number")
tnum = int(input())

even_numbers = 0
odd_number = 0

#for each number entered, they would be a if and else statement for it
if fnum % 2 == 0:
  even_numbers = even_numbers + 1
else:
  odd_number = odd_number + 1  
if snum % 2 == 0:
  even_numbers = even_numbers + 1
else:
  odd_number = odd_number + 1
if tnum % 2 == 0:
  even_numbers = even_numbers + 1
else:
  odd_number = odd_number + 1
#code to display the number of even and odd even_numbers
print("They were {} even numbers and {} odd numbers". format(even_numbers, odd_number))        