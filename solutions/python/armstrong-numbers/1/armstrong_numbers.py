def is_armstrong_number(number):
    numbers = str(number)
    power = len(numbers)
    result = 0
    for n in numbers:
        result += int(n)**power
    if result == number:
        return True
    else :
        return False
    

