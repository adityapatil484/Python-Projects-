def reset():
   global time_left
   time_left = 0

def time_add():
   global time_left
   time_left = time_left + 1

def time_subtract():
   global time_left
   time_left = time_left - 1

def print_time():
   print(time_left)

time_left=30
time_add()
print_time()
time_subtract()
print_time()
reset()
print_time()
