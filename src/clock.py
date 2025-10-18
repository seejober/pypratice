#!/usr/bin/python3
import time

def procedure():
    time.sleep(2.5)

# time.clock
t0 = time.perf_counter()
procedure()
print (time.perf_counter() - t0)

# time.time
t0 = time.time()
procedure()
print (time.time() - t0)