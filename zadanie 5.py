import math
import random
import time
from random import shuffle

t = 1
cooling = 0.9
MAX_EPOCH = 5
MAX_TRIES = 3

def f(x):
    result = 3 * math.sin(math.pi * x / 5) + math.sin(math.pi * x)
    return result

a = random.uniform(0, 10)

start_time = time.time()
for x in range(MAX_EPOCH):
    t = t*0.9
    for y in range(MAX_TRIES):
        if y > MAX_TRIES:
            y = 0
        if (a-2*t < 0):
            b = random.uniform(0, (a+2*t))
        else:
            b = random.uniform(a-2*t, a+2*t)
        if f(a) < f(b):
            a = b
        else:
            temp = random.random()
            exp = math.exp((f(b)-f(a))/t)
            if temp < exp:
                a = b
exec_time =  time.time() - start_time

print("x wynosi:", a)
print("f(x) wynosi:", f(a))
print("czas: ", exec_time)
        



