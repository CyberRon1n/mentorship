import time

print("Welcome to THE SUPER STOPWATCH")
print('\n\n\nPress ENTER to begin, then press ENTER again to end')
print('Ctrl+C to quit')

input()

print('start')
starttime = time.time()
lasttime = starttime
lapNum = 1

try:
    while True:
        input()
        laptime = round(time.time() - lasttime,2)
        totaltime = round(time.time() - starttime, 2)
        print('lap ',lapNum,totaltime,laptime,end = '')
        lapNum += 1
        lasttime = time.time()
except KeyboardInterrupt:
    print('\nDone')

