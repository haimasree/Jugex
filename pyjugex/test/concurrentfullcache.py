import sys
import subprocess
import time

procs = []
start_time = time.time()
for i in range(4):
    proc = subprocess.Popen([sys.executable, 'test_pyjugex.py'])
    procs.append(proc)

for proc in procs:
    proc.wait()
elapsed_time = time.time() - start_time
print(elapsed_time)
