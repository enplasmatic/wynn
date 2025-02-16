import time

class Time:
    def get():
        return time.time()
    
    def curtime(tup):
        return time.asctime(tup)
    
    def zone():
        return time.timezone
    
    def pause_program(seconds: float):
        return time.sleep(seconds)
    
    def time():
        return time.asctime()
    
glx = 0
def hashed():
    global glx
    glx+=1
    return glx