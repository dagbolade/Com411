#Added code to demonstrate the use of a while loop with ascii art.
print("How many bars should be charged")
user = int(input())

#createvariable to track the number of bars charged and set this to 0.
bars = 0
while (bars < user) :
  print("Charging...:", end ="")
  #Increment the variable for tracking the number of charged bars.
  bars = bars + 1
  print("█ " * bars)

print("\nThe battery is fully charged.")
