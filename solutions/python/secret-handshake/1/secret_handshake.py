def commands(binary_str):
    action = []
    bin = list(binary_str)
    
    if bin[-1] == "1":
        action.append("wink")
    if bin[-2] == "1":
        action.append("double blink")
    if bin[-3] == "1":
        action.append("close your eyes")
    if bin[-4] == "1":
        action.append("jump")
    if bin[0] == "1":
        action.reverse()
        
    
    return action
    
