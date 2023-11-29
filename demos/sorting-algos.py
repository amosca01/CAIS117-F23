###
#
# Ab Mosca
# 11/27/2023
#
# Starter code for algorithmic analysis
###

import time 

def selectionSort(arr):
    '''
    input: unsorted array
    output: none
    does: implementation of selection sort 
    ''' 
    n = len(arr) 
    for i in range(n):
        # current index of minimum 
        min_ind = i
        # search rest of array for new min 
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        # swap 
        (arr[i], arr[min_ind]) = (arr[min_ind], arr[i])

def bubbleSort(arr):
    '''
    input: unsorted array
    output: none
    does: implementation of bubble sort 
    '''
    n = len(arr)
    for i in range(n-1):
        # loop for pairwise comparisons
        for j in range(0, n-i-1):
            # if right is bigger, swap 
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])

def insersionSort(arr):
    '''
    input: unsorted array
    output: none
    does: implementation of insertion sort 
    '''
    n = len(arr)
    for i in range(1, n):
        # current item to insert
        key = arr[i]
        # j is max index before i 
        j = i - 1 
        while j >= 0 and key < arr[j]:
            # shift items left 
            arr[j+1] = arr[j]
            j -= 1
        # insert current item 
        arr[j + 1] = key
        
def main():

    # reads text file into array of ints 
    # for you to work with 
    ints = []
    with open("bunch-of-ints.txt", "r") as file:
        for line in file:
            num = int(file.readline().strip())
            ints.append(num)
    file.close()

    ## ADD YOUR CODE HERE

if __name__ == "__main__":
    main() 