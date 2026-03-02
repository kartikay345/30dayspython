fare =0
cap=0
details =input("there are few questions i would like to ask form you are \nlocal or express ").strip().lower()
detail2=int(input('how many rides per week you do'))
detail3=input("how would like to proceed your payment(omny or pay per ride)").strip().lower()

if details =='local':
  fare=3
  cap=35
elif details =='express':
  fare=7.25
  cap=67  
else:
  print('please type local or express  only')

# for the ride per week
pay_per_ride =detail2*fare


if detail3=='omny':
  print ('this will be your fare price',min(pay_per_ride,cap))
elif detail3=='pay per ride' :
  print(' your fare price will be ',pay_per_ride)
else:
  print('oops i think there is a typo ')  
