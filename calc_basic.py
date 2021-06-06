'''
Simple example module as a series of 
functions one would see in a calculator
'''


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b): 
    '''
    Compute a**(int(b))
    '''
    apowb = 1
    for i in range(int(b)):
        apowb = multiply(apowb, a)
    return apowb

def square(a): # pragma: no cover
    '''
    Compute a**2
    NOTE: the '# pragma no cover' line excludes 
    this entire function from the coverage report
    '''
    a2 = power(a,2)
    return a2 

if __name__ == "__main__": # pragma: no cover
    '''
    the pragma line exclude this entire clause from the coverage report as well
    the pragma clause should always be put in this clause
    because ideally you'd only want to test the individual functions
    '''
    one_plus_two = add(1,2)
    three_pow_four = power(3,4)
