import time
from heapq import heappop, heappush

def create_list(size, max):
    from random import randint
    return[randint(0,max) for _ in range(size)]

def bubble_sort(list, draw_data, tick):
    for i in range(0, len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                draw_data(list, ["red" if x == j or x == j+1 else "white" for x in range(len(list))])
                time.sleep(tick)
                list[j], list[j+1] = list[j+1], list[j]
                draw_data(list, ["" if x == j or x == j+1 else "white" for x in range(len(list))])
                time.sleep(tick)
    return list

def insertion_sort(list, draw_data, tick):
    index = range(1, len(list))
    for i in index:
        sort_value = list[i]
        draw_data(list, ["green" if x == sort_value else "white" for x in range(len(list))])
        time.sleep(tick)        
        while list[i-1] > sort_value and i > 0:
            draw_data(list, ["green" if x == i or x == i-1 else "white" for x in range(len(list))])
            time.sleep(tick)
            list[i] , list[i-1] = list[i-1], list[i]
            draw_data(list, ["yellow" if x == i or x == i-1 else "white" for x in range(len(list))])
            time.sleep(tick)
            i -= 1
    return list

def selection_sort(list, draw_data, tick):
    for i in range(len(list)):
        min_pos = i
        draw_data(list, ["yellow" if x == i else "white" for x in range(len(list))])
        time.sleep(tick)
        for j in range(i, len(list)):
            if list[j]<list[min_pos]:
                min_pos = j
                draw_data(list, ["yellow" if x == j else "white" for x in range(len(list))])
                time.sleep(tick)
        list[i], list[min_pos] = list[min_pos], list[i]
        draw_data(list, ["green" if x == i or x == min_pos else "white" for x in range(len(list))])
        time.sleep(tick)

    return list
        
def heap_sort(list, draw_data, tick):
    heap = []
    for i in list:
        heappush(heap,i)
        draw_data(heap, ["yellow" if x == i else "yellow" for x in range(len(heap))])
        time.sleep(tick)

    sort = []
    while heap:
        sort.append(heappop(heap))
        draw_data(sort, ["green" for x in range(len(sort))])
        time.sleep(tick)

    return sort

def quick_sort(list, draw_data, tick):
    length = len(list)
    if length < 1:
        return list
    else:
        draw_data(list, ["orange" if x == (len(list) - 1) else "white" for x in range(len(list))])
        time.sleep(tick)
        pivot = list.pop()
        time.sleep(tick)
    
    items_greater = []
    items_smaller = []

    for items in list:
        if items > pivot:
            draw_data(list, ["red" if x == items else "white" for x in range(len(list))])
            time.sleep(tick)
            items_greater.append(items)
        else:
            draw_data(list, ["yellow" if x == items else "white" for x in range(len(list))])
            time.sleep(tick)
            items_smaller.append(items)

    q_sorted = quick_sort(items_smaller, draw_data, tick)  + [pivot] + quick_sort(items_greater, draw_data, tick)
    return q_sorted 

def merge(a,b, draw_data, tick):
    c= []
    a_index = b_index = 0
    while a_index < len(a) and b_index < len(b):   
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index += 1
        else:
            c.append(b[b_index])
            time.sleep(tick)
            b_index += 1
        draw_data(c, ["yellow" for _ in range(len(c))])
    if a_index == len(a) : 
        c.extend(b[b_index:])
        time.sleep(tick)
    else:                  
        c.extend(a[a_index:])
        time.sleep(tick)
    return c

def merge_sort(a, draw_data, tick):
    if len(a) <= 1: return a
    left, right = merge_sort(a[:len(a)//2], draw_data, tick) , merge_sort(a[len(a)//2:], draw_data, tick)
    return merge(left, right, draw_data, tick)



