# -*- coding: utf-8 -*-
import random
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

def generate_rnd_array1(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = random.randint(0, vmax)*0.01*i
    return x

def generate_rnd_array2(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = i + 10*np.sin(2*np.pi*0.01)*random.randint(0, vmax)
    return x


def sample_array(arr: np.ndarray, n: int):
    if len(arr) < 1:
        return []
    
    to_array = []
    while n > 0:
        i = random.randint(0, len(arr)-1)
        to_array.append(arr[i])
        n-=1
    
    random_array = np.array(to_array)
    return random_array

def sort_array(arr: np.ndarray): #quick sort
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    smaller = arr[1:][arr[1:] <= pivot]  
    bigger = arr[1:][arr[1:] > pivot]
    
    return np.concatenate((sort_array(smaller), [pivot], sort_array(bigger)))

def average_time(data: np.ndarray, n: int):
    total_time = 0.0
    
    for i in range(n):
        start = perf_counter()
        sort_array(data)
        end = perf_counter()
        total_time+= (end-start)
        
    avg_time = total_time / n
    return avg_time

def estimate_complexity(data: np.ndarray, n_samples: np.ndarray):
    
    temp_array = []
    for i in n_samples:
        temp_time = average_time(data[:i], 5)
        temp_array.append(temp_time)
    complexity_array = np.array(temp_array)
    
    return complexity_array

def main():
    arr1 = generate_rnd_array1(1000)
    arr2 = generate_rnd_array2(1000)
    
    plt.figure(figsize=(5,8))
    #first plot
    plt.subplot(3,1,1)
    plt.plot(arr1, label='Array 1 unsorted', color='grey')
    plt.plot(arr2, label='Array 2 unsorted', color='black')
    plt.title('Unsorted arrays')
    plt.legend()
    #second plot
    plt.subplot(3,1,2)
    plt.plot(sort_array(arr1), label='Arr1 Sorted', color='grey')
    plt.plot(sort_array(arr2), label='Arr2 Sorted', color='black')
    plt.title('Sorted arrays')
    plt.legend()
    #third plot
    different_samples = np.arange(10,1000,15)
    avg_time1 = estimate_complexity(arr1, different_samples)
    avg_time2 = estimate_complexity(arr2, different_samples)
    plt.subplot(3,1,3)
    plt.plot(different_samples, avg_time1, label='Arr1 complexity', color='grey')
    plt.plot(different_samples, avg_time2, label='Arr2 complexity', color='black')
    plt.title('Arrays complexity')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    
if __name__ == '__main__':
    main()
    