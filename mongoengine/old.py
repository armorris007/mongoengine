# Prior to Python 2.5, Exception was an old-style class
import types

def subclass_exception(name, parents, unused):
    return types.ClassType(name, parents, {})

def all(iterable):
    for element in iterable:
       if not element:
          return False
    return True

def any(iterable):
    for element in iterable:
       if element:
          return True
    return False

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

