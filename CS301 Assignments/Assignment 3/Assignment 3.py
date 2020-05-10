# Sean Strawmatt Assignment 3 2/25/2020
# Dr. Miller

class Node:

    def __init__(self, idata):
        self.data = idata
        self.nextnode = None
        self.removenode = None

    def set_data(self, idata):
        self.data = idata

    def get_data(self):
        return self.data

    def set_next_node(self, inode):
        self.nextnode = inode

    def get_next_node(self):
        return self.nextnode

    def remove_node(self, rnode):
        self.removenode = rnode

    def __str__(self):
        return str(self.get_data())


class Linked_List:

    def __init__(self):
        self.firstnode = None

    def list(self):
        new_list = []
        return new_list

    def add(self, item):
        newnode = Node(item)
        newnode.set_next_node(self.firstnode)
        self.firstnode = newnode

    def get_first_node(self):
        return self.firstnode

    # def remove(self, item):
    #     deleteNode = Node(item)
    #     deleteNode.removeNode(self.firstnode)
    #
    #     if deleteNode not in list():
    #         print("Node not in list")

    def search(self, item):
        search_node = self.get_first_node()
        for i in range(self.size()):
            if search_node.get_data() == item:
                return True
            else:
                print(search_node.get_data())
                search_node = search_node.get_next_node()
                print(search_node)
        return False

        # searchNode = self.firstnode
        # if searchNode in list():
        #     return True
        # elif searchNode not in list():
        #     return False

    def isEmpty(self):
        # eList = list()
        # if len(eList==0):
        #     return True
        # else:
        #     return False

        if self is None:
            return True
        else:
            return False

    def size(self):                                 # credits to Stephen Provost
        current_node = self.firstnode
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.get_next_node()
        return counter

    def insert(self, pos, item):
        newnode = Node(item)
        currnode = self.firstnode
        for i in range(pos-1):                          # usually when you see a for loop, it's linear time
            currnode = currnode.getNextNode()
        follow_node = currnode.getNextNode()
        currnode.setNextNode(newnode)
        newnode.set_next_node(follow_node)

    def append(self,item):
        appendnode = Node(item)
        list.append(appendnode)

    # def printList(self):                     # tutorial point - https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
    #     printLists = self.firstnode
    #     while printLists is not None:
    #         print(printLists.idata)
    #         printLists = printLists.nextnode



class Stack:
    def __init__(self):
        self.internal_list = []

    def push(self, item):
        self.internal_list.append(item)
        # runs in O(1) time.

    def pop(self):
        return self.internal_list.pop()

    def peek(self):
        return self.internal_list.index(1)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.internal_list)


class Queue:
    def __init__(self):
        self.internal_list = []

    def enqueue(self, item):
        self.internal_list.append(item)

    def pop(self):
        return self.internal_list.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.internal_list)


class Deque:
    # 0(1)
    def __init__(self):
        self.deque_list = []

    # O(1)
    def add_front(self,front_item):
        self.deque_list.insert(0, front_item)
    # O(1)
    def add_rear(self,rear_item):
        self.deque_list.append(rear_item)
    # O(1)
    def remove_front(self):
        first_index = self.deque_list.pop(0)
        return first_index
    # O(n)
    def remove_rear(self):
        last_index = len(self.deque_list)
        self.deque_list.pop(last_index-1)
        return last_index
    # O(n)
    def size(self):
        return len(self.deque_list)

    # O(n)
    def __str__(self):
        print_string = "( "
        if self is None:
            return "[]"
        else:
            for i in range(self.size()):
                worlds_most_annoying_int = self.deque_list[i]
                print_string += str(worlds_most_annoying_int) + " "
        print_string += ")"
        return print_string
    # O(1)
    def is_empty(self):
        return self.size() == 0
    # O(n)
    def test_str(self):
        return self.deque_list[len(self.deque_list)-1]



new_list = Deque()
for x in range(10):
    new_list.add_front(x)

print(new_list)
new_list.add_front(12)
print(new_list)
new_list.add_rear(4)
print(new_list)
new_list.remove_front()
print(new_list)
new_list.remove_rear()
print(new_list)

print(new_list.size())
print(new_list.is_empty())
