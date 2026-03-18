import matplotlib.pyplot as plt

#data(2020,2024)
population_data = {
    "UK": {"2020": 66.7, "2024": 69.2},
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}
percentage_changes = {}

#calculate percentage change
for country, pop in population_data.items():
    pop_2020=pop["2020"]
    pop_2024=pop["2024"]
    change=((pop_2024-pop_2020)/pop_2020)*100
    percentage_changes[country]=change

#sort in descending order
sorted_changes=dict(sorted(percentage_changes.items(),key=lambda item:item[1],reverse=True))
print("the population changes in descending order, from the largest increase to the largest decrease:")
for country, change in sorted_changes.items():
    print(f"{country}:{change:.2f}%")

#largest increase and largest decrease
countries=list(sorted_changes.keys())
print(f"\nlargest increase in population:{countries[0]}")
print(f"largest decrease in population:{countries[-1]}")

#bar chart
plt.bar(sorted_changes.keys(), sorted_changes.values(),color=['blue' if v > 0 else 'red' for v in sorted_changes.values()])
plt.title("Population Change(2020vs2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change(%)")
plt.axhline(0,color='black',linewidth=0.8)
plt.show()