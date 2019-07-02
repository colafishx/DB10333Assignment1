import math
salary=eval(input('plz input the total working hour (integer) in the convenience store:'))
# bastard boss salary calculation is as below, what a shame!
if salary <= 60:
    print('Your salary for last month is TWD$',
          math.floor(salary)*120,'.')
elif 61<=salary<=80:
    print('Your salary for last month is TWD$',
          int((math.floor(salary)-60)*120*1.25)+60*120,'.')
elif salary>=81:
    print('Your salary for last month is TWD$',
          int((math.floor(salary)-80)*120*1.5)+60*120+20*120*1.25,'.')