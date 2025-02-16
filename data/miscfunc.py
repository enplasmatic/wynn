def flatten(xss):
    return [x for xs in xss for x in xs]
def sizeof(obj):
    return len(obj)
def minof(*obj):
    return min(flatten(obj))
def maxof(*obj):
    return max(flatten(obj))
