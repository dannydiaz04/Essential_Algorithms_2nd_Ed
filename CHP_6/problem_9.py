'''
Write a program that implements heapsort
'''

# the idea is to heapify an unsorted array which turns
# our array into a max-heap binary tree where every parent node
# is greater in value than its child nodes' value


def heapSort(arr):
    # get the length of the array for iteration
    n = len(arr)

    # build a max-heap using all non-leaf nodes since leaf nodes are heapified by definition
    # non-leaf nodes start at n//2 -1 index. -1 index ensures we also get root node index
    for i in range(n //2 -1, -1, -1):
        heapify(arr, n, i)

    # swap the first and last element in the sorted list
    # remove the node from the heap
    # call on heapify to restructure the heap and maintain max-heap property
    for i in range(n - 1, 0, -1): # right to left traversal
        arr[0], arr[i] = arr[i], arr[0] # swap
        # heapify 
        heapify(arr, i, 0) # 0 is to pass in the root node
    
    # return sorted array
    return arr

def heapify(arr, n, i):
    largest = i
    # this is how we build a heap using arrays
    left = 2*i + 1 
    right = 2*i + 2

    # left would be larger than n meaning we've reached the end of the left subtree
    if left < n and arr[left] > arr[largest]:
        # set largest to left
        largest = left

    # right would be larger than n meaning we've reached the end of the right subtree
    if right < n and arr[right] > arr[largest]:
        # set largest to right
        largest = right

    # current node isn't largest then call heapify again recursively
    if largest != i:
        # swap 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # largest ensures that we are passing in the current parent node

def testHeapSort():
    # test case 1: Already sorted array
    assert heapSort([1,2,3,4,5]) == [1,2,3,4,5]

    # Test case 2: Reverse sorted array
    assert heapSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test case 3: Array with duplicate elements
    assert heapSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # Test case 4: Array with negative numbers
    assert heapSort([-5, 2, -1, 0, 3, -4]) == [-5, -4, -1, 0, 2, 3]

    # Test case 5: Array with one element
    assert heapSort([42]) == [42]

    # Test case 6: Empty array
    assert heapSort([]) == []

    # Test case 7: Array with all elements the same
    assert heapSort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

    # test case 8: Large random array
    import random
    largeArray = [random.randint(-1000, 1000) for _ in range(1000)]
    assert heapSort(largeArray) == sorted(largeArray)

    print("All test cases passed!")

testHeapSort()