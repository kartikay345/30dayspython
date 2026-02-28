print('welcome to know if it is leap year or not')
year=int(input('which year do you want to know we it is leap year or not'))
if year%400==0:
  print('it is a leap year')
elif year%100==0:
  print('it is not a leap year')
elif year%4==0:
  print('it is a leap year')
else:
  print('try next time to get the year written')      