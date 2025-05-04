import re

def evalAndReplaceParensDelExpr(expression):
    openedParens = 0
    closedParens = 0
    parensDelExpr = ''
    evaluableExpression = expression
    for char in expression:
        if char == '(':
            openedParens += 1
        if char == ')':
            closedParens += 1
        if openedParens > 0:
            parensDelExpr += char
        if openedParens == closedParens and openedParens > 0 and closedParens > 0:
            # If we have more parensDelExps inside, recurse
            if re.search(r"\(|\)", parensDelExpr[1:len(parensDelExpr)-1]):
                evaluableExpression = evaluableExpression.replace(
                    parensDelExpr,
                    evalAndReplaceParensDelExpr(
                        parensDelExpr[1:len(parensDelExpr)-1]
                    )
                )
            evaluated = eval(replaceWhatPercentage(replacePercentageOf(parensDelExpr)))
            evaluableExpression = evaluableExpression.replace(
                parensDelExpr,
                str(evaluated)
            )
            openedParens = 0
            closedParens = 0
            parensDelExpr = ''
    return evaluableExpression

def replaceWhatPercentage(expression):
    pedazos = re.search(r"(\d+)\s*(\%\?)\s*(\d+)", expression)
    if (pedazos):
        return re.sub(
            r"(\d+)\s*(\%\?)\s*(\d+)",
            f"{pedazos.group(1)}/{pedazos.group(3)}*100",
            expression
        )
    else: return expression
    
def replacePercentageOf(expression):
    return expression.replace("%>", "*0.01*")
    
def evaluatePowREPL(expression):
    return eval(replaceWhatPercentage(replacePercentageOf(evalAndReplaceParensDelExpr(expression))))