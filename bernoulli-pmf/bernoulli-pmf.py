import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    d = {}
    x = np.array(x)
    d["pmf"] = np.where(x==1,p,1-p)
    d["mean"] = float(p)
    d["variance"] = float(p*(1-p))
    return d