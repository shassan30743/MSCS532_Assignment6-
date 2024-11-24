import random

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
