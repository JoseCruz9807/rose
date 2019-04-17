from DirFunc import *


x = DirFunc('global', 'int')
print(list(x.val))
x.addFunc('func1', 'float')
x.addFunc('func2', 'float')
print(x.val)
x.addVariable('global', 'fNum', 'FLOAT', 1, 2)

print(x.val)
print(x.val['global'][1])

x.addVariable('global', 'iNum', 'INT', 2, 2)
x.addVariable('func1', 'fNum', 'FLOAT', 1, 1)
print(x.val)
print(x.val['global'][1])

print(list(x.val))
