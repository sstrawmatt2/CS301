import time
import random

def timer_one_param(function_name,param):
    
    start_time = time.time()
    value = function_name(param)
    end_time = time.time()
    return [end_time - start_time,value]



def timerFunction(f,input):
    time1=time.time()
    f(input)
    time2 = time.time()

    return time2-time1

# Sean Strawmatt Assignment 2 2/11/2020


def list_tests(): # practice lists
    
    list_one = ["x"]

    start = time.time()
    for i in range(100):
        list_one.append("x")
        end = time.time()

    ltime=end-start
    
    print(list_one)
    print(ltime)

    
# example that we started in class    
def testtime(startvalue, increment, tries, fname, function):
    x = startvalue
    with open(fname, 'w') as fout:
        for i in range(tries):
            t = timer_one_param(function,x)
            fout.writerow(str(x)+","+str(t))
            x = x + increment


## Writing lists to csv file(Allen Adams)
def writeLists(f, start, end, numDataPoints, outputFile):
    file_out = open(outputFile,"w+")
    input_value = start
    increment = (end-start) // numDataPoints

    for i in range(numDataPoints):
        data_dict = createDictionary("words.txt",input_value)
        runtime = functionTime(f, data_dict)
        file_out.write(f"{str(len(data_dict))},{str(runtime)}\n")
        input_value += increment
        
    file_out.close()



def basicList():
    rnew_rando = randint(1,999)
    data2 = [1,2,3,45,67,8,6,5,4,3,4,12,3,17,1,2,3,45,67,8,6,5,4,3,4,12,3,17,1,2,3,45,67,8,6,5,4,3,4,12,3,17]
    dataTime2 = 0

    start = time.time()
    for i in range(1000):
        data2.append(new_rando)
    end = time.time()

    dataTime2 = end - start

    print(dataTime2)

