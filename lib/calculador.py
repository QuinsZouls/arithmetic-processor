from lib.lista import Lista

# Realiza la operación según sea
def operator(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
# Pasamos la expresion infija a posfija
def parsePostfix(regex):
    dic = {}
    dic["*"] = 3
    dic["/"] = 3
    dic["+"] = 2
    dic["-"] = 2
    dic["("] = 1
    stack = Lista()
    postfixList = []
    tokenList = regex.split()

    for token in tokenList:
        if token.isnumeric():
            postfixList.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = stack.pop()
        else:
            while (not stack.isEmpty()) and \
               (dic[stack.peek()] >= dic[token]):
                  postfixList.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        postfixList.append(stack.pop())
    return " ".join(postfixList)
# Evaluamos la expresión posfija
def postfixEvaluation(postRegex):
    operandStack = Lista()
    tokenList = postRegex.split()

    for token in tokenList:
        if token.isnumeric():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operator(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()
