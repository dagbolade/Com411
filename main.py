import basics.repetition.while_loop.ascii as ascii
import basics.repetition.while_loop.count as count
import basics.repetition.while_loop.simple as simple
print("To which program do you want to run")
programs=[
  "1. ascii.py",
  "2. count.py",
  "3. simple.py"
]
print(programs)
user=int(input())

if user == 1:
  ascii.run()
elif user == 2:
  count.run()
elif user == 3:
  simple.run()  