def largest_shortest(arr):
    large=arr[0]
    short=arr[0]
    for num in arr:
        if arr[num]>large:
            large=arr[num]
        if arr[num]<short:
            short=arr[num]
    return short,large
