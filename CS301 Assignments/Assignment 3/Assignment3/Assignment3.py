# Sean Strawmatt Assignment 3 2/25/2020

class Node:

    def __init__(self,idata):
        self.data = idata
        self.nextnode = None


    def setdata(self,idata):
        self.data = idata
        
    
    def getdata(self):
        return self.idata
        

    def setnextnode(self, inode):
        self.nextnode = inode


        

class Linked_List:

    def __init__(self):
        self.firstnode = None

    def add(self, item):
        self.firstnode = True
        
        

    def remove(self,item):
        self.firstnode.remove(item)


    def search(self,item):
        self.firstnode.search(item)
    

    def printList(self):
        temp = self.firstnode
        while(temp):
            print (temp.idata,
            temp = temp.next)



def main():
    
    my_list = Linked_List()
    my_list.add(5)
    my_list.add(13)
    my_list.add(44)

    print(my_list)


