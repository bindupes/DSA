def sum_of_digits(s):
    words = s.split()
    reverse= words[::-1]
    reverse1=" ".join(reverse)
    return reverse1
    
print(sum_of_digits("Hello i am bindu"))
        
