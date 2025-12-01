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

    if int(cleanLine[1:]) > 100 or int(cleanLine[1:]) < 0:
        turnCount = abs(int(cleanLine[1:])) // 100
        dialAtZero += turnCount
    change = abs(int(cleanLine[1:]) % 100)
    if cleanLine[0] == 'L':
        lastDial = dial% 100
        dial -= change
        if dial %100 > lastDial& lastDial !=0:
            dialAtZero += 1
        elif dial %100 ==0:
            dialAtZero += 1
    elif cleanLine[0] == 'R':
        lastDial = dial % 100
        dial += change
        if dial %100< lastDial & lastDial !=0:
            dialAtZero += 1
        elif dial %100 ==0:
            dialAtZero += 1
    dial = dial % 100
    
print("Dial ended at: ", dial % 100)
print("Dial hit zero ", dialAtZero, " times")
print("--- %s seconds ---" % (time.time() - startTime))