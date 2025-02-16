import sys
import bisect
import io
import os
import math
import inspect
from data.gradbits import *
from data.containers import *
from data.miscfunc import *
from data.string import *
from data.fstream import *
from data.iostream import *
from data.rand import *
from data.time import *

def println(content):
    sys.stdout.write(str(content))

def scanln():
    return input() #sys.stdin.readline()

def scanb(bits):
    return sys.stdin.read(bits)

def scanf():
    return vector(sys.stdin.readlines())

def fmt(*args):
    string = ""
    for arg in args:
        string += str(arg)
    return string

def system(command):
    os.system(command)

def TERNARY_OPERATOR(condition, ifrun, elserun):
    if condition: return ifrun
    else: return elserun

def ioconnect(tied): 
    global IOold, IObuffer
    if not tied:
        IObuffer = io.StringIO()
        IOold = sys.stdout
        sys.stdout = IObuffer
    else:
        sys.stdout = IOold
        println(IObuffer.getvalue())



class Container:
    def sized(default_value, *sizes):
        if not sizes:
            return default_value
        sizes = tuple(map(int, sizes))
        return [Container.sized(default_value, *sizes[1:]) for _ in range(sizes[0])]
    


class Alog:
    def sort(array, reversed=False):
        return sorted(array, reverse=reversed)
    
    def upper_bound(array, value):
        return bisect.bisect_right(array, value)
    
    def lower_bound(array, value):
        return bisect.bisect_left(array, value)
    
    def binary_search(array, value):
        return bisect.bisect_left(array, value)
    
    def reverse(array):
        return reversed(array)
    
    def pair(array):
        return enumerate(array)
    



class Ynums:
    def is_prime(n: int):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def lcm(a: int, b: int) -> int:
        return (a * b) // Ynums.gcd(a, b) 
        
class Bound:
    def upper_bound(array, value, lo, hi):
        return bisect.bisect_right(array, value, lo, hi)
    
    def lower_bound(array, value, lo, hi):
        return bisect.bisect_left(array, value, lo, hi)
    
    def binary_search(array, value, lo, hi):
        return bisect.bisect(array, value, lo, hi)

class Integer:
    def to(vals: str):
        return list(map(int, (vals.split())))
    
    def make(val):
        return int(val.strip())
    
    def raw(val):
        return int(val)
    
    def binary(val):
        return bin(val)[2:]
    
    def total(array):
        return sum(array)
    

    

clsmems = inspect.getmembers(sys.modules[__name__], inspect.isclass)
CLASSES = set()
for c in clsmems:
    CLASSES.add(c[0])

MEMBERS = set()
for obj in CLASSES:
    for func in dir(eval(obj)):
        MEMBERS.add(func)
