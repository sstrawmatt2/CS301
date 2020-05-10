# Sean Strawmatt Sorting Algorithms (04/07/2020)

# The worst case for insertion sort would be O(n^2) because we have two for loops. One nested
# inside of the other. Insert might cause an issue for the algorithm because depending on where
# we insert an item, then that could take O(n) time so then it would be O(n^3).
def insertion_sort(unsorted_list):
    sorted_list = [unsorted_list[0]]
    for i in range(1, len(unsorted_list)):
        print(unsorted_list, sorted_list)
        key_value = unsorted_list[i]

        if key_value > sorted_list[-1]:
            sorted_list.append(key_value)
        else:
            for j in range(0, len(sorted_list)):
                if sorted_list[j] > key_value:
                    sorted_list.insert(j, key_value)
                    break

    return sorted_list

        # junk_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        # print(junk_list, insertion_sort(junk_list))


# The worst case for bubble sort would be O(n^2) because we have 2 for loops and one is nested
# inside of the other one. However it could be worse if inside the second for loop we were popping
# something off or doing another function that would take O(n) time. If that were happening, then
# bubble would probably run O(n^3) time, but since we are comparing two items in the second for loop
# then that time to compare is just O(1).
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1):
        for j in range(len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp


# The worst case running time for selection sort, would be O(n^2) because there are 2 for loops
# and one of them is nested inside of the other one.
def selection_sort(unsorted_list):
    for fill_item in range(len(unsorted_list)-1, 0, -1):
        position_of_max_item = 0
        for location in range(1, fill_item+1):
            if unsorted_list[location] > unsorted_list[position_of_max_item]:
                position_of_max_item = location

        temp = unsorted_list[fill_item]
        unsorted_list[fill_item] = unsorted_list[position_of_max_item]
        unsorted_list[position_of_max_item] = temp
        print(unsorted_list)


# The worst case running time for merge sort, would be O(n log n) because it is unavoidable to not
# have merge run in that time.
def merge_sort(unsorted_list):
    # empty_list = []
    # merged_list = list_one + list_two
    print("Splitting ", unsorted_list)
    if len(unsorted_list) > 1:
        mid_val = len(unsorted_list)//2
        left_half = unsorted_list[:mid_val]
        right_half = unsorted_list[mid_val:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                unsorted_list[k] = left_half[i]
                i = i + 1
            else:
                unsorted_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", unsorted_list)
    print("Final sorted list ",unsorted_list)


# The worst case for this merge sort would just be O(n) because we have three while loops
# that each take O(n) time. They do not happen inside of one another so that is why it
# would just be O(n). I did struggle with this version of the merge sort so it is not
# all the way correct.
def class_merge(list1, list2):
    output_list = list1 + list2
    i = 0
    j = 0
    while(i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            output_list.append(list1[i])
            i = i + 1
        else:
            output_list.append(list2[j])
            j = j + 1
    while i < len(list1): # adding on whatever is left of the list
        output_list.append(list1[i])
        i = i + 1

    while j < len(list2):
        output_list.append(list2[j])
        j = j + 1
    return output_list


def new_merge_sort(new_list):
    if len(new_list) <= 1:
        return new_list
    mid_point = len(new_list)//2
    left_side = new_list[:mid_point]
    right_side = new_list[mid_point:]
    sorted_left = new_merge_sort(left_side)
    sorted_right = new_merge_sort(right_side)
    return class_merge(sorted_left, sorted_right)






# SELECTION SORT
# new_list = [12, 3, 56, 1, 67, 2, 15, 30]
# selection_sort(new_list)
# print("Sorted list is: ", new_list)
#
# new_list = [-1, 0.5, 34, 67, 39, 40, 40.01, 15]
# selection_sort(new_list)
# print("Sorted list is: ", new_list)
#
# new_list = [10, 9, 8, 7, 34, 15]
# selection_sort(new_list)
# print("Sorted list is: ", new_list)


# INSERTION SORT
# new_list = [12, 3, 56, 1, 1000, -22323, 12345, .5]
# insertion_sort(new_list)
# print("Sorted list is: ", new_list)
#
# new_list = [.5, .05, .005, 5000, 50000000000, 45, 23, -1]
# insertion_sort(new_list)
# print("Sorted list is: ", new_list)


# BUBBLE SORT
# new_list = [-2,89,10000000,230000]
# bubble_sort(new_list)
# print("Sorted list is: ", new_list)
#
# new_list = [.01,.02,60]
# bubble_sort(new_list)
# print("Sorted list is: ", new_list)


#  MERGE SORT
# merge_list = [12, 4, 56, 89.02, 32, 15]
# print(merge_sort(merge_list))

# thing1 = [1, 2, 12, 56]
# thing2 = [3, 4, 13, 23]
# print(class_merge(thing1, thing2))

# test1 = [30, 49, 7, 12,-1]
# test2 = [99, 100, 15, 67, 89]
# print(class_merge(test1, test2))
