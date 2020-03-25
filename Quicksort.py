'''
@Author: your name
@Date: 2020-03-24 14:53:30
@LastEditTime: 2020-03-25 09:03:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/Quicksort.py
'''

def quickSort(array,inverse=False):
    if len(array) == 0 or len(array) == 1: # len(array) < 2
        return array
    else:
        index = 0
        pivot = array[index]
        rest = array[:index] + array[index+1:]
        
        small =[ item for item in rest if item < pivot]
        big = [item for item in rest if item >= pivot]
        if not inverse:
            return quickSort(small,False) + [pivot] + quickSort(big,False)
        else:
            return quickSort(big,True) + [pivot] + quickSort(small,True)


if __name__ == "__main__":
    array = [2,2,6,4,9]
    res = quickSort(array,True)
    print(res)