from inter import *
Content = open('/Users/aaravs/Documents/Python/wynn/code.w', 'r').read()
All = Content.split("\n")
for i, a in enumerate(All):
    if a.strip().strip(" ") == "":
        del All[i]
    else:
        All[i] = All[i].rstrip()
Content = "".join(All)
Content = pref(pref(funcf(initf(stdsplit(Content, ";")))))
print(';\n'.join(Content))
result = readf(Content)