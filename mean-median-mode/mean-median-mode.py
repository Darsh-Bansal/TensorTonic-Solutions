from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.array(x)
    d = {}
    d["mean"] = float(np.mean(x))
    d["median"] = float(np.median(x))

    t = {}
    for i in x:
        if i in t:
            t[i]+=1
        else:
            t[i]=1

    t = [ (t[i],i) for i in t ]
    t.sort(key = lambda x : (-x[0],x[1]))
    d["mode"] = float(t[0][1])
    return d