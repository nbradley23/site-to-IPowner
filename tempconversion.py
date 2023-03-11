def ctof():
    degcel = input('Enter the degrees in Celsius: ')
    degfehr = round(float(degcel) * (9/5) + 32, 1)
    print('The degrees in Fahrenheit is:', degfehr)


def ftoc():
    degfehr = input('Enter the degrees in Fahrenheit: ')
    degcel = round((float(degfehr) - 32) * (5/9), 1)
    print('The degrees in Celsius is:', degcel)


def tempcalc():
    fehrorcel = input(
        'Are you converting from Celcius or Fehrenhiet? (Please enter either C or F):\n')
    if fehrorcel == 'C' or fehrorcel == 'c':
        ctof()
    elif fehrorcel == 'F' or fehrorcel == 'f':
        ftoc()
    else:
        print('Invalid entry. Please enter either C or F')


tempcalc()
