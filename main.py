import basics.repetition.while_loop.ascii as ascii
import basics.repetition.while_loop.count as count
import basics.repetition.while_loop.simple as simple
import basics.repetition.while_loop.len as len
import basics.repetition.while_loop.sum_100 as sum_100
import basics.repetition.for_loop.simple as simplee

print("To which program do you want to run")
programs=[
  "1. ascii.py",
  "2. count.py",
  "3. simple.py",
  "4. len.py",
  "5. sum_100.py",
  "6. simple.py"
]
print(programs)
user=int(input())

if user == 1:
  ascii.run()
elif user == 2:
  count.run()
elif user == 3:
  simple.run()
elif user == 4:
  len.run()      
elif user == 5:
  sum_100.run()
elif user == 6:
  simplee.run()             