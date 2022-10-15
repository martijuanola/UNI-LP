## P80049   Ús d'iterables

def count_unique(L):
    return len(set(L))

    """
    AUX = []
    for x in L:
        if not x in AUX:
            AUX.append(x)
    return len(AUX)
    """


########################################

def remove_duplicates(L):
    return set(L)
    
    """
    AUX = []
    for x in L:
        if not x in AUX:
            AUX.append(x)
    return AUX
    """
    

########################################

from functools import reduce

def flatten(L):
    return reduce(lambda a, b: a + b, L, [])


########################################

def flatten_rec(L):
    return reduce(lambda a, b: a + flatten_rec(b) if isinstance(b, list) else a + [b], L, [])


########################################