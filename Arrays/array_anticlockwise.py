#Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
def rotateArr(arr,d):
    n=len(arr)
    d=d%n # this is done so that i rotation is larger than the array ,
    # suppose [1,2,3,4,5] and d=7 , so if we do 7%5 = 2 , so we do rotation 2 times which is generally equal to rotations done for 7 times
    arr[:]=arr[d:]+arr[:d]
    print(arr)

rotateArr([1,2,3,4,5],2)