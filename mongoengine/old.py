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

