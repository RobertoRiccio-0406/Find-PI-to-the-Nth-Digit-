def egg_count(display_value):
    resto = ''
    while display_value > 0:
        resto = str(display_value%2) + resto
        display_value //= 2
    
    
    counter = 0
    for c in resto :
        if c == '1':
            counter += 1
    return counter
        
    
        
