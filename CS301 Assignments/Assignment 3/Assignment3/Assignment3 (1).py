# Jessica Herold, Stephen Provost, and Sean Strawmatt
# A3 CS301 (03/06/2020)
# Dr. Miller


class Node:
    # O(1)
    def __init__(self, i_data):
        self.data = i_data
        self.next_node = None
        self.past_node = None

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

    def set_past_node(self, n_past_node):  # n_past is new past node
        # Constant time
        self.past_node = n_past_node

    def get_past_node(self):
        # Constant time
        return self.past_node

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

    # Not working properly with items not in list.
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

    # O(n) because, despite there being 2 O(n)'s, they are not nested.
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

    # O(n) as there are no nested for loops, only a single one that is run concurrently with another O(n)[self.size()-1]
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

    # O(n) as you have to go through the entire list to pop the final Node.
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


class DoubList:
    def __init__(self):
        # Constant time = O(1)
        self.start = None
        self.global_size = 0

    def __str__(self):
        returnString = "( "
        if self is None:
            return "[]"
        else:
            i = self.size()
            now_node = self.get_start()
            while i > 0:
                returnString += str(now_node) + " "
                now_node = now_node.get_next_node()
                i -= 1
        return returnString + ")"
    
    # O(1) 
    def set_start(self, n_next_node):
        self.start = n_next_node
    # O(1) 
    def get_start(self):
        return self.start
    # O(1)
    def get_global_size(self):
        return self.global_size
    # O(1)
    def increase_global_size(self):
        self.global_size += 1
    # O(1)
    def decrease_global_size(self):
        self.global_size -= 1

    def add(self, item):
        # Constant time /  O(1) because we aren't going through the list. We're just referencing the one before and after
        if self.start is not None:
            old_node = self.start
            n_node = Node(item)
            previous_node = old_node.get_past_node()
            n_node.set_next_node(old_node)  # n_node is new node
            n_node.set_past_node(previous_node)
            previous_node.set_next_node(n_node)
            old_node.set_past_node(n_node)
            self.increase_global_size()

        if self.start is None:
            n_node = Node(item)
            self.start = n_node
            n_node.set_past_node(n_node)
            n_node.set_next_node(n_node)
            self.increase_global_size()

    # O(1)
    def is_empty(self):
        # Constant time
        if self.start is None:
            return True
        else:
            return False

    # def remove(self, item):  # not working properly
    #     # Linear time
    #     current_node = self.get_start()
    #     item_there = False
    #     while not item_there:
    #         if current_node.get_data() == item:
    #             next_node = current_node.get_next_node()
    #             del current_node
    #             if last_node == None:
    #                 self.start = next_node
    #             else:
    #                 last_node.set_next_node(next_node)
    #                 item_found = True
    #         else:
    #             last_node = now_node
    #             now_node = now_node.get_next_node()

    # O(n) because we are referencing so many different "places" at a time that I think it would be O(n) or O(1)
    def remove(self, item):
        current_node = self.get_start()
        time_limit = self.get_global_size()
        while time_limit > 0:
            if current_node.getData() == item:
                next_node = current_node.get_next_node()
                previous_node = current_node.get_past_node()
                previous_node.set_next_node(next_node)
                next_node.set_past_node(previous_node)
                self.decrease_global_size()
                time_limit = 0
                return "Item Eliminated"
            else:
                current_node = current_node.get_next_node()
                time_limit -= 1
        return "Item Not Found"

    # O(n)
    def search(self, item):
        # Linear time
        current_node = self.get_start()
        time_limit = self.get_global_size()
        while time_limit > 0:
            if current_node.getData() == item:
                return True
            else:
                current_node = current_node.get_next_node()
                time_limit -= 1
        return False

    # O(n)
    def size(self):
        # Linear time
        return self.get_global_size()

    # O(n)
    def append(self, item):  # n node is new node!!
        # Linear time
        n_node = Node(item)
        now_node = self.start
        past_node = now_node.get_past_node()
        if now_node is None:
            self.add(item)
        else:
            past_node.set_next_node(n_node)
            n_node.set_past_node(past_node)
            n_node.set_next_node(now_node)
            now_node.set_past_node(n_node)
            self.increase_global_size()

    # O(n)
    def index(self, item):
        # Linear time
        item_i = 0  # item index
        now_node = self.start
        timer = self.get_global_size()
        while timer > 0:
            if now_node.getData() == item:
                return item_i
            else:
                now_node = now_node.get_next_node()
                item_i += 1
                timer -= 1

    # O(n)
    def insert(self, pos, item):
        # Linear time
        now_node = self.start
        now_i = 0  # Current index
        index_there = False
        n_node = Node(item)
        while now_i >= 0:
            if now_node is None and pos == 0:
                self.add(item)
                break
            elif now_node is None:
                return "Index Error"
            elif pos == now_i:
                next_node = now_node.get_next_node()
                next_node.set_past_node(n_node)
                n_node.set_past_node(now_node)
                n_node.set_next_node(next_node)
                now_node.set_next_node(n_node)
                self.increase_global_size()
                break
            else:
                now_node = now_node.get_next_node()
                now_i += 1

    def pop(self):
        current_node = self.get_start()
        if current_node is not None:
            soon_to_be_gone_node = current_node.get_past_node()
            previous_node = soon_to_be_gone_node.get_past_node()
            previous_node.set_next_node(current_node)
            current_node.set_past_node(previous_node)
            self.decrease_global_size()
            return "Item Eliminated"
        else:
            return "List too short."

    # O(n)
    def pop_pos(self, pos):
        # Linear time
        now_node = self.start
        now_i = 0  # Current index
        while now_i >= 0:
            if now_node is None:
                return "Index Error"
            elif pos == now_i:
                next_node = now_node.get_next_node()
                past_node = now_node.get_past_node()
                next_node.set_past_node(past_node)
                past_node.set_next_node(next_node)
                self.decrease_global_size()
                break
            else:
                now_node = now_node.get_next_node()
                now_i += 1

# QUESTION 3:
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

    # O(1)
    def push(self, item):
        self.internal_list.append(item)

    # O(1)
    def pop(self):
        return self.internal_list.pop()

    # O(n) due to needing to cycle through the list to return the last item.
    def peek(self):
        return self.internal_list[len(self.internal_list)-1]

    # O(1)
    def is_empty(self):
        return self.size() == 0

    # O(n) due to it needing to cycle through the list.
    def size(self):
        return len(self.internal_list)


class Queue:
    # O(1)
    def __init__(self):
        self.internal_list = []

    # O(1)
    def enqueue(self, item):
        self.internal_list.append(item)

    # O(n), due to needing to go through the list.
    def pop(self):
        return self.internal_list.pop(0)

    # O(1)
    def is_empty(self):
        return self.size() == 0

    # O(1)
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



# new_list = Deque()
# for x in range(10):
#     new_list.add_front(x)
# 
# print(new_list)
# new_list.add_front(12)
# print(new_list)
# new_list.add_rear(4)
# print(new_list)
# new_list.remove_front()
# print(new_list)
# new_list.remove_rear()
# print(new_list)
# 
# print(new_list.size())
# print(new_list.is_empty())


# testStack = Stack()
# for x in range(10):
#     testStack.push(x)
# print(testStack.peek())
# print(testStack.pop())
# print(testStack.peek())
# print(testStack.size())
# print(testStack.is_empty())

# tester = LinkedList()
# for x in range(10):
#     soonToBeAdded = x
#     tester.add(soonToBeAdded)
# tester.add(10)
# tester.add(15)
# tester.add(3)
# tester.add(7)
# print(tester.size())
# print(tester.is_empty())
# print(str(tester.get_first_node()))
# print(tester)
# print(tester.search(8))
# print(tester.get_first_node().get_next_node())
# print(tester.append(17))
# print(tester)
# print(tester.remove(7))
# print(tester)
# print(tester.index(2))
# print(tester.insert(7, 13))
# print(tester)
# print(tester.pop(7))
# print(tester)
# print(tester.pop_without_pos())
# print(tester)

print("DoubleList")
Testing = DoubList()
Testing.add(1)
Testing.add(2)
Testing.add(3)
Testing.add(4)
Testing.add(5)
Testing.add(6)
print(Testing.remove(5))
print(Testing)
print(Testing.search(4))
print(Testing.append(10))
print(Testing)
print(Testing.index(4))
print(Testing.insert(16, 5))
print(Testing)
print(Testing.pop())
print(Testing)
print(Testing.pop_pos(7))
print(Testing)
