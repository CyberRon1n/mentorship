import time

def calcprod():
    product = 1
    for i in range(1,1000):
        product = product * i
    return product

starttime = time.time()
prod = calcprod()
endtime = time.time()
print("the result is ",len(str(prod))," digits long")
print("it took ",endtime - starttime,"seconds to calculate")
