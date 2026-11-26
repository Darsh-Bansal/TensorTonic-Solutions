import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    d = {}
    d["variance"] = float(np.var(np.array(x)))*(len(x)/(len(x)-1))
    d["standard_deviation"] = d["variance"]**0.5
    return d