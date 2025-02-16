import random

class Rand:
    def rand():
        return random.random()
    
    def randint(lo,hi):
        return random.randint(lo, hi)
    
    def randlong(lo, hi, step):
        return random.randrange(lo, hi, step)
    
    def choose(array):
        return random.choice(array)
    
    def randomize(arrays):
        random.shuffle(arrays)
        return arrays
    
    def seed(a, v):
        return random.seed(a, v)