from lib.balanceador import checkBalance
from lib.calculador import parsePostfix, postfixEvaluation
regex = '( ( 3 * 2 ) - 3 )'


if checkBalance(regex) :
  parsed = parsePostfix(regex)
  print(postfixEvaluation(parsed))
else:
  print('Expresión no válida')