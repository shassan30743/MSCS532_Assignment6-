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
