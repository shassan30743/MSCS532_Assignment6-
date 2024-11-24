import time
import random

def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    pivot = select(medians, len(medians)//2)
    
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return select(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return select(right, k - len(left) - len(equal))

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return randomized_select(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return randomized_select(right, k - len(left) - len(equal))

def measure_time(func, arr, k):
    start = time.time()
    result = func(arr.copy(), k)
    end = time.time()
    return end - start

sizes = [1000, 10000, 100000]
distributions = ['random', 'sorted', 'reverse_sorted']

with open('output.txt', 'w') as f:
    for size in sizes:
        for dist in distributions:
            if dist == 'random':
                arr = [random.randint(1, 1000000) for _ in range(size)]
            elif dist == 'sorted':
                arr = list(range(1, size+1))
            else:  # reverse_sorted
                arr = list(range(size, 0, -1))
            
            k = size // 2  # Find median
            
            det_time = measure_time(select, arr, k)
            rand_time = measure_time(randomized_select, arr, k)
            
            output = f"Size: {size}, Distribution: {dist}\n"
            output += f"Deterministic: {det_time:.6f} seconds\n"
            output += f"Randomized: {rand_time:.6f} seconds\n\n"
            
            f.write(output)
            print(output)

print("Results have been exported to output.txt")
