# set total population to 91
# set initial infected to 5, growth rate to 0.40
# use Whlie loop to calculate daily increase
# Update day count and print status
# Stop when everyone is infected
 
total_students=91
infected=5
growth_rate=0.40
days=1

print(f'on the {days} day, {infected} students are infected.')

while infected<total_students:
    new_infections=infected*growth_rate
    infected+=new_infections
    days+=1
    if infected>total_students:
        infected=total_students
    print(f'on the {days} day, {infected} students are infected')
print(f'it takes {days} days to infect all.')