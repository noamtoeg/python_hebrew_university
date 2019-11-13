ef calculate_mathematical_expression(a,b,operator):
    a = float(a)      # turn a and b from strings to floats
    b = float(b)
    operators = ['/','*','+','-']
    if b == 0 and operator == '/':     #exception for division by zero
        return None
    elif operator not in operators:
        return None
    elif operator == '+':      #adding  2 numbers and returning the result as integer if the result is a whole number
        if a + b == int(a + b):
            return int(a + b)
        else:
            return float(a + b)
    elif operator == '-':      #substracting  2 numbers and returning the result as integer if the result is a whole number
        if a - b == int(a - b):
            return int(a - b)
        else:
            return float(a - b)
    elif operator == '*':      #multiplying  2 numbers and returning the result as integer if the result is a whole number
        if a * b == int(a * b):
            return int(a * b)
        else:
            return float(a * b)
    elif operator == '/':
        return a / b
    #    print('please chose a valid operator')

def calculate_from_string(expression):
    list_of_operations = expression.split()    # Splits the string into 2 numbers and 1 operator
    a = list_of_operations[0]       # assigns numbers a and b and operator from list
    b = list_of_operations[2]
    operator = list_of_operations[1]
    return calculate_mathematical_expression(a,b,operator)      #runs calculate_mathematical_expression func.






