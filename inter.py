import types
from std import *
from build import *
from termcolor import colored
from collections import deque

FUNCS = {
    println, scanf, scanb, scanln, ioconnect, system, iostream, # stdi/o bound
    fstream, # file bound
    fmt, sizeof, maxof, minof, TERNARY_OPERATOR, vars, type, hashed, # misc
    Alog, Bound, Integer, Rand, Container, String, Time, # classes
    Gradbit, GradbitGroup, GradbitMouse, GradbitSprite, Timer, # gradbits
    array, vector, queue, heap, set, sset, multiset, hashmap, multimap, pair, couple, # containers
}

TYPERS = set()
for f in FUNCS:
    if not isinstance(f, types.FunctionType):
        TYPERS.add(f)
TYPERS.remove(vars)
ops = ["+=", "-=", "*=", "/=", "//=", ">>=", "&=", "|=", "<<=", "%="]

DFDP = {}
for f in FUNCS:
    DFDP[str(f.__name__)] = f
DFDP["__builtins__"] = {'__build_class__': __build_class__, '__name__': __name__}
PTRS = {}
FUNCTIONS = {}
ForLoopIndents = set()
conditionIndented = {}


def remove_indent(ln:str, ind):
    lb = 0
    for i in range(ind):
        if ln[i] == ' ':
            lb+=1
    return ln[lb:]
CONSTANTS = set()

def SuitsChar(x:str):
    return ((x.isalnum()) or (x == "_"))

def findvars(x: str):
    VARS = eval('vars()')
    avars = list(VARS.items())
    avars.sort(key = get_len, reverse=True)
    splitted = x
    for var in avars:
        splitted=forvar(splitted,x,var)

def ignreplace(splitted:str, x:str, var, backwards = False):
    inString = False
    # for i, value in enumerate(splitted):
    i = 0
    while i < len(splitted):
        value = splitted[i]
        replaced = False
        # splitted += value
        # prxnt(i, splitted[0:i+1], var, splitted[0:i+1].endswith(var[0]))
        
        if not inString:
            if value in ["'", '"', "#"]:
                if x[min(0, i-1)] != '\\':
                    inString = True
                    delimiter = value
            txts = splitted[0:i+1]
        if backwards:
            co = inString
        else:
            co = not inString
        if co:
            if txts.endswith(var[0]):
                    if i+1==len(splitted): 
                        # This is a right edge.
                        replaced = True
                        splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1))
                    elif txts == var[0]:
                        # This is a left edge.
                        lefr = splitted[i+1:]
                        replaced = True
                        splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1)) + lefr
                    else: 
                        # This is a middle char.
                        lefr = splitted[i+1:]
                        replaced = True
                        splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1)) + lefr
        if inString:
            if value == delimiter:
                inString = False
        if not replaced:
            i+=1
        else: 
            i -= len(var[0])-1
    return splitted

def forvar(splitted:str, x:str, var):
    inString = False
    # for i, value in enumerate(splitted):
    i = 0
    
    while i < len(splitted):
        value = splitted[i]
        replaced = False
        # splitted += value
        # prxnt(i, splitted[0:i+1], var, splitted[0:i+1].endswith(var[0]))
        
        if not inString:
            if value in ["'", '"', "#"]:
                if x[min(0, i-1)] != '\\':
                    inString = True
                    delimiter = value
            txts = splitted[0:i+1]
            if txts.endswith(var[0]):
                    if i+1==len(splitted): 
                        # This is a right edge.
                        li = (i-len(var[0]))
                        if not SuitsChar(splitted[li]):
                            replaced = True
                            splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1))
                    elif txts == var[0]:
                        # This is a left edge.
                        ri = (i+1)
                        if not SuitsChar(splitted[ri]):
                            lefr = splitted[i+1:]
                            replaced = True
                            splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1)) + lefr
                    else: 
                        # This is a middle char.
                        li = (i-len(var[0]))
                        ri = (i+1)
                        if (not SuitsChar(splitted[li])) and (not SuitsChar(splitted[ri])):
                            replaced = True
                            lefr = splitted[i+1:]
                            splitted = str(var[1]).join(splitted[0:i+1].rsplit(var[0], 1)) + lefr
        else:
            if value == delimiter:
                inString = False
        if not replaced:
            i+=1
        else: 
            i -= len(var[0])-1
    return splitted

def do_reps(line):
    line = ignreplace(line, line, ['?(', 'TERNARY_OPERATOR('])
    line = ignreplace(line, line, ("\n","\\n"), True)
    return line

def tryln(line):
    line = do_reps(line)
    return eval(line, DFDP)

def runln(line):
    line = do_reps(line)
    compiled_code = compile(line, '<string>', 'exec')
    exec(compiled_code, DFDP)

def isImm(fullname):
    fullname = fullname.strip()
    # name = ""
    # i = 0
    # while SuitsChar(fullname[i]):
    #     name += fullname[i]
    #     i += 1
    #     if i <= len(fullname): 
    #         break
    # print(CONSTANTS, name, ">")
    if fullname in CONSTANTS:
        raise ReferenceError(f"Cannot change value of read-only variable '{fullname}'")

lastSwitch = []

def checkGroup(line:str):
    grouping = (int, str, bool, float, tuple)
    if line.startswith("derive"):
        line = line.replace("derive", "", 1).strip()
        grouping = (int, str, bool, float, tuple, *TYPERS)
    return grouping, line

def readln(line: str, index: int, code):
    global conditionIndented, ForLoopIndents, FUNCTIONS
    indent = indentlvl(line)
    line = line.strip()
    inc = index+1

    if line.startswith("new "):
        # define a variable
        line = line.replace("new", "", 1).strip()
        # imm = var is immutable
        if line.startswith("imm"):
            line = line.replace("imm", "", 1).strip()
            grouping, line = checkGroup(line)
            stuff = line.split("=", 1) # get name and value
            name, value = stuff[0], stuff[1]
            isImm(name)
            
            lmao = tryln(value)
            if isinstance(lmao, grouping):
                if isinstance(lmao, str):
                    lmao = '"'+lmao+'"'
            else:
                raise TypeError("Inappropriate argument type given to initialize variable")
            CONSTANTS.add(name.strip())
            runln(f"{name.strip()} = {lmao}")
        elif line.startswith("expansion"):
            line = line.replace("expansion", "", 1).strip()
            stuff = line.split("=", 1) # get name and value
            name, value = stuff[0].strip(), stuff[1].strip()
            ninety = value.split("(")
            if ninety[1][-1]!=")":
                raise SyntaxError("Invalid expansion call")
            name2 = ninety[0]
            args = ninety[1][:-1]
            if name2 in EXPANDERS:
                value = EXPANDERS[name2]["content"]
                if args != "":
                    arguments = args.split(",")
                    for i, arg in enumerate(arguments):
                        arg = arg.strip()
                        value = ignreplace(value, value, (EXPANDERS[name2]["args"][i].strip(), arg))
                runln(f"{name.strip()} = {tryln(value)}")
            else:
                raise NameError(f"Undefined expansion {name2}")
        

        elif line.startswith('<'):
            tokens = line.split(' ')
            if tokens[0].endswith('>'):
                classed = tokens[0][1:-1]
                shouldUnpack = False
                if (classed.endswith("!")):
                    shouldUnpack = True
                    classed = classed[:-1]
                line = " ".join(tokens[1:])
                stuff = line.split("=", 1) # get name and value
                name, value = stuff[0], stuff[1]
                if (not shouldUnpack) and ("," in name.strip()): raise SyntaxError(f"unpack operator required to unpack {name.strip()}.\n             Use 'new <{classed}!> {name}={value}' instead. (add the ! next to the container type)")

                isImm(name.strip())
                runln(f"{name.strip()} = {classed}({tryln(value)})")
            else:
                raise SyntaxError("container initialization requires angle brackets on both sides of type, such as 'new <set> vals = ...'")
        else:
            for op in ops:
                if op in line:
                    grouping, line = checkGroup(line)
                    stuff = line.split(op, 1) # get name and value
                    name, value = stuff[0], stuff[1]
                    isImm(name.strip())
                    lmao = tryln(value)
                    if isinstance(lmao, grouping):
                        if isinstance(lmao, str):
                            lmao = '"'+lmao+'"'
                        runln(f"{name.strip()} = ({name.strip()}) {op[:-1]} ({lmao})")
                    else:
                        raise TypeError("Inappropriate argument type given to initialize variable")
                    break
            else:
                grouping, line = checkGroup(line)
                stuff = line.split("=", 1) # get name and value
                name, value = stuff[0], stuff[1]
                isImm(name.strip())
                lmao = tryln(value)
                if isinstance(lmao, grouping):
                    if isinstance(lmao, str):
                        lmao = '"'+lmao+'"'
                    runln(f"{name.strip()} = {lmao}")
                else:
                    raise TypeError("Inappropriate argument type given to initialize variable")


    elif line.startswith("ptr "):
        line = line.replace("ptr", "", 1).strip()
        inc = int(line)

    elif line.startswith("enter "):
        line = line.replace("enter", "", 1).strip()
        inc = int(PTRS[(line)][0])

    elif line.startswith("struct "):
        line = line.replace("struct", "", 1).strip()
        if ("{" in line) and (line.endswith("}")):
            stuff = line.split("{", 1)
            className = stuff[0]
            args = "".join(stuff[1])[:-1]
            spaces = " "*indent
            pypycode = []
            splitargs = args.split(",")
            allVals = len(splitargs)
            pypycode.append(spaces+f"class {className}:")
            pypycode.append(spaces+f"    def __init__(self, listOfArgs):")
            pypycode.append(spaces+f"          self._VALUES = [None]*{allVals}")
            pypycode.append(spaces+f"          if sizeof(listOfArgs) == {allVals}: self._VALUES = listOfArgs")
            
            for j, arg in enumerate(splitargs):
                arg = arg.strip()
                if arg != "":
                    if arg.startswith("new"):
                            arg = arg.replace("new", "", 1).strip()
                            pypycode.append(spaces+f"          self.{arg} = self._VALUES[{j}]")
                    else: raise SyntaxError("use [new] keyword to assign variable")
            runln("\n".join(pypycode))

        else: raise SyntaxError("struct initialization requires curly brackets {new a, new b... new z} next to name")
        
    elif line.startswith("enum "):
        line = line.replace("enum", "", 1).strip()
        if ("{" in line) and (line.endswith("}")):
            stuff = line.split("{", 1)
            className = stuff[0]
            args = "".join(stuff[1])[:-1]
            spaces = " "*indent
            pypycode = []
            pypycode.append(spaces+f"class ENUM_named_{className}:")
            pypycode.append(spaces+f"    def __init__(self, nothing):")
            first = 0
            for usize, argument in enumerate(args.split(",")):
                argument = argument.strip()
                if argument != "":
                        j = usize+first
                        value = str(j)
                        if "=" in argument:
                            stuffagain = argument.split("=")
                            arg = stuffagain[0].strip()
                            value = stuffagain[1].strip()
                            if not isinstance(tryln(value), int): raise TypeError("enum must only contain integer types")
                            if first == 0:
                                first = int(value)
                            
                        else:
                            arg = argument
                        pypycode.append(spaces+f"          self.{arg} = {tryln(value)}")
            pypycode.append(spaces+f"{className} = ENUM_named_{className}(0)")
            coden = "\n".join(pypycode)
            runln(coden)

        else: raise SyntaxError("enum initialization requires curly brackets {a, new b... new z} next to name")
        
    elif line.startswith("break"):
        # break out of a loop
        line = line.replace("break", "", 1).strip()
        # if not (line.startswith('[') and line.endswith(']')):
        #     lvl = 2
        # else:
        #     lvl = int(line[1:-1])
        ptr = index+1
        while ptr < len(code):
            if (" "*indent) > (" "*indentlvl(code[ptr])):
                # might be buggy, god knows
                if indentlvl(code[ptr]) in ForLoopIndents:
                    break
            ptr+=1 
        inc = ptr

    elif line.startswith("if "):
        line = line.replace("if", "", 1).strip()
        cond = tryln(line)
        conditionIndented[indent] = cond
        if not cond:
            ptr = index+1
            while ptr < len(code):
                if (" "*indent) >= (" "*indentlvl(code[ptr])):
                    break
                ptr+=1 
            inc = ptr

    # elif line.startswith("return "):
    #     line = line.replace("return", "", 1).strip()
    #     return [tryln(line)]
    
    elif line.startswith("macro "):
        ptr = index+1
        while indentlvl(code[ptr]) > indent:
            ptr+=1
        inc = ptr

    elif line.startswith("throw"):
        line = line.replace("throw", "", 1).strip()
        print(colored("\n\n -- internal error thrown --", "red", None, ["bold"]))
        println(fmt("Callback: ", tryln(line), '\n\n'))
        sys.exit(1)


    elif line.startswith("else if "):
        line = line.replace("else if", "", 1).strip()
        cond = (not conditionIndented[indent])
        if cond:
            cond = tryln(line)
            conditionIndented[indent] = cond
            ptr = index+1
            if not cond:
                ptr = index+1
                while ptr < len(code):
                    if (" "*indent) >= (" "*indentlvl(code[ptr])):
                        break
                    ptr+=1 
                inc = ptr
        else:
            ptr = index+1
            while ptr < len(code):
                if (" "*indent) >= (" "*indentlvl(code[ptr])):
                    break
                ptr+=1 
            inc = ptr

    elif line.startswith("else"):
        line = line.replace("else", "", 1).strip()
        cond = (not conditionIndented[indent])
        if not cond:
            ptr = index+1
            while ptr < len(code):
                if (" "*indent) >= (" "*indentlvl(code[ptr])):
                    break
                ptr+=1 
            inc = ptr

    elif line.startswith("//"):
        # comment
        pass

    elif line.startswith("call "):
        pass

    elif line.startswith("free "):
        line = line.replace("free", "", 1).strip()
        PTRS[(line)].popleft()        


    else:
        if not is_variable_assignment(line):       
            vs = tryln('vars()')
            for v in vs.copy():
                if line.startswith(v) and not SuitsChar(line[len(v)]):
                    runln(line.strip())
        else:
            raise SyntaxError("use [new] keyword to assign variable")

    return inc, code

def funcln(line: str, index: int, code):
    indent = indentlvl(line.rstrip())
    line = line.strip()
    inc = index+1
    
    if line.strip(" ") == "":
        return inc, code
    
    if line.startswith("expand "):
            line = line.replace("expand", "", 1).strip()
        # if line.startswith("mac "):
        #     line = line.replace("mac", "", 1).strip()
            rofl = line.split("->", 1)
            content = rofl[1].strip(); line = rofl[0].strip()
            stuff = line.split("(", 1)
            name = stuff[0]
            line = line.replace(name, "", 1).strip()
            if line.startswith('(') and line.endswith(")"):
                if line == "": args = []
                else:
                    line = line[1:-1]
                    args = stdsplit(line, ',')
            else:
                raise SyntaxError("Parenthesis must follow expansion defention")
            EXPANDERS[name] = {"args": args, "content": content}


        
    elif line.startswith("macro "):
        line = line.replace("macro", "", 1).strip()
        stuff = line.split("(", 1)
        name = stuff[0]
        line = line.replace(name, "", 1).strip()
        if line.startswith('(') and line.endswith(")"):
            if line == "": args = []
            else:
                line = line[1:-1]
                args = stdsplit(line, ',')
        else:
            raise SyntaxError("Parenthesis must follow macro defention")
        ptr = index+1
        content = []
        firstindent = indentlvl(code[ptr])
        while indentlvl(code[ptr]) > indent:
            content.append(remove_indent(code[ptr], firstindent))
            ptr+=1
        inc = ptr
        FUNCTIONS[name] = {"args": args, "content": content}

    elif line.startswith("call "):
        line = line.replace("call", "", 1).strip()
        stuff = line.split("(", 1)
        name = stuff[0]
        line = line.replace(name, "", 1).strip()
        if line.startswith('(') and line.endswith(")"):
            if line == "": args = []
            else:
                line = line[1:-1]
                args = stdsplit(line, ',')
            content = FUNCTIONS[name]["content"].copy()
            if args != ['']:
                length = len(FUNCTIONS[name]["args"])-1
                for i, arg in enumerate(reversed(FUNCTIONS[name]["args"])):
                    # result = tryln(args[i])
                    result = args[length-i]
                    # if isStr(args[i]):
                    #     result = '"' + result + '"'
                    content.insert(0, f"{arg.strip()} = {result}")      
            for c in reversed(content):
                code.insert(index+1, (" "*indent)+c)
        else:
            raise SyntaxError("Parenthesis must follow function defention")
        
    
    return inc, code

runln("null=None")
firstIf = []
def preln(line: str, index: int, code):
    global conditionIndented, ForLoopIndents, lastSwitch, firstIf
    indent = indentlvl(line.rstrip())
    line = line.strip()
    
    if line.strip(" ") == "":
        return code
    
    # if line.startswith("loop"):
    #     code[index] = indent+"while True"

    elif line.startswith("while "):
        ForLoopIndents.add(indent)
        code[index] = code[index].replace("while", "if", 1)
        ptr = index+1
        newindex = indentlvl(code[ptr])
        while ptr < len(code):
            if (" "*indent) >= (" "*indentlvl(code[ptr])):
                code.insert(ptr, f"{" "*newindex}ptr {index}")
                break
            ptr+=1 

    elif line.startswith("for"):
        ForLoopIndents.add(indent)
        line = line.replace("for", "", 1).strip()
        if not (line.startswith('(') and line.endswith(')')):
            raise SyntaxError("For loop requires parenthesis after 'for' keyword")
        stuff = ignsplit(line[1:-1], ",")
        start = stuff[0].strip()
        condition = stuff[1].strip()
        update = stuff[2].strip()
        
        code[index] = f"{" "*indent}if ({condition})"
        code.insert(index, f"{" "*indent}{start}")
        ptr = index+2
        newindex = indentlvl(code[ptr])
        while ptr < len(code):
            if (" "*indent) >= (" "*indentlvl(code[ptr])):
                code.insert(ptr, f"{" "*newindex}ptr {index+1}")
                code.insert(ptr, f"{" "*newindex}{update}")
                break
            ptr+=1 

    elif line.startswith("switch "):
        line = line.replace("switch", "", 1).strip()
        lastSwitch.append(f"({line})")
        firstIf.append(True)
        code[index] = (" "*indent)+"if True"

    elif line.startswith("case"):
        line = line.replace("case", "", 1).strip()
        values = stdsplit(line, ',')
        if firstIf[-1]:
            p = ""
        else:
            p = "else "
        code[index] = (" "*indent)+f"{p}if "
        lev = len(values)
        for q in range(lev):
            val = values[q].strip()
            if q == lev-1:
                code[index] += f"({lastSwitch[-1]} == ({val}))"
            else:
                code[index] += f"({lastSwitch[-1]} == ({val})) or "
        firstIf[-1] = False

    elif line.startswith("end"):
        line = line.replace("end", "", 1).strip()
        if line == "switch":
            firstIf.pop()
            lastSwitch.pop()
        code[index] = (" "*indent)+"voided"

    elif line.startswith("setat "):
        line = line.replace("setat", "", 1).strip()
        if line not in PTRS: PTRS[(line)] = deque()
        PTRS[(line)].append(index)

   

    return code
            
def initln(line, index, code):
    global conditionIndented, ForLoopIndents
    indent = indentlvl(line.rstrip())
    line = line.strip()

    if line.strip(" ") == "":
        return code
    
    
    elif line.startswith("include "):
        line = line.replace("include", "", 1).strip()
        if not isStr(line):
            raise SyntaxError("Include preprocessor requires quotes to direct to path")
        path = line[1:-1]
        file = open(path, "r").read()
        All = file.split("\n")
        for i, a in enumerate(All):
            if a.strip().strip(" ") == "":
                del All[i]
            else:
                All[i] = All[i].rstrip()
        file = stdsplit("".join(All), ';')
        del code[index]
        isStatic = False
        for ide, f in enumerate(file):
            concord = f.strip()
            if concord == "static":
                isStatic = True
            elif concord == "end static":
                isStatic = False
            if not isStatic:
                code.insert(index+ide, f)

    elif line.startswith("using "):
        line = line.replace("using", "", 1).strip()
        if "::" in line:
            stuff = line.split("::")
            old = stuff[1].strip(); new = stuff[0].strip()
            for i, _ in enumerate(code):
                if i <= index: continue
                code[i] = forvar(code[i], code[i], (new, old))
        else: raise SyntaxError("using keyword needs [NEW] :: [OLD] syntax")

    elif line.startswith("define "):
        line = line.replace("define", "", 1).strip()
        if "::" in line:
            stuff = line.split("::")
            old = stuff[1].strip(); new = stuff[0].strip()
            for i, _ in enumerate(code):
                code[i] = ignreplace(code[i], code[i], (new, old))
        else: raise SyntaxError("define keyword needs [NEW] :: [OLD] syntax")
    
    return code
EXPANDERS = {}
def pref(code):
    a = 0
    while a < len(code):
        code = preln(code[a],a,code)
        a+=1
    return code

def initf(code):
    a = 0
    while a < len(code):
        code = initln(code[a],a,code)
        a+=1
    return code

def readf(code):
    a = 0
    while a < len(code):
        a, code = readln(code[a],a,code)
        # if isinstance(a, list):
        #     return a[0]
    return None

def funcf(code):
    a = 0
    while a < len(code):
        a, code = funcln(code[a],a,code)
    return code
