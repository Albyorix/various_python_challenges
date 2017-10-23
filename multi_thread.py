import threading
from random import randint
from time import sleep


def print_number(number):
    # Sleeps a random 1 to 10 seconds
    rand_int_var = randint(1, 3)
    sleep(rand_int_var)
    print "Thread " + str(number) + " slept for " + str(rand_int_var) + " seconds"

thread_list = []

for i in range(1, 10):
    t = threading.Thread(target=print_number, args=(i,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

print thread_list
# This blocks the calling thread until the thread whose join() method is called is terminated.
# From http://docs.python.org/2/library/threading.html#thread-objects
for thread in thread_list:
    thread.join()

# Demonstrates that the main process waited for threads to complete
print "Done"