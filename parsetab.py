
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS AND APPEND ARRANGE BARCHART BOOL COLON COMMA COMMENT COS CTEF CTEI CTES DIFFERENT DIVIDE ELSE EQUALS EQUIVALENTE EXPORTCSV FACTORIAL FALSE FLOAT FUNCTION GLOBALS GRAPH GRAPH3D GT GTEQ HISTOGRAMCHART ID IF INT LEFTBRACKET LEFTPARENTHESIS LINECHART LINREG LT LTEQ MAIN MEAN MEDIAN MINUS MODE MULTICOMCL MULTICOMOP MULTIPLY NOT OR PERIOD PIECHART PLUS POW PRINT PROGRAM QUOTE READ RETURN RIGHTBRACKET RIGHTPARENTHESIS SEMICOLON SIN SORT SQRT STDEV STRING TAN TRANSPOSE TRUE VAR WHILE\n    rose : PROGRAM ID SEMICOLON vars bloque\n            | PROGRAM ID SEMICOLON bloque\n    \n    bloque : LEFTBRACKET b RIGHTBRACKET\n    \n    b : estatuto b\n        | empty\n    \n    estatuto : asignacion\n            | condicion\n            | escritura\n    \n    vars : GLOBALS c\n    \n    c : ID COMMA c\n        | ID COLON tipo SEMICOLON c\n        | ID COLON tipo SEMICOLON\n    \n    tipo : INT \n        | FLOAT\n    \n    asignacion : ID EQUALS expresion SEMICOLON\n    \n    escritura : PRINT LEFTPARENTHESIS e RIGHTPARENTHESIS SEMICOLON\n    \n    e : expresion PERIOD e\n        | CTES PERIOD e\n        | CTES\n        | expresion\n        | empty\n    \n    expresion : exp GT exp\n                | exp LT exp\n                | exp DIFFERENT exp\n                | exp\n    \n    exp : termino g\n    \n    g : PLUS termino g\n        | MINUS termino g\n        | empty\n    \n    condicion : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque h SEMICOLON\n    \n    h : ELSE bloque \n        | empty\n    \n    termino : factor i\n            | factor\n    \n    i : MULTIPLY factor i\n        | DIVIDE factor i\n        | MULTIPLY factor\n        | DIVIDE factor\n    \n    factor : LEFTPARENTHESIS expresion RIGHTPARENTHESIS\n            | PLUS varcte\n            | MINUS varcte\n            | varcte\n    \n    varcte : ID\n            | CTEI\n            | CTEF\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,6,9,23,],[0,-2,-1,-3,]),'ID':([2,7,8,13,15,16,17,21,25,26,27,37,38,40,48,49,50,51,52,54,55,58,59,65,66,77,87,],[3,11,18,18,-6,-7,-8,11,32,32,32,32,32,32,11,-15,32,32,32,32,32,32,32,32,32,-16,-30,]),'SEMICOLON':([3,23,29,30,31,32,33,34,35,36,39,41,42,53,56,57,61,62,64,68,69,70,71,72,73,74,75,76,80,81,82,83,84,86,88,],[4,-3,48,-13,-14,-43,49,-25,-46,-34,-42,-44,-45,-26,-29,-33,-40,-41,77,-22,-23,-24,-46,-46,-37,-38,-39,-46,-27,-28,-35,-36,87,-32,-31,]),'GLOBALS':([4,],[7,]),'LEFTBRACKET':([4,5,10,28,48,63,67,85,],[8,8,-9,-10,-12,8,-11,8,]),'RIGHTBRACKET':([8,12,13,14,15,16,17,24,49,77,87,],[-46,23,-46,-5,-6,-7,-8,-4,-15,-16,-30,]),'IF':([8,13,15,16,17,49,77,87,],[19,19,-6,-7,-8,-15,-16,-30,]),'PRINT':([8,13,15,16,17,49,77,87,],[20,20,-6,-7,-8,-15,-16,-30,]),'COMMA':([11,],[21,]),'COLON':([11,],[22,]),'EQUALS':([18,],[25,]),'LEFTPARENTHESIS':([19,20,25,26,27,37,50,51,52,54,55,58,59,65,66,],[26,27,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'INT':([22,],[30,]),'FLOAT':([22,],[31,]),'ELSE':([23,76,],[-3,85,]),'PLUS':([25,26,27,32,35,36,37,39,41,42,50,51,52,54,55,57,58,59,61,62,65,66,71,72,73,74,75,82,83,],[38,38,38,-43,54,-34,38,-42,-44,-45,38,38,38,38,38,-33,38,38,-40,-41,38,38,54,54,-37,-38,-39,-35,-36,]),'MINUS':([25,26,27,32,35,36,37,39,41,42,50,51,52,54,55,57,58,59,61,62,65,66,71,72,73,74,75,82,83,],[40,40,40,-43,55,-34,40,-42,-44,-45,40,40,40,40,40,-33,40,40,-40,-41,40,40,55,55,-37,-38,-39,-35,-36,]),'CTEI':([25,26,27,37,38,40,50,51,52,54,55,58,59,65,66,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'CTEF':([25,26,27,37,38,40,50,51,52,54,55,58,59,65,66,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'CTES':([27,65,66,],[46,46,46,]),'RIGHTPARENTHESIS':([27,32,34,35,36,39,41,42,43,44,45,46,47,53,56,57,60,61,62,65,66,68,69,70,71,72,73,74,75,78,79,80,81,82,83,],[-46,-43,-25,-46,-34,-42,-44,-45,63,64,-20,-19,-21,-26,-29,-33,75,-40,-41,-46,-46,-22,-23,-24,-46,-46,-37,-38,-39,-17,-18,-27,-28,-35,-36,]),'MULTIPLY':([32,36,39,41,42,61,62,73,74,75,],[-43,58,-42,-44,-45,-40,-41,58,58,-39,]),'DIVIDE':([32,36,39,41,42,61,62,73,74,75,],[-43,59,-42,-44,-45,-40,-41,59,59,-39,]),'GT':([32,34,35,36,39,41,42,53,56,57,61,62,71,72,73,74,75,80,81,82,83,],[-43,50,-46,-34,-42,-44,-45,-26,-29,-33,-40,-41,-46,-46,-37,-38,-39,-27,-28,-35,-36,]),'LT':([32,34,35,36,39,41,42,53,56,57,61,62,71,72,73,74,75,80,81,82,83,],[-43,51,-46,-34,-42,-44,-45,-26,-29,-33,-40,-41,-46,-46,-37,-38,-39,-27,-28,-35,-36,]),'DIFFERENT':([32,34,35,36,39,41,42,53,56,57,61,62,71,72,73,74,75,80,81,82,83,],[-43,52,-46,-34,-42,-44,-45,-26,-29,-33,-40,-41,-46,-46,-37,-38,-39,-27,-28,-35,-36,]),'PERIOD':([32,34,35,36,39,41,42,45,46,53,56,57,61,62,68,69,70,71,72,73,74,75,80,81,82,83,],[-43,-25,-46,-34,-42,-44,-45,65,66,-26,-29,-33,-40,-41,-22,-23,-24,-46,-46,-37,-38,-39,-27,-28,-35,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rose':([0,],[1,]),'vars':([4,],[5,]),'bloque':([4,5,63,85,],[6,9,76,88,]),'c':([7,21,48,],[10,28,67,]),'b':([8,13,],[12,24,]),'estatuto':([8,13,],[13,13,]),'empty':([8,13,27,35,65,66,71,72,76,],[14,14,47,56,47,47,56,56,86,]),'asignacion':([8,13,],[15,15,]),'condicion':([8,13,],[16,16,]),'escritura':([8,13,],[17,17,]),'tipo':([22,],[29,]),'expresion':([25,26,27,37,65,66,],[33,43,45,60,45,45,]),'exp':([25,26,27,37,50,51,52,65,66,],[34,34,34,34,68,69,70,34,34,]),'termino':([25,26,27,37,50,51,52,54,55,65,66,],[35,35,35,35,35,35,35,71,72,35,35,]),'factor':([25,26,27,37,50,51,52,54,55,58,59,65,66,],[36,36,36,36,36,36,36,36,36,73,74,36,36,]),'varcte':([25,26,27,37,38,40,50,51,52,54,55,58,59,65,66,],[39,39,39,39,61,62,39,39,39,39,39,39,39,39,39,]),'e':([27,65,66,],[44,78,79,]),'g':([35,71,72,],[53,80,81,]),'i':([36,73,74,],[57,82,83,]),'h':([76,],[84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> rose","S'",1,None,None,None),
  ('rose -> PROGRAM ID SEMICOLON vars bloque','rose',5,'p_rose','rose.py',280),
  ('rose -> PROGRAM ID SEMICOLON bloque','rose',4,'p_rose','rose.py',281),
  ('bloque -> LEFTBRACKET b RIGHTBRACKET','bloque',3,'p_bloque','rose.py',288),
  ('b -> estatuto b','b',2,'p_b','rose.py',292),
  ('b -> empty','b',1,'p_b','rose.py',293),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','rose.py',298),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','rose.py',299),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','rose.py',300),
  ('vars -> GLOBALS c','vars',2,'p_vars','rose.py',305),
  ('c -> ID COMMA c','c',3,'p_c','rose.py',311),
  ('c -> ID COLON tipo SEMICOLON c','c',5,'p_c','rose.py',312),
  ('c -> ID COLON tipo SEMICOLON','c',4,'p_c','rose.py',313),
  ('tipo -> INT','tipo',1,'p_tipo','rose.py',318),
  ('tipo -> FLOAT','tipo',1,'p_tipo','rose.py',319),
  ('asignacion -> ID EQUALS expresion SEMICOLON','asignacion',4,'p_asignacion','rose.py',324),
  ('escritura -> PRINT LEFTPARENTHESIS e RIGHTPARENTHESIS SEMICOLON','escritura',5,'p_escritura','rose.py',329),
  ('e -> expresion PERIOD e','e',3,'p_e','rose.py',334),
  ('e -> CTES PERIOD e','e',3,'p_e','rose.py',335),
  ('e -> CTES','e',1,'p_e','rose.py',336),
  ('e -> expresion','e',1,'p_e','rose.py',337),
  ('e -> empty','e',1,'p_e','rose.py',338),
  ('expresion -> exp GT exp','expresion',3,'p_expresion','rose.py',344),
  ('expresion -> exp LT exp','expresion',3,'p_expresion','rose.py',345),
  ('expresion -> exp DIFFERENT exp','expresion',3,'p_expresion','rose.py',346),
  ('expresion -> exp','expresion',1,'p_expresion','rose.py',347),
  ('exp -> termino g','exp',2,'p_exp','rose.py',352),
  ('g -> PLUS termino g','g',3,'p_g','rose.py',358),
  ('g -> MINUS termino g','g',3,'p_g','rose.py',359),
  ('g -> empty','g',1,'p_g','rose.py',360),
  ('condicion -> IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque h SEMICOLON','condicion',7,'p_condicion','rose.py',365),
  ('h -> ELSE bloque','h',2,'p_h','rose.py',370),
  ('h -> empty','h',1,'p_h','rose.py',371),
  ('termino -> factor i','termino',2,'p_termino','rose.py',376),
  ('termino -> factor','termino',1,'p_termino','rose.py',377),
  ('i -> MULTIPLY factor i','i',3,'p_i','rose.py',382),
  ('i -> DIVIDE factor i','i',3,'p_i','rose.py',383),
  ('i -> MULTIPLY factor','i',2,'p_i','rose.py',384),
  ('i -> DIVIDE factor','i',2,'p_i','rose.py',385),
  ('factor -> LEFTPARENTHESIS expresion RIGHTPARENTHESIS','factor',3,'p_factor','rose.py',390),
  ('factor -> PLUS varcte','factor',2,'p_factor','rose.py',391),
  ('factor -> MINUS varcte','factor',2,'p_factor','rose.py',392),
  ('factor -> varcte','factor',1,'p_factor','rose.py',393),
  ('varcte -> ID','varcte',1,'p_varcte','rose.py',398),
  ('varcte -> CTEI','varcte',1,'p_varcte','rose.py',399),
  ('varcte -> CTEF','varcte',1,'p_varcte','rose.py',400),
  ('empty -> <empty>','empty',0,'p_empty','rose.py',405),
]
