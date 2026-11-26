import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    def fun(x):
        a =1 
        for i in range(x+1,n+1):
            a*=i
    
        c = 1
        for i in range(1,n-x+1):
            c*=i
    
        pmf = a/c
        pmf *= (p**x)*((1-p)**(n-x))
        return pmf

    d = {}
    d["pmf"] = fun(k)
    d["cdf"] = sum([ fun(i) for i in range(k+1) ])
    return d