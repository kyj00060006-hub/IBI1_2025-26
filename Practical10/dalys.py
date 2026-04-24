import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/Users/kyj/Desktop/ibi/Portfolio/Practical10')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 1. Showing the third and fourth columns for the first 10 rows
first_10_rows = dalys_data.iloc[0:10, 2:4]
print("First 10 rows (Year & DALYs):\n", first_10_rows)
# Determine the year with max DALYs in the first 10 rows (Afghanistan)
afg_first_10 = dalys_data.head(10)
daly_col_name = dalys_data.columns[3]
max_year_afg = afg_first_10.loc[afg_first_10[daly_col_name].idxmax(), "Year"]
print(f"\nYear with maximum DALYs in the first 10 years for Afghanistan: {max_year_afg}")
# The year with maximum DALYs in the first 10 rows for Afghanistan is: 1998

# 2. Boolean to show all years for Zimbabwe
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]
print("\nYears recorded for Zimbabwe:\n", zimbabwe_years.tolist())
first_zim = zimbabwe_years.min()
last_zim = zimbabwe_years.max()
print(f"\nFirst year recorded for Zimbabwe: {first_zim}")
print(f"Last year recorded for Zimbabwe: {last_zim}")
# First year recorded for Zimbabwe: 1990; Last year recorded for Zimbabwe: 2019

# 3. Countries with max and min DALYs in 2019
recent_data = dalys_data[dalys_data["Year"] == 2019]
max_country_2019 = recent_data.loc[recent_data[daly_col_name].idxmax(), "Entity"] # idxmax() function means find the index of the maximum, i learn it from GenAI and optimize the loop structure.
min_country_2019 = recent_data.loc[recent_data[daly_col_name].idxmin(), "Entity"] # the same as above.
print(f"\n2019 - Country with Max DALYs: {max_country_2019}")
print(f"2019 - Country with Min DALYs: {min_country_2019}")
# Country with maximum DALYs in 2019: Lesotho
# Country with minimum DALYs in 2019: Singapore

# 4. Plotting DALYs over time for the country with Maximum DALYs
target_data = dalys_data[dalys_data["Entity"] == max_country_2019]
plt.figure(figsize=(10, 6))
plt.plot(target_data["Year"], target_data[daly_col_name], 'r-o', label=max_country_2019)
plt.title(f"DALYs Rate Over Time in {max_country_2019}")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.xticks(target_data["Year"], rotation=-90)
plt.legend()
plt.tight_layout()
plt.show()

# 5. Code to answer the question
plt.figure(figsize=(10, 6))
plt.hist(recent_data[daly_col_name].dropna(), bins=25, color='skyblue', edgecolor='black')
plt.title("Distribution of DALYs Rates Across All Countries in 2019")
plt.xlabel("DALYs Rate")
plt.ylabel("Frequency (Number of Countries)")
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()