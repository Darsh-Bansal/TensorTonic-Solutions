import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.array(a)
    b = np.array(b)

    dot = np.dot(a,b)
    a = np.dot(a,a)**0.5
    b = np.dot(b,b)**0.5

    if a==0 or b==0:
        return float(0)

    return float(dot/(a*b))

    pass