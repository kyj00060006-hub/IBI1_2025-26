#Some simple math
a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
print('difference 2004-2014:',round(d,2))
print('difference 2014-2024:',round(e,2))
#Answer:d >e
#So the population growth in Scotland is decelerating.
#Booleans task
X=True
Y=False
W=X or Y
print(W)
#W=True

#Truth Table for W=(X and not Y) or (not X and Y)
# X=True,Y=True => W=False
# X=True,Y=False => W=True
# X=False,Y=True => W=True
# X=False,Y=False => W=False