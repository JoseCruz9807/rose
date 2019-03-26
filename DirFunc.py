import sys

#Tabla de Directorio de Funciones
class DirFunc:
    class __DirFunc:
        def __init__(self,nombre,tipo):
            self.val = { nombre : (tipo, {}) }
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self,nombre,tipo):
        if not DirFunc.instance:
            DirFunc.instance = DirFunc.__DirFunc(nombre,tipo)
        else:
            addFunc(nombre,tipo)
    def __getattr__(self, table):
        return getattr(self.instance, table)

    def addFunc(self, nombre, tipo):
        """ Adjunta la funcion especificada al Directorio de Funciones 
            Args:
             nombre : Nombre de la funcion a aniadir.
             tipo   : Tipo de dato que le pertenece a la funcion.
        """
        if (nombre in DirFunc.instance.val):
            print('Function {} previously defined.'.format(nombre))
            sys.exit()
        else:
            DirFunc.instance.val[nombre] = (tipo, {} )

    def addVariable(self, nameFunc, variable, tipo, filas, columnas):
        """ Adjunta la variable a la funcion especificada 
            Args:
             nameFunc   : Nombre de la funcion a la que se le aniadiran las variables.
             variable   : Nombre de la variable a aniadir.
             tipo       : Tipo de dato que le pertenece a 'variable'.
             filas      : Cantidad de filas en la variable.
             columnas   : Cantidad de columnas en la variable.
        """
        if (variable in self.val[nameFunc][1]):
            print('Variable {} previously defined.'.format(variable))
            sys.exit()
        else:
            tableVars = self.val[nameFunc][1]  
            tableVars[variable] = (tipo, filas, columnas)
            self.val[nameFunc] =  (self.val[nameFunc][0], tableVars)
        
