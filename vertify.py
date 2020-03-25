'''
@Author: your name
@Date: 2020-03-24 14:18:21
@LastEditTime: 2020-03-24 14:20:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/vertify.py
'''

def refer(a):
    print(id(a))
    a = 100
    print(id(a))

if __name__ == "__main__":
    A = 10
    print("id A is:",id(A))
    refer(A)
    print(id(A))