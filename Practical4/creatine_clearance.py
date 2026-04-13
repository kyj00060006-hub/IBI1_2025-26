#Pseudocode:
#Use while loops and try-except to get valid inputs for age, weight, cr concentration and gender.
#check if values are within the ranges
#calculate crcl using Cockcroft-Gault equation
#if female ,crcl should be mutiplied with 0.85
#the loops will keep running until it is valid
while True:
    try:
        age=float(input('Your age:'))
        if 0<age<100:
            break
        else:
            print('Your age should be between 0 and 100!Plz try again')
    except ValueError:
        print('Plz input valid number! NUMBER!!!')

while True:
    try:
        weight=float(input('Your weight(kg):'))
        if 20<weight<80:
            break
        else:
            print('Your weight should be between 20kg and 80kg!Plz try again')
    except ValueError:
        print('Plz input valid number! NUMBER!!!')

while True:
    try:
        cr=float(input('Your cr concentration:'))
        if 0<cr<100:
            break
        else:
            print('Your cr concentration should be between 0 and 100umol/l!Plz try again')
    except ValueError:
        print('Plz input valid number! NUMBER!!!')
        
while True:
    gender=input('Your gender(male/female):').strip().lower()
    if gender in ['male','female']:
        break
    else:
        print('Plz input your biological gender! MALE or FEMALE!')  
        
crcl=((140-age)*weight)/(72*cr)
if gender=='female':
    crcl*=0.85
crcl=round(crcl,2)
    
print('\nResult:')
print(f'Your crcl is {crcl} ml/min.')