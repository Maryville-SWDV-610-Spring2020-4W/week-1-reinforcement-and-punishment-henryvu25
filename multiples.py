def is_multiple(n, m): #defined the function with two arguments
    if n % m == 0: #modulo to see if n is a multiple of m. so if n is divided by m, will the remainder be 0?
        return True
    else:
        return False #if the remainer is anything but 0, the function will return False
    
print(is_multiple(24, 4)) #this is a test inputting arguments 24 and 4 which will print the returned value True