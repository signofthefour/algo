from sort_algo import sort_algo
import numpy as np

if __name__ == '__main__':
    # arr: len=1000 with elements from 0 to 1000
    arr = np.random.randint(0,1000,10000)
    com = lambda x, y: x < y
    s = sort_algo(arr, com, 'bubble')
    s.sort()