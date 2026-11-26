import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x = np.array(X,dtype = 'float64')
    sh = x.shape
    exp = np.mean(x,axis = 0)
    x -= exp
    x = x.T@x
    x = x/(sh[0]-1)
    
    return x