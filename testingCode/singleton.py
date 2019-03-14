from DirFunc import *

class Vars:
    # class __Vars:
    #     def __init__(self,key,value):
    #         self.val = {key: value}
    #     def __str__(self):
    #         return repr(self)
    # instance = None
    def __init__(self, key, value):
        if not Vars.instance:
            Vars.instance = Vars.__Vars(key,value)
        else:
            Vars.instance.val[key] = value
    def __getattr__(self, table):
        return getattr(self.instance, table)



x = DirFunc('global', 'int', 'scope')
print(list(x.val))
y = DirFunc('func1', 'float', 'scope')
"""
y = DirFunc('dav', 1996)
print(list(y.val))
z = DirFunc('rom', 1978)
print(list(z.val))
w = DirFunc('fer', 1998)
print(list(w.val))
"""
print(x.val)
variables = {'fNum': ('float', 'scope'), 'fProb': ('float', 'scope')}
x.addVariables('global', variables)
#x.val['global'] = (x.val['global'][0], x.val['global'][1], {'fNum': ('float', 'scope')})
print(x.val)
print(x.val['global'][2])

variables2 = {'iNum': ('int', 'scope'), 'iProb': ('int', 'scope')}
x.addVariables('global', variables2)
print(x.val)
print(x.val['global'][2])



print(list(x.val))
#print(y.val)
#print(z.val)