class Node:
    def __init__(self, i_data):  # i_date is input data
        # Constant time
        self.data = i_data
        self.next_node = None
        self.previous_node = None

    def set_data(self, n_data):  # n_data is new data
        # Constant time
        self.data = n_data

    def get_data(self):
        # Constant time
        return self.data

    def set_next_node(self, n_next_node):  # n_next is new next node
        # Constant time
        self.next_node = n_next_node

    def get_next_node(self):
        # Constant time
        return self.next_node

    def set_past_node(self, n_past_node):  # n_past is new past node
        # Constant time
        self.past_node = n_past_node

    def get_past_node(self):
        # Constant time
        return self.past_node


class DoubList:
    def __init__(self):
        # Constant time
        self.start = None

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

    def set_start(self, n_next_node):
        self.start = n_next_node

    def get_start(self):
        return self.start

    def add(self, item):
        # Constant time
        if self.start is not None:
            old_node = self.start
            n_node = Node(item)
            n_node.set_next_node(self.start)  # n_node is new node

            self.start = n_node
            old_node.set_past_node(old_node)
            n_node.set_past_node(old_node)

        if self.start == None:
            n_node = Node(item)
            self.start = n_node
            n_node.set_past_node(n_node)
            n_node.set_next_node(None)
            node_tail = Node(item)

    def remove(self, item):  # not working properly
        # Linear time
        now_node = self.start
        last_node = None
        item_there = False
        while not item_there:
            if now_node.data == item:
                next_node = now_node.get_next_node()
                del now_node
                if last_node is None:
                    self.start = next_node
                else:
                    last_node.set_next_node(next_node)
                item_found = True
            else:
                last_node = now_node
                now_node = now_node.get_next_node()

    def search(self, item):
        # Linear time
        node = self.start
        item_there = False
        while not item_there:
            if node.data == item:
                item_there = True
            else:
                node = node.get_next_node()
                if node is None:
                    break
        return item_there

    def isEmpty(self):
        # Constant time
        if self.start is None:
            return True
        else:
            return False

    def size(self):
        # Linear time
        number_nodes = 0
        node = self.start
        while node is not None:
            number_nodes += 1
            node = node.get_next_node()
        return number_nodes

    def append(self, item):  # n node is new node!!
        # Linear time
        n_node = Node(item)
        now_node = self.start
        if now_node is None:
            self.start = n_node
        else:
            last_node = False
            while not last_node:
                next_node = now_node.get_next_node()
                if next_node is None:
                    now_node.set_next_node(n_node)
                    n_node.set_past_node(now_node)
                    last_node = True
                else:
                    now_node = now_node.get_next_node()

    def index(self, item):
        # Linear time
        item_i = 0  # item index
        item_there = False
        now_node = self.start
        while not item_there:
            if now_node.get_data() == item:
                item_there = True
            if now_node == None:
                print("Index Error")
            else:
                now_node = now_node.get_next_node()
                item_i += 1
        return item_i

    def insert(self, pos, item):
        # Linear time
        now_node = self.start
        now_i = 0  # Current index
        index_there = False
        n_node = Node(item)
        while not index_there:
            if now_node is None and pos == 0:
                self.add(item)
                index_there = True
            elif now_node is None:
                print("Index Error")
            elif pos == now_i + 1:
                next_node = now_node.get_next_node()
                n_node.set_past_node(now_node)
                n_node.set_next_node(next_node)
                if next_node is None:
                    now_node.set_next_node(n_node)
                else:
                    n_node.set_next_node(next_node)
                    now_node.set_next_node(n_node)
                index_found = True
            else:
                now_node = now_node.get_next_node()
                now_i += 1

    def pop(self):  # I'll start working on it
        # Linear time
        now_node = self.start
        while True:
            if now_node is None:
                print("Index error")
            elif now_node.get_next_node() is None:
                item = now_node.get_data()
                del now_node
                self.start = None
                return item
            elif now_node.get_next_node().get_next_node() is None:
                next_node = now_node.get_next_node()
                item = next_node.get_data()
                del next_node
                now_node.set_next_node(None)
                return item
         # else:
         #     now_node = now_node.get_next_node()


tester = DoubList()
for x in range(10):
    soonToBeAdded = x
    tester.add(soonToBeAdded)
tester.add(10)
print(tester.size())
print(tester.search(9))
# tester.remove(10)
# tester.remove(10)
print(tester.isEmpty())
# tester.append(12)
print(tester.append(12))
print(tester.size())
# print(tester)
print(tester.index(3))
print(tester.insert(4, 10))

# Print tester using the __str__ method is unfortunately not working correctly at the moment.
# tester.remove is not working correctly as well.