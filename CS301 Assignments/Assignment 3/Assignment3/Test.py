class Node:
    # O(1)
    def __init__(self, i_data):
        self.data = i_data
        self.next_node = None

    # O(1)
    def setData(self, i_data):
        self.data = i_data

    # O(1)
    def getData(self):
        return self.data

    # O(1)
    def set_next_node(self, inode):
        self.next_node = inode

    # O(1)
    def get_next_node(self):
        return self.next_node

    # O(1)
    def __str__(self):
        returnedstatement = str(self.getData())
        return returnedstatement


class LinkedList:
    # O(1)
    def __init__(self):
        self.first_node = None

    # O(n^2) because of the self.size() method being of o(n) as well.
    def __str__(self):
        returnString = "( "
        if self is None:
            return "[]"
        else:
            i = self.size()
            current_node = self.get_first_node()
            while i > 0:
                returnString += str(current_node)+" "
                current_node = current_node.get_next_node()
                i -= 1
        return returnString+")"

    # O(1)
    def add(self, node_to_add):
        new_node = Node(node_to_add)
        new_node.set_next_node(self.get_first_node())
        self.set_first_node(new_node)

    # O(1)
    def set_first_node(self, inode):
        self.first_node = inode

    # O(1)
    def get_first_node(self):
        return self.first_node

    # O(1)
    def is_empty(self):
        if self is None:
            return True
        else:
            return False

    # O(n) - this is due to the fact that this method goes through all of the list's nodes.
    def size(self):
        current_node_loc = self.get_first_node()
        size_hunter = 0
        while current_node_loc is not None:
            size_hunter += 1
            current_node_loc = current_node_loc.get_next_node()
        return size_hunter

    # O(n) - this goes through the list until it reaches the item to find.
    def search(self, item_to_look_for):
        current_node = self.get_first_node()
        for i in range(self.size()):
            if current_node.getData() == item_to_look_for:
                return True
            else:
                current_node = current_node.get_next_node()
        return False

#Not working properly with items not in list.
    # O(n) - Despite the conditionals, this remains order N.
    def remove(self, item_to_look_for_and_remove):
        current_node = self.get_first_node()
        next_node = current_node.get_next_node()
        for i in range(self.size()):
            if i == 0 and current_node.getData() == item_to_look_for_and_remove:
                self.set_first_node(next_node)
                return "Item Eliminated"
            elif current_node.get_next_node().getData() == item_to_look_for_and_remove:
                next_node = next_node.get_next_node()
                current_node.set_next_node(next_node)
                return "Item Eliminated"
            elif i == range(self.size()-1) and next_node == item_to_look_for_and_remove:
                current_node.set_next_node(None)
                return "Item Eliminated"
            elif i == range(self.size()-1) and next_node != item_to_look_for_and_remove:
                return "Item was not found and was thus, not removed. Please try again with a better choice."
            else:
                current_node = current_node.get_next_node()
                next_node = next_node.get_next_node()
        return "Item was not found and was thus, not removed. Please try again with a better choice."

    # O(n) as it needs to progress through the nodes to the end location.
    def append(self, item_to_append):
        i = self.size()
        current_node = self.get_first_node()
        while i > 1:
            current_node = current_node.get_next_node()
            i -= 1
        if i == 1:
            node_to_append = Node(item_to_append)
            current_node.set_next_node(node_to_append)

    # O(n) as it needs to progress through the nodes to try to find the specified data.
    def index(self, item_to_find):
        current_node = self.get_first_node()
        for i in range(self.size()):
            if current_node.getData() == item_to_find:
                return i
            else:
                current_node = current_node.get_next_node()
        return False

    #O(n) because, despite there being 2 O(n)'s, they are not nested.
    def insert(self, pos, item_to_insert):
        insertion_node = Node(item_to_insert)
        searching_node = self.get_first_node()
        if pos > self.size()-1:
            return "List is too small."
        for i in range(self.size()):
            if i == pos-1:
                node_to_right = searching_node.get_next_node()
                searching_node.set_next_node(insertion_node)
                insertion_node.set_next_node(node_to_right)
                return
            else:
                searching_node = searching_node.get_next_node()

    #O(n) as there are no nested for loops, only a single one that is run concurrently with another O(n) [self.size()-1]
    def pop(self, pos):
        popped_node = self.get_first_node()
        list_size = self.size()
        if pos > list_size:
            return "Error, Will Robinson"
        for i in range(list_size-1):
            if i == 0 and pos == 0:
                popped_node = self.get_first_node()
                self.set_first_node(popped_node.get_next_node())
                return popped_node
            elif i == pos-1 and pos-1 == self.size()-2:
                left_node = popped_node
                left_node.set_next_node(None)
                popped_node = popped_node.get_next_node()
                return popped_node
            elif i == pos-1:
                left_node = popped_node
                popped_node = popped_node.get_next_node()
                left_node.set_next_node(popped_node.get_next_node())
                return popped_node
            else:
                popped_node = popped_node.get_next_node()
        return "Item was not found and was thus, not removed. Please try again with a better choice."

    #O(n) as you have to go through the entire list to pop the final Node.
    def pop_without_pos(self):
        popped_node = self.get_first_node()
        for i in range(self.size()-1):
            if i == self.size()-2:
                left_node = popped_node
                left_node.set_next_node(None)
                popped_node = popped_node.get_next_node()
                return popped_node
            else:
                popped_node = popped_node.get_next_node()

#QUESTION 3:
# The list in Python is not a Linked List, nor is it a doubly Linked List. My reasoning for this is due to the fact
# that, while you can index using negative integers, Python does not loop around from the last items in its list to the
# first or vice versa, instead it simply states the objects from one point to the next. Additionally, unless Python
# keeps an index (recognizable due to it being O(1), which a doubly-linked list often needs to help with figuring out
# certain methods and size-related functions. I am not sure what the Python list actually is, but due to these facts,
# I reiterate that I do not believe it is a linked list, or a doubly linked list.


class Stack:
    # O(1)
    def __init__(self):
        self.internal_list = []

    def push(self, item):
        self.internal_list.append(item)

    def pop(self):
        return self.internal_list.pop()

    def peek(self):
        return self.internal_list[len(self.internal_list)-1]

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


tester = LinkedList()
for x in range(10):
    soonToBeAdded = x
    tester.add(soonToBeAdded)
tester.add(10)
tester.add(15)
tester.add(3)
tester.add(7)
print(tester.size())
print(tester.is_empty())
print(str(tester.get_first_node()))
print(tester)
print(tester.search(8))
print(tester.get_first_node().get_next_node())
print(tester.append(17))
print(tester)
print(tester.remove(7))
print(tester)
print(tester.index(2))
print(tester.insert(7, 13))
print(tester)
print(tester.pop(7))
print(tester)
print(tester.pop_without_pos())
print(tester)