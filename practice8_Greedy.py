import sys
import time
import copy
import random
from functools import cmp_to_key

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def calc_time(func):  
    def wrapper(*args, **kw):  
        start_time = time.time()  
        func(*args, **kw)
        end_time = time.time()
        print('[%s] run time is %.6f s' % (func.__name__, end_time - start_time))
    return wrapper 


class Greedy(object):
    def __init__(self):
        pass

    @calc_time
    def get_change(self, mlist, total):
        '''找零钱问题'''
        clist = [0 for _ in mlist]
        for i,m in enumerate(mlist):
            clist[i] = total//mlist[i]
            total = total%mlist[i]
        print(clist, sum(clist))
        return clist, sum(clist)


    @calc_time
    def fractional_backpack(self, glist, total_weight):
        '''背包问题，小偷偷商品，商品可以分割'''
        wlist = [0 for _ in glist]
        total_v = 0
        for i, (v, w) in enumerate(glist):
            if total_weight > w:
                wlist[i] = 1
                total_v += v
                total_weight = total_weight - w
            else:
                wlist[i] = total_weight/w
                total_v += wlist[i]*v
                break

        print(total_v, wlist)


    def number_join(self, nlist):
        '''数字拼接成最大整数'''
        slist = list(map(str, nlist))
        slist.sort(key=cmp_to_key(xy_cmp))
        return "".join(slist)


    def activity_selection(self, alist):
        slist = [alist[0]]
        for i in range(1,len(alist)):
            if alist[i][0] >= slist[-1][1]:
                slist.append(alist[i])

        return slist



def main():
    greedy = Greedy()
    print("-"*10, "1.找零钱问题", "-"*10)
    mlist = [100, 50, 20, 5, 1] #money
    greedy.get_change(mlist, 439)
    print()

    print("-"*10, "2.背包偷商品问题", "-"*10)
    glist = [(100, 20), (60, 10), (120, 30)] #(value, weight)
    glist.sort(key=lambda x : x[0]/x[1], reverse=True)
    print(glist)
    greedy.fractional_backpack(glist, 40)

    print("-"*10, "3.拼接最大数字问题", "-"*10)
    nlist = [32, 94, 128, 1286, 6, 71]
    max_num = greedy.number_join(nlist)
    print("max_num =", max_num)

    print("-"*10, "4.最多活动场次问题", "-"*10)
    # (开始时间，结束时间)
    alist = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
    random.shuffle(alist)
    print("origin alist:", alist)
    alist.sort(key = lambda x:x[1])
    print("sorted alist:", alist)
    slist = greedy.activity_selection(alist)
    print(slist)



if __name__ == '__main__':
    main()