import codeop

def ignin(x: str, target):
    splitted = ""
    inString = False

    for i, value in enumerate(x):
        splitted += value

        if not inString:
            if value in ["'", '"', "#"]:
                if x[min(0, i-1)] != '\\':
                    inString = True
                    delimiter = value

            if splitted.endswith(target):
                    return True

        else:
            if value == delimiter:
                inString = False

    return False       

def is_variable_assignment(code):
    try:
        compiled = codeop.compile_command(code, "<string>", "exec")
        return compiled and compiled.co_names == ()  # Assignments have no function calls
    except SyntaxError:
        return False  # Invalid code is not an assignment
    
def get_len(key):
    return len(key[0])


def indentlvl(a: str):
    return (len(a) - len(a.lstrip(' ')))

def ignsplit(x: str, splitval: str):
    splitted = [""]
    inString = False
    delimiter = None
    for i, value in enumerate(x):
        if not inString:
            if value in ["'", '"', "#"]:
                if x[min(0, i-1)] != '\\':
                    inString = True
                    delimiter = value
            if value == splitval:
                splitted.append("")
            else:
                splitted[-1]+=(value)
        
        else:
            splitted[-1]+=(value)
            if value == delimiter and value != "#":
                inString = False


    return splitted     

def isStr(x: str):
    return ((x.startswith('"') and x.endswith('"')) or (x.startswith("'") and x.endswith("'")))   

def stdsplit(x: str, splitval: str):
    splitted = [""]
    inString = False
    delimiter = None
    TEN = {"'":"'", '"':'"', "#": "#", "(": ")", "[": "]", "{": "}"}
    for i, value in enumerate(x):
        if not inString:
            if value in TEN:
                if x[min(0, i-1)] != '\\':
                    inString = True
                    delimiter = value
            if value == splitval:
                splitted.append("")
            else:
                splitted[-1]+=(value)
        
        else:
            splitted[-1]+=(value)
            if value == TEN[delimiter] and value != "#":
                inString = False


    return splitted     

def is_variable_assignment(code):
    try:
        compiled = codeop.compile_command(code, "<string>", "exec")
        return compiled and compiled.co_names == ()  # Assignments have no function calls
    except SyntaxError:
        return False  # Invalid code is not an assignment

import codeop
import dis

def is_variable_assignment(code):
    try:
        compiled = codeop.compile_command(code, "<string>", "exec")
        if not compiled:
            return False  # If code is incomplete or invalid

        # Disassemble and check if assignment (`STORE_NAME`, `STORE_FAST`, etc.) exists
        bytecode = dis.Bytecode(compiled)
        return any(instr.opname.startswith("STORE") for instr in bytecode)

    except SyntaxError:
        return False  # Invalid code is not an assignment
    
