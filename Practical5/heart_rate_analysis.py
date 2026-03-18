import matplotlib.pyplot as plt

#heart rates, and you can add more
heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
print("you can enter heart rate data, enter 'q' when u have finished inputting.")
while True:
    addition=input().strip()
    if addition.lower()=='q':
        break
    try:
        num=float(addition)
        heart_rates.append(num)
        print('u can enter more')
    except ValueError:
        print('number or q, plz!!!')
#sort the heart rate data
low,normal,high=0,0,0
for hr in heart_rates:
    if hr<60:
        low+=1
    elif hr>120:
        high+=1
    else:
        normal+=1

#figure out mean and largest      
count=len(heart_rates)
mean_hr=sum(heart_rates)/count
categories={'Low':low,'Normal':normal,'High':high}
largest=max(categories,key=categories.get)

#print the analysis
print("\n=== Heart Rate Analysis ===")
print(f"Total patients: {count},Mean heart rate: {mean_hr:.1f} bpm")
print(f"Low (<60): {low},Normal (60-120): {normal},High (>120): {high}")
print(f'largest category:{largest}')

plt.figure(figsize=(6, 6))
plt.pie([low, normal, high], labels=["Low", "Normal", "High"],
        autopct="%1.1f%%", colors=["lightblue", "lightgreen", "salmon"])
plt.title("Heart Rate Categories")
plt.show()