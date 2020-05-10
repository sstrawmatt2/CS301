# CS301 - Assignment 2
# Lists vs Dictionaries

# By: Allen Adams, 

# IMPORTANT: Create folder call csvs in the same directory as this file(Assignment2.py)
import time

#################################################################################
#################################################################################

#Overhead Section

#################################################################################
#Esablish a Function Timer

def functionTimer(f, input):

    time1 = time.time()
    f(input)
    time2 = time.time()
    
    return time2 - time1

#################################################################################
#Writes List Based Timer Values to CSV file

def writeLists(f, start, end, numDataPoints, outputFile):

    file_out = open(outputFile, "w+")
    input_value = start  
    increment = (end-start) // numDataPoints
    
    for i in range(numDataPoints):
        dataList = listConverter(input_value)
        runtime = functionTimer(f, dataList)
        file_out.write(f"{str(len(dataList))},{str(runtime)}\n")
        input_value += increment
        
    file_out.close()
    
#################################################################################
#Writes Dictionary Based Timer Values to CSV file
    
def writeDict(f, start, end, numDataPoints, outputFile):
    
    file_out = open(outputFile, "w+")
    input_value = start 
    increment = (end-start) // numDataPoints
    
    for i in range(numDataPoints):
        data_dict = createDictionary("words.txt",input_value)
        runtime = functionTimer(f, data_dict)
        file_out.write(f"{str(len(data_dict))},{str(runtime)}\n")
        input_value += increment
        
    file_out.close()
    
#################################################################################
#Creates List
#(using words.txt)
    
def listConverter(amount):
    
    values = []
    times = 0
    
    with open("words.txt") as fi:
        for line in fi:
            if times > amount:
                #allows list to be trimmed to a more manageable size
                return values
            else:
                values.append(line.strip())
                times += 1
                
#################################################################################              
#Creates Dictionary
#(using specified input method in this case we use words.txt)
                
def createDictionary(fileName,numItems):
    
    dictionary = {}
    count = 0

    with open(fileName) as f:
        words = f.read().splitlines()

    #concatonate each item to the dictionary
    for i in words:
        dictionary[count] = i
        count +=1
    
        if  count == numItems:
            #allows dictionary size to be trimmed
            break
        
    return dictionary

#################################################################################
#################################################################################
#################################################################################

#List vs Dictionary Section

#################################################################################
#Append List vs Append Dictionary

#Append List
#(adds XXXX to the end of the list)
def append_list(data):
    
    return data.append("XXXX")

#Append Dictionary
#(adds XXXX to the dictionary)
def append_dict(data):

    data[len(data)] = "XXXX"
    return True
#################################################################################
#Delete Lists vs Delete Dictionary

#Delete List
#(Removes last element in the list)
def delete_list(data):

    del data[-1]

    return  True

#Delete Dictionary
#(Removes last elemnt in the dictionary)
#(uses libaraies list/ keys to envoke element)
def delete_dict(data):
   
    last_key = list(data.keys())[-1]
    del data[last_key]

    return True

#################################################################################
#Sort List vs Sort Dictionary

#Sort List
def sort_list(data):

    return data.sort()

#Sort Dictionary
#(Dictionaries come pre sorted after python 3.7)
#(Appended alphabeticaly)
def sort_dict(data):

    return False

#################################################################################
# Concatonation List vs Concationation Dictionary

#Concationation List
#(Adds XXXX to the end of each element)
def concat_list(data):

    return [l + "XXXX" for l in data]

#Concatonation Dictionary
#(Adds XXXX to each element in dictionary)
def concat_dict(data):

    for index in data:
        data[index] = data[index] + "XXXX"

    return True

#################################################################################
#Index[0] List vs Index[0] Dictionary

#First Element List
#(Gets 0 indexed element in the list)
def first_list(data):

    return data[0]

#First Element Dictionary
#(Gets 0 indexed element in the dict)
def first_dict(data):

    return data[0]

#################################################################################
#Index[last] List vs Index[last] Dictionary

#Last Element List
#(-1 wraps around to get last element)
def last_list(data):

    return data[-1]

#Last Element Dictionary
#(uses libaraies list/ keys to envoke element)
def last_dict(data):
   
    last_key = list(data.keys())[-1]

    return data[last_key]

#################################################################################
#Count List vs Count Dictionary

#Count Lists
#(manualy count number of elements in the list)
def count_list(data):

    numOfElements = 0
    for element in data:
        numOfElements += 1
        
    return numOfElements

#Count Dictionary
#(manualy count number of elements in the Dictionary)
def count_dict(data):

    numElements = 0
    for element in data:
        numElements += 1
        
    return numElements

#################################################################################
#Length List vs Length Dictionary

#Length of List
def length_list(data):

    return len(data)

#Length of Dictionary
def length_dict(data):

    return len(data)

#################################################################################
#################################################################################
#################################################################################

#Call Functions Section

#################################################################################

#Determine Sampe Size for Dictionary/ List
def main(number_of_elements=100000):

    #Set input file for data
    inputFile = "words.txt"
   
    print("Thinking", end="")
    #Call Write functions for each test method
    #(given as: function name, Starting Index, Last Index, Number of Data Points, Output File Name)
    
    #Append
    writeLists(append_list, 1, number_of_elements, 20, "csvs/append_list.csv")
    writeDict(append_dict, 1, number_of_elements, 20, "csvs/append_dict.csv")
    print(".", end="")

    #Delete
    writeLists(delete_list, 1, number_of_elements, 20, "csvs/delete_list.csv")
    writeDict(delete_dict, 1, number_of_elements, 20, "csvs/delete_dict.csv")
    print(".", end="")
    
    #Sort
    writeLists(sort_list, 1, number_of_elements, 20, "csvs/sort_list.csv")
    writeDict(sort_dict, 1, number_of_elements, 20, "csvs/sort_dict.csv")
    print(".", end="")

    #Concatination
    writeLists(concat_list, 1, number_of_elements, 20, "csvs/concat_list.csv")
    writeDict(concat_dict, 1, number_of_elements, 20, "csvs/concat_dict.csv")
    print(".", end="")

    #Fist Indexed Element
    writeLists(first_list, 1, number_of_elements, 20, "csvs/first_list.csv")
    writeDict(first_dict, 1, number_of_elements, 20, "csvs/first_dict.csv")
    print(".", end="")

    #Last Indexed Element
    writeLists(last_list, 1, number_of_elements, 20, "csvs/last_list.csv")
    writeDict(last_dict, 1, number_of_elements, 20, "csvs/last_dict.csv")
    print(".", end="")

    #Count
    writeLists(count_list, 1, number_of_elements, 20, "csvs/count_list.csv")
    writeDict(count_dict, 1, number_of_elements, 20, "csvs/count_dict.csv")
    print(".", end ="")

    #Length
    writeLists(length_list, 1, number_of_elements, 20, "csvs/length_list.csv")
    writeDict(length_dict, 1, number_of_elements, 20, "csvs/length_dict.csv")
    print(".")

    print("Done!")
    print("check csvs folder")
    
    

if __name__ == "__main__":
    main()
