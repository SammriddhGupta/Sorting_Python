# -*- coding: utf-8 -*-
 #program to use bubble sort in python 
 
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
A=[23,45,64,21,98,34,56]
print(bubbleSort(A))

print("Hellooooo")