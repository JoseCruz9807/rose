#Tabla de Directorio de Funciones
class DirFunc:
    class __DirFunc:
        
        #variables = Vars()
        variables = 0
        def __init__(self,nombre,tipo,scope):
            self.val = {
            "name"  : nombre,
            "tipo"  : tipo,
            "scope" : scope,
            "vars"  : variables
            }
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self,nombre,tipo,scope):
        if not DirFunc.instance:
            DirFunc.instance = DirFunc.__DirFunc(nombre,tipo,scope)
        else:
            DirFunc.instance.val = {
            "name"  : name,
            "tipo"  : tipo,
            "scope" : scope,
            "vars"  : variables
            }
    def __getattr__(self, table):
        return getattr(self.instance, table)

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



x = DirFunc('global', 1996)
print(list(x.val))
y = DirFunc('dav', 1996)
print(list(y.val))
z = DirFunc('rom', 1978)
print(list(z.val))
w = DirFunc('fer', 1998)
print(list(x.val))
print(x.val)
print(y.val)
print(z.val)