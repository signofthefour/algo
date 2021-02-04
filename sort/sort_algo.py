import time

class sort_algo():
    def __init__(self, arr=[], compare_function=lambda x, y: x < y, sort_algo='selection'):
        """
        Initialize the the attribute that needed for sort algo

        @param arr: the array that need to be sorted
            type: list
            default: []
        @param compare_function: the comparing function
            type: (ele1, ele2) -> boolean
                false: if ele1 > ele2
                true: if ele1 < ele2
            default: lambda x, y: x < y
        @param sort_algo: selected sort algo
        """
        self.arr = arr
        self.arr_len = len(arr)
        self.compare = compare_function
        self.sort_algo = sort_algo
    
    def sort(self):
        """
        Select the sort algo by the user choice
        """
        begin_time = time.time()
        if self.sort_algo == 'selection':
            self.selection_sort(self.arr, self.arr_len)
        elif self.sort_algo == 'bubble':
            self.bubble_sort(self.arr, self.arr_len)
        elif self.sort_algo == 'insertion_sort':
            self.insertion_sort(self.arr)
        end_time = time.time()
        time_consumption = end_time - begin_time
        print('Sort result: {} \nResult: {}\nTime consump: {}'.format(self.sort_algo, self.arr, time_consumption))

    def selection_sort(self, arr, arr_len):
        """
        Sort the arr by selection sort algorithm
        Repeatedly finding the minimum element in the entire array and place it at first place of its
        worstcase = bestcase = normal = O(n^2)

        @param arr -- list: that need to be sort
        @param arr_len -- int: len of the arr
        """
        for idx in range(len(arr)):
            idx_min = idx
            for i in range(len(arr[idx + 1:])):
                if self.compare(arr[idx + i + 1], arr[idx_min]):
                    idx_min = idx + i + 1
            # swap min element and the fisrt
            arr[idx], arr[idx_min] = arr[idx_min], arr[idx]
    
    def bubble_sort(self, arr, arr_len):
        """
        Sort the arr by bubble sort algorithm
        swap two respectively element if the compare return true until down
        worst case = normal = bestcase = O(n^2)

        @param arr -- list: that need to be sort
        @param arr_len -- int: len of the arr
        """
        begin_time = time.time()
        for idx1 in range(arr_len):
            for idx2 in range(arr_len - idx1 - 1):
                if self.compare(arr[idx1], arr[idx2 + 1]):
                    # swap (a_i, a_i+1) -> (a_i+1, a_i) if true
                    arr[idx1], arr[idx2 + 1] = arr[idx2 + 1], arr[idx1]

    def insertion_sort(self, arr):

        for i in range(1, len(arr)):
            # from the element 1, choose the current as the key
            key = arr[i]

            # from 0 to i - 1
            j = i - 1

            # iteratively traversal the arr
            while j >= 0 and key < arr[j]:
                # swap if the key is less than the element at index j
                arr[j+1] = arr[j]
                j -= 1

            arr[j-1] = key

