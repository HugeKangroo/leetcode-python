'''
@Author: your name
@Date: 2020-02-29 20:37:39
@LastEditTime: 2020-03-24 18:55:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm Study/Sorting/sort.py
'''
# def reverse_queue()

def exchange_element(queue,a_index,b_index):
    # tmp = None
    # tmp = queue[a_index]
    # queue[a_index] = queue[b_index]
    # queue[b_index] = tmp

    queue[a_index],queue[b_index] = queue[b_index],queue[a_index]
    return queue

def quick_sort(queue,reverse=False):
    if len(queue) <= 1:
        return queue
    else:
        index = 0
        pivot = queue[index]
        rest = queue[:index] + queue[index+1:]
        small = [i for i in rest if i < pivot]
        big = [i for i in rest if i >= pivot]
        if not reverse:
            return quick_sort(small,reverse) + [pivot] + quick_sort(big,reverse)
        else:
            return quick_sort(big,reverse) + [pivot] + quick_sort(small,reverse)

def bubble_sort(queue,reverse=False):
    length = len(queue)
    # sorted_queue = []
    for i in range(length):
        for j in range(length-1):
            if reverse:
                if queue[j] < queue[j+1]:
                    queue = exchange_element(queue,j,j+1)
                else:
                    continue
            else:
                if queue[j] > queue[j+1]:
                    queue = exchange_element(queue,j,j+1)
                else:
                    continue
        length -= 1
    return queue

def select_sort(queue,reverse=False):
    def min_of_queue(queue):
        minimum = queue[-1] 
        _id = len(queue) - 1
        for i in range(len(queue)-1):
            if queue[i] < minimum:
                minimum = queue[i]
                _id = i
            else:
                continue
        return minimum,_id

    def max_of_queue(queue):
        maximum = queue[-1]
        _id = len(queue) - 1
        for i in range(len(queue)-1):
            if queue[i] > maximum:
                maximum = queue[i]
                _id = i
            else:
                continue
        return maximum,_id



    length = len(queue)
    begin = 0
    for i in range(begin,length-1):
        if reverse:
            _,_id = max_of_queue(queue[begin:length])
            queue_id = begin+_id
            queue = exchange_element(queue,begin,queue_id)
            begin += 1
        else:
            _,_id = min_of_queue(queue[begin:length])
            queue_id = begin+_id
            queue = exchange_element(queue,begin,queue_id)
            begin += 1
            # length -= 1
    return queue

def insert_sort(queue,reverse=False):
    def find_insert_index(sorted_queue,item,reverse=False):
        out_index = 0
        for i in range(len(sorted_queue)):
            if reverse:
                if sorted_queue[i] > item and i != len(sorted_queue) - 1:
                    continue
                if sorted_queue[i] <= item:
                    out_index = i - 1 
                    return out_index
                if i == len(sorted_queue) - 1:
                    return i

            else:
                if sorted_queue[i] < item and i != len(sorted_queue) - 1:
                    continue
                if sorted_queue[i] >= item:
                    out_index = i - 1 
                    return out_index
                if i == len(sorted_queue) - 1:
                    return i
        # out_index = 0 if out_index < 0 else out_index
        # return out_index

    
    def insert(queue,index,item):
        length = len(queue)
        inserted_queue = [ 0 for i in range(length+1)]
        # inserted_queue[index] = item
        for i in range(length+1):
            if i < index :
                inserted_queue[i] = queue[i]
            elif i == index:
                inserted_queue[i] = item
            else:
                inserted_queue[i] = queue[i-1]
        return inserted_queue
        
    length = len(queue)
    sorted_list = [queue[0]]
    # sorted_list = sorted_list + [queue[0]]
    index = 1
    while len(sorted_list) < length :
        item = queue[index]
        insert_id = find_insert_index(sorted_list,item,reverse)
        sorted_list = insert(sorted_list,insert_id+1,item)
        index += 1
    return sorted_list
        
if __name__ == "__main__":
    import math
    import random

    NUM_LEN = 10
    seed = random.seed(0)
    input_list = [ random.randint(1,100) for i in range(NUM_LEN)]
    print("input list is:",input_list)
    FUN = quick_sort
    sorted_list = FUN(input_list,True)
    print(FUN.__name__,"sort list is:",sorted_list)
    # sorted_list = bubble_sort(input_list,False)
    # print("bubble sorted list is:",sorted_list)
    # sorted_list = select_sort(input_list,False)
    # print("select sorted list is:",sorted_list)