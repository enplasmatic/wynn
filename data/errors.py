class Error:
    def Syntax(msg):
        raise SyntaxError(msg)
    
    def Type(msg):
        raise TypeError(msg)