import time
from bisect import bisect
import datetime
import pickle
import random
        

def choose(in_lst, n, in_chosen=[]):
    """choose n items by weighting from a list of (item, weighting) tuples
    returns (chosen, remainder)
    
    Warning! This is a probabilistic test. It could fail occasionally!
    
    >>> a = range(10)                       #ten items available to choose from
    >>> w = [2] + [1] * (len(a)-1)          #first item (0) has twice the weighting of the others
    >>> avail = zip(a,w)
    >>> runs = 100
    >>> first_chosen = len([1 for i in range(runs) if 0 in choose(avail,5)[0] ])
    >>> first_chosen / float(runs) > 0.5    #first item will be chosen more often because of its bigger weighting
    True
    
    >>> print choose([],5)
    ([None, None, None, None, None], [])
    """
    lst = in_lst[:]
    chosen = in_chosen[:]
    if not lst or len(chosen) == n:
        return ([c[0] for c in chosen] + [None] * (n - len(chosen)), [c[0] for c in lst])
    else:
        #make random choice from list based on weightings
        wtotal = sum([x[1]**2 for x in lst])
        r = random.uniform(0, wtotal)
        for item, weight in lst:
            ws = weight**2
            if r < ws:
                break
            r = r - ws
        c = (item,weight)

        chosen.append(c)
        lst.remove(c)
        return choose(lst, n, chosen)

