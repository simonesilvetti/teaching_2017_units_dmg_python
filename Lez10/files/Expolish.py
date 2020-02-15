

def isAnOperator( x ):
    """Return True if x is '+','-','*','/'"""
    return (x=='+') or (x=='-') or (x=='*') or (x=='/')

def compute( op , x , y ):
    """Compute the value of expression 'x op y', where -x and y 
are two integers and op is an operator in '+','-','*','/'"""
    if (op=='+'):
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=='/':
        return x/y
    else:
        return 0

def evalPolishExpression( e ):
    """Evaluate expression e in polish notation"""
    stack = []
    for v in [ e[len(e)-i] for i in range(1,len(e)+1) ]:
        if isAnOperator( v ):
            stack.append( compute( v , stack.pop() , stack.pop() ) )
        else:
            stack.append( v )
    return stack.pop()


