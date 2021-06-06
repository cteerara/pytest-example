
from calc_basic import *

def factorial(a):
    '''
    Compute a!
    '''
    if a == 1: return 1
    else: return a*factorial(a-1) 

def exp(a, tol=1e-6):
    '''
    Compute exp(a) using taylor series expansion
    stop when the differences in each iteration is less than tol
    '''
    import copy
    exp_a = 1
    exp_a_old = 0
    residue = tol+1 # Some initial value for residue that is more than tol
    k = 1
    while residue > tol:
        exp_a_old = copy.deepcopy(exp_a)
        exp_a = add( exp_a , divide( power(a, k), factorial(k)  )  )
        residue = abs( exp_a - exp_a_old )
        k = add( k, 1 )
    return exp_a

def trig(a, is_sin=True ,tol=1e-6):
    '''
    Compute either sin(a) or cos(a) depending on is_sin 
    stop when the differences in each iteration is less than tol
    '''
    import copy
    if is_sin:
        sin_a = a
        sin_a_old = 0
        residue = tol+1 # Some initial value for residue that is more than tol
        k = 1
        while residue > tol:
            sin_a_old = copy.deepcopy(sin_a)
            one_plus_two_k = add(1, multiply(2,k))
            sin_a = add( sin_a , divide( multiply(power(-1, k), power(a,one_plus_two_k)), factorial(one_plus_two_k)  ) ) 
            residue = abs( sin_a - sin_a_old )
            k = add( k, 1 )
        return sin_a

    else: 
        cos_a = 1
        cos_a_old = 0
        residue = tol+1 # Some initial value for residue that is more than tol
        k = 1
        while residue > tol:
            cos_a_old = copy.deepcopy(cos_a)
            two_k = multiply(2,k)
            cos_a = add( cos_a, divide( multiply( power(-1,k) , power( a, two_k )   )  , factorial(two_k) ) )
            residue = abs( cos_a - cos_a_old )
            k = add( k, 1 )
        return cos_a














