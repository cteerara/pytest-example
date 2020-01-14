def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    c = 0
    for i in range(0,b):
        c+=a
    return c

def test_multiply():
    assert multiply(2,3) == 6
