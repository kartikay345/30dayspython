# today we are going to build a converter for the numbers to the romannumbers]
# we are going to use tuple for it 
# this is how tuples work 
# conerters_number=[
    # (1000,"M"),
    # (900,"CM"),
    # (500,"D"),
    # (400,"CD"),
    # (100,"C"), exampple this is your tuple 
# print conerters_numbers[o] will give you (1000 m)
# print conerters_numbers[0][0] will give you (1000 )




conerters_number=[
    (1000,"M"),
    (900,"CM"),
    (500,"D"),
    (400,"CD"),
    (100,"C"),
    (90,"XC"),
    (50,"L"),
    (40,"XL"),
    (10,"X"), 
    (9,"IX"),
    (5,"V"),
    (4,"VI"),
    (1,"I")

]
#getting number from the user 
num =int(input('what number would like to conver in roman form 1-3999'))

#loop for the convertion 
results =""
for key , value in conerters_number:
    while num>=key:
        results+=value
        num-= key
print('Here is your result of your calculator',results)


