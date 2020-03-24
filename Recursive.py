'''
@Author: your name
@Date: 2020-03-24 14:02:16
@LastEditTime: 2020-03-24 14:06:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/Recursive.py
'''

def main(array):
    res = mySum(array)
    print(res)

def mySum(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return 0
    else:
        res = array[0] + mySum(array[1:])
        return res

if __name__ == "__main__":
    array = [3,4,5]
    main(array)