import sys

#Tabla de Directorio de Funciones
class DirFunc:
    class __DirFunc:
        def __init__(self,nombre,tipo):
            self.val = { nombre : (tipo, {}, 0, 0) }
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

    def addFunc(self, nombre, tipo, quadCount):
        """ Adjunta la funcion especificada al Directorio de Funciones 
            Args:
             nombre : Nombre de la funcion a aniadir.
             tipo   : Tipo de dato que le pertenece a la funcion.
             quadCount : Cantidad de cuádruplos generados hasta el momento.
        """
        if (nombre in DirFunc.instance.val):
            print('Function {} previously defined.'.format(nombre))
            sys.exit()
        else:
            DirFunc.instance.val[nombre] = (tipo, {}, 0, quadCount)

    def addVariable(self, nameFunc, variable, tipo, filas, columnas, posMemory):
        """ Adjunta la variable a la funcion especificada 
            Args:
             nameFunc   : Nombre de la funcion a la que se le aniadiran las variables.
             variable   : Nombre de la variable a aniadir.
             tipo       : Tipo de dato que le pertenece a 'variable'.
             filas      : Cantidad de filas en la variable.
             columnas   : Cantidad de columnas en la variable.
             posMemory  : Indice que apunta a la posicion de memoria en la que se encuentra.
        """
        if (variable in self.val[nameFunc][1]):
            print('Variable {} previously defined.'.format(variable))
            sys.exit()
        else:
            tableVars = self.val[nameFunc][1]  
            tableVars[variable] = (tipo, filas, columnas, posMemory)
            self.val[nameFunc] =  (self.val[nameFunc][0], tableVars, self.val[nameFunc][2], self.val[nameFunc][3])

    def updateParams(self, nombre, numPar):
        """
        Actualiza la cantidad de parametros en la funcion
        Args:   
         nombre: Nombre de la funcion a modificar
         numPar: Cantidad de parametros de la funcion a modificar
        """
        self.val[nombre] = (self.val[nombre][0], self.val[nombre][1], numPar, self.val[nombre][3])

    def getVarType(self, scope, nombre):
        """
        Regresa el tipo de la variable solicitada.
        Args:
         scope: Función donde se busca la variable deseada
         nombre: Nombre de la variable que se desea saber el tipo 
        """
        try:
            tableVars = self.val[scope][1]
            varType = tableVars[nombre][0]
        except:
            tableVars = self.val['globals'][1]
            varType = tableVars[nombre][0]            
        return varType

    def getVarName(self, scope, memAdd):
        """
        Regresa el nombre de la variable solicitada.
        Args:
         scope: Función donde se busca la variable deseada
         memAdd: Posición de memoria que tiene la variable 
        """
        nameVar = 'none'
        tableVars = self.val[scope][1]
        for var in tableVars:
            if tableVars[var][3] == memAdd:
                nameVarTemp = var
        try:
            nameVar = nameVarTemp
        except:
            tableVars = self.val['globals'][1]
            for var in tableVars:
                if tableVars[var][3] == memAdd:
                    nameVar = var
        return nameVar


    def getVarMemPos(self, scope, nombre):
        """
        Regresa el valor de memoria que le fue asignado.
        Args:
         scope: Función donde se busca la variable deseada
         nombre: Nombre de la variable que se desea saber el valor de memoria que le fue asignado 
        """
        try:
            tableVars = self.val[scope][1]
            numMemPos = tableVars[nombre][3]
        except:
            tableVars = self.val['globals'][1]
            numMemPos = tableVars[nombre][3] 
        return numMemPos

    def getFilasVar(self, scope, nombre):
        """
        Regresa el tipo de la variable solicitada.
        Args:
         scope: Función donde se busca la variable deseada
         nombre: Nombre de la variable que se desea saber el tipo 
        """
        try:
            tableVars = self.val[scope][1]
            numFilas = tableVars[nombre][1]
        except:
            tableVars = self.val['globals'][1]
            numFilas = tableVars[nombre][1]
        return numFilas

    def getColumnasVar(self, scope, nombre):
        """
        Regresa el tipo de la variable solicitada.
        Args:
         scope: Función donde se busca la variable deseada
         nombre: Nombre de la variable que se desea saber el tipo 
        """
        try:
            tableVars = self.val[scope][1]
            numColumnas = tableVars[nombre][2]
        except:
            tableVars = self.val['globals'][1]
            numColumnas = tableVars[nombre][2]
        return numColumnas

    def getFuncType (self, scope):
        """
        Regresa el tipo de la funcion solicitada.
        Args:
         scope: Función que se busca
        """
        return self.val[scope][0]