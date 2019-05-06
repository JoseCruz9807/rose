
#Cubo semantico
class CuboSemantico:
	def __init__(self):
		self.semantica = {
		#op1		#op2		#operator	#result
		('int',		'int',		'='		)	:'int'		,
		('int',		'int',		'=*'	)	:'int'		,
		('int',		'int',		'+'		)	:'int'		,
		('int',		'int',		'-'		)	:'int'		,
		('int',		'int',		'*'		)	:'int'		,
		('int',		'int',		'/'		)	:'float'	,
		('int',		'int',		'AND'	)	:'bool'		,
		('int',		'int',		'OR'	)	:'bool'		,
		('int',		'int',		'<'		)	:'bool'		,
		('int',		'int',		'<='	)	:'bool'		,
		('int',		'int',		'>'		)	:'bool'		,
		('int',		'int',		'>='	)	:'bool'		,
		('int',		'int',		'=='	)	:'bool'		,
		('int',		'int',		'!='	)	:'bool'		,
		('int',		'float',	'+',	)	:'float'	,
		('int',		'float',	'-',	)	:'float'	,
		('int',		'float',	'*',	)	:'float'	,
		('int',		'float',	'/',	)	:'float'	,
		('int',		'float',	'AND'	)	:'bool'		,
		('int',		'float',	'OR'	)	:'bool'		,
		('int',		'float',	'<'		)	:'bool'		,
		('int',		'float',	'<='	)	:'bool'		,
		('int',		'float',	'>'		)	:'bool'		,
		('int',		'float',	'>='	)	:'bool'		,
		('int',		'float',	'=='	)	:'bool'		,
		('int',		'float',	'!='	)	:'bool'		,

		('float',	'int',		'='		)	:'float'		,
		('float',	'int',		'=*'	)	:'float'		,
		('float',	'int',		'+'		)	:'float'		,
		('float',	'int',		'-'		)	:'float'		,
		('float',	'int',		'*'		)	:'float'		,
		('float',	'int',		'/'		)	:'float'	,
		('float',	'int',		'AND'	)	:'bool'		,
		('float',	'int',		'OR'	)	:'bool'		,
		('float',	'int',		'<'		)	:'bool'		,
		('float',	'int',		'<='	)	:'bool'		,
		('float',	'int',		'>'		)	:'bool'		,
		('float',	'int',		'>='	)	:'bool'		,
		('float',	'int',		'=='	)	:'bool'		,
		('float',	'int',		'!='	)	:'bool'		,
		('float',	'float',	'=',	)	:'float'	,
		('float',	'float',	'+',	)	:'float'	,
		('float',	'float',	'-',	)	:'float'	,
		('float',	'float',	'*',	)	:'float'	,
		('float',	'float',	'/',	)	:'float'	,
		('float',	'float',	'AND'	)	:'bool'		,
		('float',	'float',	'OR'	)	:'bool'		,
		('float',	'float',	'<'		)	:'bool'		,
		('float',	'float',	'<='	)	:'bool'		,
		('float',	'float',	'>'		)	:'bool'		,
		('float',	'float',	'>='	)	:'bool'		,
		('float',	'float',	'=='	)	:'bool'		,
		('float',	'float',	'=*'	)	:'float'	,
		
		('string',	'string',	'+',	)	:'string'	,
		('string',	'string',	'='		)	:'string'	,
		('string',	'string',	'=*'	)	:'string'	,
		('string',	'string',	'=='	)	:'bool'	,
		
		('bool',	'bool',		'='		)	:'bool'	,
		('bool',	'bool',		'=*'	)	:'bool'	,
		('bool',	'bool',		'!='	)	:'bool'	,
		('bool',	'bool',		'AND'	)	:'bool'	,
		('bool',	'bool',		'OR'	)	:'bool'	,
		('bool',	'bool',		'=='	)	:'bool'	,
		('bool',	'string',	'+'		)	:'error',


		('print',	'string',	''	)	:	'string',
		('print',	'bool',		''	)	:	'string',
		('print',	'int',		''	)	:	'string',
		('print',	'float',	''	)	:	'string',	
		
		('read',	'string',	''	)	:	'string',
		('read',	'bool',		''	)	:	'bool',
		('read',	'int',		''	)	:	'int',
		('read',	'float',	''	)	:	'float',
		
		('read*',	'string',	''	)	:	'string',
		('read*',	'bool',		''	)	:	'bool',
		('read*',	'int',		''	)	:	'int',
		('read*',	'float',	''	)	:	'float',
		

		('not',		'bool',		''	)	:	'bool',
		('sqrt', 	'float',	''	)	:	'float',
		('sqrt',	'int',		''	)	:	'float',

		('pow',		'int',		'int')	:	'float',
		('pow',		'int',		'float'):	'float',
		('pow',		'float',	'int')	:	'float',
		('pow',		'float',	'float'):	'float',

		('abs',		'int',		''	)	:	'int',
		('abs',		'float',	'' )	:	'float',

		('sin',		'int',		'')		:	'float',
		('sin'		'float',	'')		:	'float',
		('cos',		'int',		'')		:	'float',
		('cos',		'float',	'')		:	'float',
		('factorial','int',		'')		:	'int',

		('stdev',	'int',		'')		:	'float',
		('stdev',	'float',	'')		:	'float',

		('mean',	'int',		'')		:	'float',
		('mean',	'float',	'')		:	'float',

		('median',	'float',	'')		:	'float',
		('median',	'int',		'')		:	'float',

		('mode',	'int',		'')		:	'int',
		('mode'		'float',	'')		:	'float',
		('mode',	'string',	'')		:	'string',

		('sort',	'int',		'')		:	'int',
		('sort',	'float',	'')		:	'float',
		('sort',	'string',	'')		:	'string',

		('exportCSV','string',	'string'):	'bool',
		('exportCSV','string',	'int')	:	'bool',
		('exportCSV','string',	'float'):	'bool',
		('exportCSV','string',	'bool')	:	'bool',

		('lineChart','int',		'int')	:	'bool',
		('lineChart','float',	'float'):	'bool',
		('lineChart','float',	'int')	:	'bool',
		('lineChart','int',		'float'):	'bool',

		('graph3d','int',		'int')	:	'graph3d2',
		('graph3d','float',	'float')	:	'graph3d2',
		('graph3d','float',	'int')		:	'graph3d2',
		('graph3d','int',		'float'):	'graph3d2',

		('graph3d2','int',		'int')	:	'bool',
		('graph3d2','float',	'float'):	'bool',
		('graph3d2','float',	'int')	:	'bool',
		('graph3d2','int',		'float'):	'bool',

		('pieChart','string',	'int')	:	'bool',
		('pieChart','string',	'float'):	'bool',

		('histogramChart','int','int')	:	'bool',
		('histogramChart','float','int'):	'bool',
		
		('barChart','string',	'float'):	'bool',
		('barChart','string',	'int')	:	'bool',

		('transpose','int',		'')		:	'bool',
		('transpose','float',		'')	:	'bool',
		('transpose','bool',		'')	:	'bool',
		('transpose','string',		'')	:	'bool',

		('linreg','int',		'int')	:	'linreg2',
		('linreg','float',	'float')	:	'linreg2',
		('linreg','int',	'float')	:	'linreg2',
		('linreg','float',	'int')		:	'linreg2',

		('linreg2','int',	'')			:	'float',

		}

	def resultType(self, op1, op2, operator):
		""" Busca en el diccionario de valores el tipo de valor que la operación debe regresar.
			Args:
			 op1: Primer Operando.
			 op2: Segundo Operando.
			 operator: Operador que se está ejecutando.
		 """
		#return self.semantica[op1,op2,operator]
		try:
			tipo = self.semantica[op1,op2,operator]
		except:
			tipo ='error'
		return tipo
			