import sys
import fileinput
import time
from re import search
if len(sys.argv) >=2:
    fileName = sys.argv[1]
else:
    fileName = "input"

result =0
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    ranges = cleanLine.split(",")
    for r in ranges:
        bounds = r.split("-")
        for i in range(int(bounds[0]), int(bounds[1])+1):
            match ={search(r"^(.+)\1+$", str(i))}
            if match != {None} :
                result += i

print(f"Sum: {result}")
print(f"--- {(time.time() - startTime)} seconds ---")
