def is_pangram(sentence):
    alfabeto = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    lower = sentence.lower()
    for chr in alfabeto:
        if chr not in lower:
            return False
    return True    
        
    
