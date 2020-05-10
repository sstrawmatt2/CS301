################################################################################
#                              Assignment 1                                    #
#                                                                              #
# PROGRAMMER:       Kiley Krosky and Sean Strawmatt                            #
# CLASS:            CS301                                                      #
# ASSIGNMENT:       Assignment 1                                               #
# INSTRUCTOR:       Dr. Miller                                                 #
# SUBMISSION DATE:  01/22/20                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
# This assingment covers various problems that can be solved using alogrithms  #
# and data structures.                                                         #
################################################################################

################################################################################
# timers                                                                       #
################################################################################
def timer_one_param(function_name,param):
    start_time=time.time()
    value=fuction_name(param)
    end_time=time.time()
    return (end_time-start_time, value)

def timer_two_param(function_name,param1,param2):
    start_time=time.time()
    value=fuction_name(param1,param2)
    end_time=time.time()
    return (end_time-start_time, value)

################################################################################
# question 1                                                                   #
################################################################################


################################################################################
# count1(n)                                                                    #
#                                                                              #
# Purpose:     Calculates the sum of the first n positive integers             #
# Parameters:                                                                  #
#           n                                                                  #
# Return Value:  num (the sum)                                                 #
################################################################################
def count1(n):
    num=0
    for a in range(n+1):
        num+=a
    return num

################################################################################
# count2(n)                                                                    #
#                                                                              #
# Purpose:     Calculates the sum of the first n positive integers             #
# Parameters:                                                                  #
#           n                                                                  #
# Return Value:  sum                                                           #
################################################################################
def count2(n):
    sum = n*(n+1)/2
    return sum

################################################################################
# count3(n)                                                                    #
#                                                                              #
# Purpose:     Calculates the sum of the first n positive integers             #
# Parameters:                                                                  #
#           n                                                                  #
# Return Value:  sum                                                           #
################################################################################
def count3(n):
    sum=0
    while(n!=0):
        sum=sum+n
        n=n-1
    return sum




################################################################################
# question 2                                                                   #
################################################################################


################################################################################
# q2(word)                                                                     #
#                                                                              #
# Purpose:     Checks to see if a word is a valid scrabble word                #
# Parameters:                                                                  #
#           word                                                               #
# Return Value:  True (if the word is found) or False (if not found)           #
################################################################################
def q2(word):
    with open('words.txt') as file:
        words = file.read()
        
        if word in words:
            return True
        else:
            return False



################################################################################
# question2(word)                                                              #
#                                                                              #
# Purpose:     Checks to see if a word is a valid scrabble word                #
# Parameters:                                                                  #
#           word                                                               #
# Return Value:  num (the sum)                                                 #
################################################################################

# This is a second solution but is very slow compared to the one above

def question2(word):  
    file = open("words.txt","r")
    lines = file.read()

    wordList=[]
    
    for i in lines.split('\n'):
        wordList.append(i)
        for w in wordList:
            if word == w:
                return True
    return False



################################################################################
# question 3                                                                   #
################################################################################

            
################################################################################
# q3(tiles,word)                                                               #
#                                                                              #
# Purpose:     Checks to see if a word can be made from the given tiles        #
# Parameters:                                                                  #
#           word                                                               #
# Return Value:  True (if the word is found) or False (if not found)           #
################################################################################
def question3(tiles,word):
    maxChar = 256
    freq = [0] *  maxChar  
    for i in range(0 , len(tiles)): 
        freq[ord(tiles[i])] += 1

   
    for i in range(0, len(word)): 
        freq[ord(word[i])] -= 1
        if (freq[ord(word[i])] < 0):  
            return False
        else:
            return True
  

################################################################################
# question 4                                                                   #
################################################################################

    
  
################################################################################
# question4()                                                                  #
#                                                                              #
# Purpose:     Checks to see all the words made from a set of tiles            #
# Parameters:                                                                  #
#           none                                                               #
# Return Value:  a list of all the words  (empty list if none are found)       #
################################################################################  
def question4():
    givenTiles = ['r', 'e', 't', 'a', 'i', 'n', 's'] 
    file = open("words.txt","r")
    lines = file.read()
    wordList=[]
    rearrangedWords=[]
    for i in lines.split('\n'):
        wordList.append(i)
    for word in wordList: 
        flag = 1
        counter = {} 
        for i in word: 
            counter[i] = counter.get(i, 0) + 1 
        for key in counter: 
            if key not in givenTiles: 
                flag = 0
            else: 
                if givenTiles.count(key) != counter[key]: 
                    flag = 0
        if flag == 1:
            if len(word)==len(givenTiles):
                rearrangedWords.append(word)
                
    return rearrangedWords 
  


################################################################################
# question 5                                                                   #
################################################################################

# I could not code this fully but if it were finished, it should take all the
# letters from the spelling bee puzzle and should be put together to form words
# greater than 5 letters. Then it would have to make sure that the central
# letter is accounted for at least once and then it would print the word


# This is what I have so far, it finds all the words containing those letters
# but does not take into acocunt more than one of each letter, so those
# words are not included


def charCount(word): 
    count = {} 
    for i in word: 
        count[i] = count.get(i, 0) + 1
    return count
  
  
def question5():
    givenTiles = ['r', 'a', 'b', 'l', 'c', 'i', 'n']
    centralLetter='l'
    file = open("words.txt","r")
    lines = file.read()
    wordList=[]
    for i in lines.split('\n'):
        wordList.append(i)
    for word in wordList: 
        flag = 1
        chars = charCount(word) 
        for key in chars: 
            if key not in givenTiles: 
                flag = 0
            else: 
                if givenTiles.count(key) != chars[key]: 
                    flag = 0
        if flag == 1:
            if len(word)>=5:
                if word.find(centralLetter)!=-1:
                    print(word) 

################################################################################
# question 6                                                                   #
################################################################################
    

# I could not figure out the full solution, but I have an idea of what would
# need to be incorporated in the code: This code would need to test all the
# combinations of 8 letters and determine which combo forms the most words.



# I had time to attempt this but did not have time to finish. I started by 
# adding all the 8 letter words to a list. Then, I would compare the first word
# to all the other 8 letter words to find the anagrams which would be removed
# from the original list. Then, the words removed would be added to a new list
# and would become the max and would compare to the next list of anagrams and
# which ever is the max would take over and the process repeats until the actual
# max is found.

def q6():
    

    
    file = open("words.txt","r")
    lines = file.read()
    wordList=[]
    Anagrams=[]
    for i in lines.split('\n'):
        if len(i)==8:
            wordList.append(i)
            

    firstWord = wordList[1]            
    for word in wordList: 
        flag = 1
        counter = {} 
        for i in word: 
            counter[i] = counter.get(i, 0) + 1 
        for key in counter: 
            if key not in firstWord: 
                flag = 0
            else: 
                if firstWord.count(key) != counter[key]:
                    flag = 0
        
        if flag == 1:
            if len(word)==len(firstWord):
                Anagrams.append(word)
                
          
    return Anagrams




