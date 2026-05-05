def square(number):
    result = 1
    if number < 1 :
        raise ValueError("square must be between 1 and 64")
    if number > 64 :
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return result
    if number > 1:
        for n in range (1,number):
            result *= 2
    return result        
            


def total():
    result = [1]
    temp = 1
    for n in range (1,64):
        temp *= 2
        result.append(temp)
    somma = sum(result)
    return somma    
