import pandas as pd
import matplotlib.pyplot as plt
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 1. Showing the third and fourth columns for the first 10 rows
first_10_rows = dalys_data.iloc[0:10, 2:4]
print("First 10 rows (Year & DALYs):\n", first_10_rows)
# Determine the year with max DALYs in the first 10 rows (Afghanistan)
afg_first_10 = dalys_data.head(10)
daly_col_name = dalys_data.columns[3]
max_year_afg = afg_first_10.loc[afg_first_10[daly_col_name].idxmax(), "Year"]
print(f"\nYear with maximum DALYs in the first 10 years for Afghanistan: {max_year_afg}")

# 2. Using a Boolean to show all years for Zimbabwe
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]
print("\nYears recorded for Zimbabwe:\n", zimbabwe_years.tolist())

# 3. Computing countries with max and min DALYs in 2019
recent_data = dalys_data[dalys_data["Year"] == 2019]
max_country_2019 = recent_data.loc[recent_data[daly_col_name].idxmax(), "Entity"]
min_country_2019 = recent_data.loc[recent_data[daly_col_name].idxmin(), "Entity"]
print(f"\n2019 - Country with Max DALYs: {max_country_2019}")
print(f"2019 - Country with Min DALYs: {min_country_2019}")

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