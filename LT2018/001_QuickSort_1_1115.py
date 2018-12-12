#!/usr/bin/env python2
# coding:utf-8

def parititon(s,l,r):
    val_key = s[l]
    while l<r:
        while l<r and val_key < s[r]:
            r -= 1
        if l < r:
            s[l] = s[r]
        while l<r and val_key > s[l]:
            l += 1
        print(val_key,s[l])
        if l < r:
            s[r] = s[l]
    s[l] = val_key
    return l

def quick_sort_standord(s,l,r):
    if l<r:
        val_l = parititon(s,l,r)
        print(s[l:val_l + 1])
        # print(val_l)
        quick_sort_standord(s,l,val_l)
        # print(s[l:val_l+1])
        quick_sort_standord(s,val_l+1,r)


if __name__ == '__main__':
    # array2 = [9,3,2,1,4,6,7,0,5]
    # array2 = [3,2,1,5,6,4]
    array2 = [5,6,3,4,1,2]


    print (array2)
    quick_sort_standord(array2,0,len(array2)-1)
    print (array2)
# ---------------------
# 作者：willard
# 来源：CSDN
# 原文：https://blog.csdn.net/longshenlmj/article/details/51613597
# 版权声明：本文为博主原创文章，转载请附上博文链接！


'''
@author: willard
'''
#
# def quick_sort_standord(array,low,high):

# realize from book "data struct" of author 严蔚敏
#     if low < high:
#         key_index = partion(array,low,high)
#         quick_sort_standord(array,low,key_index)
#         quick_sort_standord(array,key_index+1,high)
#
# def partion(array,low,high):
#     key = array[low]
#     while low < high:
#         while low < high and array[high] >= key:
#             high -= 1
#         # print(high)
#         # print(key)
#         if low < high:
#             array[low] = array[high]
#
#         while low < high and array[low] < key:
#             low += 1
#         # print(low)
#         if low < high:
#             array[high] = array[low]
#         print(low,high)
#
#     array[low] = key
#     return low


'''
# 19 nov, 2018
def quick_sort_standord(nums,low,high):
    if low<high:
        keyind=partition(nums,low,high)
        quick_sort_standord(nums,low,keyind)
        quick_sort_standord(nums,keyind+1,high)

def partition(nums,low,high):
    val_key = nums[low]
    while low < high:
        while low < high and nums[high] >= val_key:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        while low < high and nums[low] < val_key:
            low += 1
        if low < high:
            nums[high] = nums[low]
    nums[low] = val_key
    return low

'''