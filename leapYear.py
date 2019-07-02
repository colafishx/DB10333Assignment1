year=eval(input('plz insert a year(integer in 4 digits),'
                'and I will check whether it is a leap year or not:'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 4000 != 0:
    print('AD',year,'is a leap year!congratulations!!')
else:
    print('AD',year,'is not a leap year. What a shame man...')