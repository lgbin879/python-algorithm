import sys
import time
import copy
import random


def calc_time(func):  
    def wrapper(*args, **kw):  
        start_time = time.time()  
        func(*args, **kw)
        end_time = time.time()
        print('[%s] run time is %.6f s' % (func.__name__, end_time - start_time))
    return wrapper 


class DynamicProgramming(object):
    def __init__(self):
        num = 0

    def _fibnacci_recursive(self, n):
        if n <= 1:
            return n

        num = (self._fibnacci_recursive(n-1)+self._fibnacci_recursive(n-2))
        #print(num)
        return num


    @calc_time
    def fibnacci_recursive(self, n):
        self.num = self._fibnacci_recursive(n)
        return self.num


    @calc_time
    def fibnacci_nonrecursive(self, n):
        fib = [0, 1, 1]
        if n<=2:
            return fib[n]

        for i in range(3,n+1):
            num = fib[-1]+fib[-2]
            fib.append(num)

        self.num = fib[-1]
        return self.num



def main():
    dp = DynamicProgramming()

    print("-"*10, "1.fibnacci_recursive", "-"*10)
    num = dp.fibnacci_recursive(30)
    print(num)

    print("-"*10, "2.fibnacci_nonrecursive", "-"*10)
    num = dp.fibnacci_nonrecursive(30)
    print(num)



if __name__ == '__main__':
    main()


