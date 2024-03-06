import threading, time

print('start of program')

def takeanap():
    time.sleep(5)
    print('wake up!')

threadobj = threading.Thread(target=takeanap)
threadobj.start()

print('End of program')


