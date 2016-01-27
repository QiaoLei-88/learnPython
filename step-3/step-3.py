import math

def format_term(a, symbol, is_leading_term = False):
    if is_leading_term:
        assert symbol != ''
        if a==1:
            return symbol;
        elif a==0:
            return ''
        elif a==-1:
            return '-' + symbol
        else:
            return str(a) + symbol
    if symbol=='':
        # Trailing term
        if a>0:
            return '+' + str(a)
        elif a<0:
            return str(a)
        else:
            return ''
    # Normal term
    if a>0:
        if a==1:
            return '+' + symbol
        else:
            return '+' + str(a) + symbol
    elif a<0:
        if a==-1:
            return '-' + symbol
        else:
            return str(a) + symbol
    else:
        return ''
    # End function

def quadratic(a, b, c):
    # Check argument type
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError('use integer or float as arguments!')
    if a == 0.0:
        raise ArithmeticError("parameter 'a' can't be zero!")

    out = 'Solution to equation "'
    out += format_term(a, 'x^2', True)
    out += format_term(b, 'x')
    out += format_term(c, '')
    out += '=0"'
    out = out.ljust(40, ' ') + ' is '

    delta = b*b - 4*a*c
    if delta < 0.0:
        out += 'No real solution!'
    elif delta == 0.0:
        out += 'x=' + str(-b/(2*a))
    else:
        out += 'x=' + str( ((-b + math.sqrt(delta))/(2*a), \
                            (-b - math.sqrt(delta))/(2*a)) )
    print out
    return

# Main 
quadratic(1, 2.0, 1)
quadratic(1, 3, 5)
quadratic(1, 0, 0)
quadratic(1, 0, -1)
quadratic(2, 7, -9)
quadratic(-1, 1, 12)
quadratic(-1, -1, 12)
# This will trigger the ArithmeticError
#quadratic(0, 1, -1)
# This will trigger the TypeError
#quadratic(0, 1, 'zz')
