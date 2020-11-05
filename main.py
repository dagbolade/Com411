import basics.repetition.while_loop.ascii as ascii
import basics.repetition.while_loop.count as count
<<<<<<< HEAD
import basics.repetition.while_loop.simple as simple
=======
>>>>>>> efdfee6cb5b1fced5c0c6f72db7a72180ebad184

print("To which program do you want to run")
programs=[
  "1. ascii.py",
<<<<<<< HEAD
  "2. count.py",
  "3. simple.py"
=======
  "2. count.py"
>>>>>>> efdfee6cb5b1fced5c0c6f72db7a72180ebad184
]
print(programs)
user=int(input())

if user == 1:
  ascii.run()
elif user == 2:
<<<<<<< HEAD
  count.run()
elif user == 3:
  simple.run()  
=======
  count.run()
>>>>>>> efdfee6cb5b1fced5c0c6f72db7a72180ebad184
