# Sean Strawmatt Assignment 4 CS301 03/24/2020


def recursive_binary_search(input_list, value_to_look_for, low_index, high_index):
    if low_index > high_index:
        return False
    else:
        midpoint_index = (low_index + high_index) // 2
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
        return (old_position + 7) % self.len  # changed this for the final exam to check my work.

    # O(1)
    def hash_put(self, item_to_enter):
        # count = 0
        index_value = item_to_enter % len(self.list_one)-1
        if self.list_one[index_value] is None:
            self.list_one[index_value] = item_to_enter
            return self.list_one
        # elif count == len(self.list_one):
        #     print("Error")
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


    def hash_search(self,item_to_look_for, some_list):
        mid = self.list_one // 2
        list1 = [mid:]
        list2 = [:mid]
        if item_to_look_for in list1:
            return True
        elif item_to_look_for in list2:
            return True
        else:
            return False


my_hash = HashList(12)
print(my_hash.hash_put(25))
print(my_hash.hash_put(36))
print(my_hash.hash_put(18))
print(my_hash.hash_put(121))
print(my_hash.hash_put(126))
my_hash.hash_print()
print(my_hash.rehash_function(126))
my_hash.hash_print()



alist = [1, 11, 20, 35, 47, 67, 77]


def search_rec(item, low, high):
    if high < low:
        print("Not found")
        return False
    mp = ((high + low) // 2)
    mv = alist[mp]
    print(mp, mv)
    if mv == item:
        print(item, " found at position ", mp)
        return True
    elif mv < item:
        return search_rec(item, mp + 1, high)
    else:
        return search_rec(item, low, mp-1)


def search(item):
    return search_rec(item, 0, len(alist)-1)


ans = search(50)
print(ans)




# new_list = [1, 11, 20, 35, 47, 67, 77]
# temp = len(new_list) -1
# print(temp)
# print(new_list)


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
