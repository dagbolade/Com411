import basics.repetition.while_loop.ascii as ascii
import basics.repetition.while_loop.count as count

print("To which program do you want to run")
programs=[
  "1. ascii.py",
  "2. count.py"
]
print(programs)
user=int(input())

if user == 1:
  ascii.run()
elif user == 2:
  count.run()