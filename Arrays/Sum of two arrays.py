def add_arrays(arr1, arr2):
    # Make both arrays the same length (pad shorter one with 0s if needed)
    max_len = max(len(arr1), len(arr2))
    arr1 = arr1 + [0] * (max_len - len(arr1))
    arr2 = arr2 + [0] * (max_len - len(arr2))
    
    # Add elements pairwise
    result = [arr1[i] + arr2[i] for i in range(max_len)]
    return result
