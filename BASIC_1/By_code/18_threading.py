

    # Multithreading example in Python.

#  It is a technique that allows a program to run multiple threads of execution
#  concurrently within the same process. 

# start(): Begin the thread's activity.
# run(): The target method that defines the thread’s activity.
# join(): Wait for the thread to finish.


from time import sleep
from threading import Thread  # import*

class Hello(Thread):    
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)  # small stagger to observe interleaving
t2.start()

t1.join()
t2.join()

print('Bye')