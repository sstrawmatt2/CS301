# Sean Strawmatt Assignment 4 CS301 03/24/2020


def recursive_binary_search(input_list, value_to_look_for, low_index, high_index):
    if low_index > high_index:
        return False
    else:
        midpoint_index = (high_index + low_index) // 2
        midpoint_value = input_list[midpoint_index]
    if midpoint_value == value_to_look_for:
        return True
    elif value_to_look_for < midpoint_value:
        return recursive_binary_search(input_list, value_to_look_for, low_index, midpoint_index - 1)
    else:
        return recursive_binary_search(input_list, value_to_look_for, midpoint_index + 1, high_index)


def in_class_binary(input_list, item_to_look_for):
    temp_val = len(input_list)-1
    return recursive_binary_search(input_list, item_to_look_for, 0, temp_val)


# my_list = [1, 2, 3, 4, 6, 7, 10, 12, 15]
# print(my_list)
# my_item = 15
# print(my_item, in_class_binary(my_list, my_item))
#
#
# my_item = 2
# print(my_item, in_class_binary(my_list, my_item))
#
#
# my_item = 100000
# print(my_item, in_class_binary(my_list, my_item))
#
#
# my_item = -2
# print(my_item, in_class_binary(my_list, my_item))


class HashList:
    def __init__(self, length):
        self.list_one = [None] * length
        self.len = length

    # O(1)
    def hash_print(self): # hash_list(length)
        print(self.list_one)

    # O(1)
    def hash_function(self, item_to_search_for):  # function in class. Finds where an item is in the list
        return item_to_search_for % self.len

    # O(1)
    def rehash_function(self, old_position):
        return (old_position + 1) % self.len

    # O(1)
    def hash_put(self, item_to_enter):
        count = 0
        index_value = item_to_enter % len(self.list_one)-1
        if self.list_one[index_value] is None:
            self.list_one[index_value] = item_to_enter
            count = count + 1
            return self.list_one
        elif count == len(self.list_one):
            print("Error")
        else:
            print("Error")

    def hash_contain(self, item_to_look_for):
        if item_to_look_for in self.list_one:
            return True
        else:
            return False

    # this one is wrong
    def hash_items(self):
        item_to_remove = None
        none_list = []
        none_occurences = 0
        for item_to_remove in self.list_one:
            none_occurences += 1
            self.list_one.remove(item_to_remove)
            none_list.append(item_to_remove)
            print(none_occurences)
            print(none_list)
            return self.list_one

    def hash_items2(self):
        new_hash_list = []
        item_counter = 0
        for item in self.list_one:
            if item is not None:
                new_hash_list.append(item)
        return new_hash_list


my_hash = HashList(5)
print(my_hash.hash_put(22))
print(my_hash.hash_put(130))
print(my_hash.hash_items2())

# Number 3
# Most of the hash list functions such as print, function, rehash, and put are all O(1).
# The best case scenario for them would be if the item that we are looking for is the first
# item in the hash list, or if it is only a few spots away from the first position in the list.
# The worst case scenario for these would be if the item in the list is a very large number, or
# if the item is one of the last in our list. The whole point of the functions being O(1) is so
# that they can run quickly and so that we can get our result. But if the item is in the last spot,
# then that would mean that our function would run O(n) time if not worse.


# Number 4
# If we were to change our hash list to a dictionary, the first thing we would have to do, would
# be to make sure that all of our data types were the same. In a hash list, you can have any data
# types you could think of. Hash lists are loosely typed compared to dictionaries. A dictionary
# requires that you have only one specific data type throughout the entire thing. Another piece that
# we would have to change if we were moving from a hash list to a dictionary, would be to have each
# item to be a key. Each place that an item would fit into, would be a key. For hash_function(), the
# return value will be the key that is associated with the item in that slot. The key and the item that
# is in that position work together so in a way, there are two items in one slot. It's known as a key:value
# pair.
