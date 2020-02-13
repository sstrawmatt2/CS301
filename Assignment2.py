## correct time function
## start_time = time.time()
## value = function_name(param)
## end_time = time.time()
## return [end_time - start_time,value]

# Sean Strawmatt Assignment 2 2/11/2020


def list_tests():
    import time
    
    list_one = ["x"]
    list_two = ["x","x","x"]
    list_three = ["x,x,x"]

    lists = []
    lists.append(list_one)
    lists.append(list_two)
    lists.append(list_three)

    start = time.time()
    for i in range(100):
        list_one.append("x")
        end = time.time()

    ltime=end-start
    
    print(list_one)
    print(ltime)

    

def testtime(startvalue, increment, tries, fname, function):
    x = startvalue
    with open(fname, 'w') as fout:
        for i in range(tries):
            t = timer_one_param(function,x)
            fout.writerow(str(x)+","+str(t))
            x = x + increment



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
        






    

    
# write to csv file
