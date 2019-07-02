import math
eType = eval(input('plz specify your type of electricity usage\n'
                 'for domestic use, plz input "0";for industrial use, plz input "1":'))
eUse = eval(input('Then, plz input your electricity usage for last month (in integer):'))
if eType == 1:
    print('your industrial electricity use last month is TWD$',math.ceil(eUse*0.45),'.')
elif eType == 0 and eUse <= 240:
    print('your household electricity use last month is TWD$',math.ceil(eUse*0.15),'.')
elif eType == 0 and 240 < eUse <= 540:
    print('your household electricity use last month is TWD$',
          math.ceil((eUse-240)*0.25+240*0.15), '.')
elif eType == 0 and eUse > 540:
    print('your household electricity use last month is TWD$',
          math.ceil((eUse-540)*0.45+(540-240)*0.25+240*0.15), '.')
else:
    print('[Invalid Input]plz kindly check your input and exercise again.')