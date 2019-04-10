import sys
#Tabla de Directorio de Funciones
class ParameterTable:
    class __ParameterTable:
        def __init__(self,nombre,tipo):
            self.val = { nombre : (tipo, {}) }
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self,nombre,tipo):
        if not ParameterTable.instance:
            ParameterTable.instance = ParameterTable.__ParameterTable(nombre,tipo)
        else:
            addFunc(nombre,tipo)
    def __getattr__(self, table):
        return getattr(self.instance, table)

        
