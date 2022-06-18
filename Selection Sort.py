#
# #Selection sort Function with a list called "A"
#
# # first find the smallest number
# # Selection sort in Python
# def selectionSort(array, size):
#     for i in range(size): # setting the first element as minimum
#         min_idx = i
#
#         for j in range(i + 1, size): # +1 index because first index is already the minimum, and will check the next index
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[j] < array[min_idx]: #in this next loop it will check if array J is less than first minimum value
#                 min_idx = j
#
#         # put min at the correct position
#         (array[i], array[min_idx]) = (array[min_idx], array[i])
#
#
# data = [-2, 45, 0, 11, -9,98,34,5,12]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)
# print (size)



# def SelectionSort2(array, size):
#     for y in range(size):
#         minIndex = y
#
#         for h in range (y + 1, size):
#             if array[h] < array[minIndex]:
#               minIndex = h
#
#         (array[y], array[minIndex]) = (array[minIndex], array[y]) # how to sort
#
# datatwo = [2,7,34,8,3,6,3,4,90]
#
# size =len(datatwo)
# SelectionSort2(datatwo, size)
# print(datatwo)
# print(size)


# def anotherFuntion (array, size):
#     for i in range (size):
#         minIndex = i
#
#         for j in range(i + 1, size):
#             if array[j] < array[minIndex]:
#                 minIndex = j
#
#         (array[i], array[minIndex]) = (array[minIndex], array[i] )
#
# data = [ 9,23,4,2,54,6,2,5,100]
# size = len(data)
#
# anotherFuntion(data,size)
# print(data)
# print(size)


# def anotherFunction (array, size):
#     for i in range(size):
#         minIndex = i
#
#         for j in range(i + 1, size):
#             if array [j] < array[minIndex]:
#                 minIndex = j
#
#         (array[i], array[minIndex]) = (array[minIndex], array[i])
#
#
# data = [1,56,84,45,7,7,54,]
# size = len(data)
#
# anotherFunction(data, size)
#
# print (data)
















# def lastAttempt (array, size):
#     for i in range(size):
#         minIndex = i
#
#         for j in range( i+1, size):
#             if array[j] < array[minIndex]:
#                 minIndex = j
#
#         (array[i], array[minIndex]) = (array[minIndex], array[i])
#
#
# array = [56,2,34,6,32,5,7,3,4,65]
#
# size = len(array)
#
# lastAttempt(array, size)
#
# print (array)
#



def SelectionSort(array, size):
    for i in range(size):
        minIndex = i

        for j in range(i + 1, size):
            if array[j] < array[minIndex]:
                minIndex = j

        (array[i], array[minIndex]) = array[minIndex], array[i]


array = [8,34,3,6,7,3,5,6,87]

size = len(array)

SelectionSort(array, size)
print(array)













