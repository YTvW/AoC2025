import sys
import fileinput
import time

if len(sys.argv) >=2:
    fileName = sys.argv[1]
else:
    fileName = "input"

dial = 50
startTime = time.time()
dialAtZero = 0
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if cleanLine[0] == 'L':
        dial -= int(cleanLine[1:])
    elif cleanLine[0] == 'R':
        dial += int(cleanLine[1:])
    if dial % 100 == 0:
        dialAtZero += 1
    # print(cleanLine)
    print("Dial now at: ", dial)
    print("dialMod 100: ", dial % 100)

print("Dial ended at: ", dial % 100)
print("Dial hit zero ", dialAtZero, " times")
print("--- %s seconds ---" % (time.time() - startTime))