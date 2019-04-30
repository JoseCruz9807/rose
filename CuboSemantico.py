
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
		('not',		'bool',		''	)	:	'bool'
		}

	def resultType(self, op1, op2, operator):
		#return self.semantica[op1,op2,operator]
		try:
			tipo = self.semantica[op1,op2,operator]
		except:
			#print("issue en el CuboSemantico")
			tipo ='error'
		return tipo
			