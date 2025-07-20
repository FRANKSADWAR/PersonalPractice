from __future__ import with_statement

def f(x):
    assert x < 0, 'x must be negative'
    return x **2

### This is simar to
def f(g):
    if __debug__:
        if not g < 0:
            raise AssertionError('x must be negative')
        else:
            return g ** 2

"""
The assert can be thought of a conditional raise statement. If the test evaluates to a false, Python raises an exception using the optional 
data item as a constructor argument to the Exception subclass raised.
"""

