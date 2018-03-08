import sys
import subprocess
import time

procs = []
start_time = time.time()
for i in range(int(sys.argv[1])):
    proc = subprocess.Popen([sys.executable, 'test_pyjugex_emptycache.py'])
    procs.append(proc)

for proc in procs:
    proc.wait()
elapsed_time = time.time() - start_time
print(elapsed_time)
