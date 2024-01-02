def switch_challenge_level1(comb1: str, comb2: str) -> int: 
    if len(comb1) != 4 or len(comb2) != 4: 
        raise ValueError("Ugyldig params")
    
    int_as_list = ["","","",""]
    for index, color in enumerate(comb1):
        match_index = comb2.find(color)
        int_as_list[match_index] = str(index+1)

    int_as_str = ""
    for number in int_as_list: 
        int_as_str += number

    return int(int_as_str)    


def switch_challenge_level2(comb1: str, comb2: str, *levels: list[int], ref: None|list[int] = None) -> bool|list[int]:
    if len(comb1) != 4 or len(comb2) != 4: # checks for error
        raise ValueError("Ugyldig params")
    for number in levels[0]:
        new_comb = transform(comb1, number)
        if len(levels) == 1: 
            if new_comb == comb2:
                return [*ref, number]
        else: 
            if ref != None: 
                new_ref = [*ref, number]
            else: 
                new_ref = [number]
            
            val = switch_challenge_level2(new_comb, comb2, *levels[1:], ref=new_ref)
            if val: 
                return val
    
    if len(levels) == 1: 
        return False


def transform(comb1: str, number: int) -> str: 
    # checks for error 
    if len(comb1) != 4: 
        raise ValueError("Ugyldig params")
    
    number_as_list = list(str(number))
    new_comb_as_list = ["", "", "", ""]
    for index, color in enumerate(comb1): 
        new_comb_as_list[number_as_list.index(f"{index+1}")] = color # basically finner indexen hvor fargen er representert i tallet, og setter det til gitt farge

    return "".join(new_comb_as_list)

