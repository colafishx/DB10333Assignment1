month=eval(input('plz input a month(integer) in a year:'))
if month in (3,4,5):
    print(month,'is in spring!')
elif month in (6,7,8):
    print(month, 'is in summer!')
elif month in (9,10,11):
    print(month, 'is in fall!')
elif month in (1,2,12):
    print(month, 'is in winter!')
else:
    print(month, "isn't a month man![input error]")