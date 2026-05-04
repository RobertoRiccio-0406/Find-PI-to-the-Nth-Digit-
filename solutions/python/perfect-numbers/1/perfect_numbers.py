def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisori = []
    for i in range (1, number):
        if number % i == 0:
            divisori.append(i)
    if sum(divisori) == number:
        return "perfect"
    if sum(divisori) < number:
        return "deficient"
    if sum(divisori) > number:
        return "abundant"
        
    
