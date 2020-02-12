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

    
# write to csv file
