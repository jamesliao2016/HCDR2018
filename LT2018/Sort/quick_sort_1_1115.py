#!/usr/bin/env python2
# coding:utf-8

'''
@author: willard
'''

def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        # print(high)
        # print(key)
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        # print(low)
        if low < high:
            array[high] = array[low]
        print(low,high)

    array[low] = key
    return low

if __name__ == '__main__':
    # array2 = [9,3,2,1,4,6,7,0,5]
    array2 = [3,2,1,5,6,4]

    print (array2)
    quick_sort_standord(array2,0,len(array2)-1)
    print (array2)
# ---------------------
# 作者：willard
# 来源：CSDN
# 原文：https://blog.csdn.net/longshenlmj/article/details/51613597
# 版权声明：本文为博主原创文章，转载请附上博文链接！