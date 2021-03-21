from sort_algo import sort_algo, QuickSort
import argparse
import numpy as np

def main(args):
    # arr: len=1000 with elements from 0 to 1000
    if args.case == 'normal':
        arr = np.random.randint(0,1000,10000)
        compare_func = lambda x, y: x < y
        s = sort_algo(arr, compare_func, args.algo)
        s.sort()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Expect dir for gen process.')
    # parser.add_argument('--case', type=str, default='normal', help="best, worst, or normal (random)")
    # parser.add_argument('--algo', type=str, default='insertion_sort', help="the sort algo ")

    # args = parser.parse_args()
    # main(args)
    a = [12, 0, 9 , 3, 1, 5, 2, 11, 3, 8, 4]
    qs = QuickSort(a)
    qs.sort()