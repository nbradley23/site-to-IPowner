

try:
    num_hours = float(input('Enter amount of hours: '))
    payrate = float(input('Enter rate of pay: '))
    if (num_hours) <= 40:
        grosspay = num_hours * payrate
        print('Your gross pay is:', grosspay)
    elif (num_hours) > 40:
        overtimehours = num_hours - 40
        regratepay = payrate * 40
        overtimepay = overtimehours * (payrate * 1.5)
        print('Your gross pay is:', regratepay + overtimepay)
except:
    print('Please enter correct hours and payrate.')
