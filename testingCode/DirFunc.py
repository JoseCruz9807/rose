#Tabla de Directorio de Funciones
class DirFunc:
    class __DirFunc:
        def __init__(self,nombre,tipo,scope):
            self.val = { nombre : (tipo, scope, {}) }
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self,nombre,tipo,scope):
        if not DirFunc.instance:
            DirFunc.instance = DirFunc.__DirFunc(nombre,tipo,scope)
        else:
            DirFunc.instance.val[nombre] = (tipo, scope, {} )
    def __getattr__(self, table):
        return getattr(self.instance, table)

    def addVariables(self, nameFunc, variables):
        """ Adjunta las variables a la función especificada 
            Args:
             nameFunc   : Nombre de la función a la que se le añadirán las variables.
                            Tiene que estar en formato 'nameFunc'
             variables  : Dictionary que contiene todas las variables encontradas.
                            Tiene que estar en formato { nombreVariable1 : (tipoDeDato1, Scope1), nombreVariable2 : (tipoDeDato2, Scope2) ...}
        """
        self.val[nameFunc] =  (self.val[nameFunc][0], self.val[nameFunc][1], variables)
        #print('addVariables: ')
        #print(self.val)
        #return self