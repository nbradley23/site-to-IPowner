def calculate(**kwargs):
    if kwargs['make_float']:
        first = float(kwargs['first'])
        second = float(kwargs['second'])
    else:
        first = int(kwargs['first'])
        second = int(kwargs['second'])
    
    operations = {
        'add': first + second,
        'subtract': first - second,
        'divide': first / second,
        'multiply':first * second
    }

    calculation = operations[kwargs['operation']]
    if 'message' in kwargs:
        return kwargs['message'] + ' ' + str(calculation)
    return "The result is" + ' ' + str(calculation)

print(calculate(make_float=True, operation='divide', first=3.5, second=5))
