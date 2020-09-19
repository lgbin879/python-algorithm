import sys
import time
import copy
import random

def calc_time(func):  
    def wrapper(*args, **kw):  
        start_time = time.time()  
        func(*args, **kw)
        end_time = time.time()
        print('\n[%s] run time is %.6f s' % (func.__name__, end_time - start_time))
    return wrapper 


class Sorting(object):
    def __init__(self):
        pass

    @calc_time
    def bubble_sort(self, alist):
        lens = len(alist)
        for i in range(lens-1):
            for j in range(lens-1-i):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]


    @calc_time
    def bubbleE_sort(self, alist):
        lens = len(alist)
        for i in range(lens-1):
            need_swap = 0
            for j in range(lens-1-i):
                if alist[j] > alist[j+1]:
                    need_swap += 1
                    alist[j], alist[j+1] = alist[j+1], alist[j]
            if not need_swap:
                return


    @calc_time
    def select_sort(self, alist):
        lens = len(li)
        for i in range(0, lens-1):
            min_loc = i
            min_val = li[i]
            for j in range(i+1, lens):
                if li[j] < min_val:
                min_val = li[j]
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
            

    def partition(self, alist, left, right):
        pivot = alist[left]
        while left < right:
            while left < right and alist[right] > pivot:
                right = right - 1
            alist[left] = alist[right]
            while left < right and alist[left] < pivot:
                left = left + 1
            alist[right] = alist[left]

        alist[left] = pivot
        return left


    def _quick_sort(self, alist, left, right):
        if left < right:
            mid = self.partition(alist, left, right)
            self._quick_sort(alist, left, mid-1)
            self._quick_sort(alist, mid+1, right)


    @calc_time
    def quick_sort(self, alist):
        lens = len(alist)
        self._quick_sort(alist, 0, lens-1)



if __name__ == "__main__":
    sort_obj = Sorting()
    sys.setrecursionlimit(100000) # set recursion limit
    #alist = [54,26,93,17,77,31,44,55,20]
    alist = list(range(0, 10000))
    random.shuffle(alist)
    #print(alist)
    li1 = copy.deepcopy(alist)
    li2 = copy.deepcopy(alist)
    sort_obj.bubbleE_sort(li1)
    #print(li1)
    sort_obj.quick_sort(li2)
    #print(li2)





