import sys
import fileinput
import time
from math import floor

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
            if str(i)[0:floor((len(str(i))/2))] == str(i)[floor((len(str(i))/2)):]:
                print(f"Found match: {i} in range {bounds[0]}-{bounds[1]}")
                result += i

print(f"Sum: {result}")
print(f"--- {(time.time() - startTime)} seconds ---")
