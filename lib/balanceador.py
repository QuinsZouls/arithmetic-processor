from lib.lista import Lista
## Verifica si la cadena es valida en cuanto a parentesis
def checkBalance(text):
  count  = Lista()
  balanced = True
  index = 0
  while index < len(text) and balanced:
    symbol = text[index]
    if symbol == '(':
      count.push(symbol)
    elif symbol == ')':
      if count.isEmpty():
        balanced = False
      else:
        count.pop()

    index += 1
  return balanced and count.isEmpty()