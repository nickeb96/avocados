
import pandas as pd

df = pd.read_csv("avocado.csv")




months = {x: 0 for x in range(1, 13)}
for date in df["Date"]:
    month_number = int(date.split("-")[1])
    months[month_number] += 1

# Question 6 = January
print("Month {} had the most avocado sales.".format(
    max((v, k) for k, v in months.items())[1]))



blanket_regions = {"TotalUS", "West", "East"}
region_volumes = dict()
for region in df["region"].unique():
    region_volumes[region] = df[df["region"] == region]["Total Volume"].sum()

# Question 7 = California
print("Region with most avocado sales by volume is {}.".format(
    max((v, k) for k, v in region_volumes.items() if k not in blanket_regions)[1]))



# Question 8 = Syracuse
print("Region with least avocado sales by volume is {}.".format(
    min((v, k) for k, v in region_volumes.items() if k not in blanket_regions)[1]))



year_volumes = dict()
for year in df["year"].unique():
    year_volumes[year] = df[df["year"] == year]["Total Volume"].sum()

# Question 9 = 2017
print("Year {} had the most avocado sales".format(
    max((v, k) for k, v in year_volumes.items())[1]))



total_organic = df[df["type"] == "organic"]["Total Volume"].sum()
total_conventional = df[df["type"] == "conventional"]["Total Volume"].sum()

# Question 10 = organic: 2.81%; conventional: 97.19%
print("Organic avocodos make up {:.2%} and conventional avocodos make up {:.2%}."
        .format(total_organic / (total_organic + total_conventional),
                total_conventional / (total_organic + total_conventional)))



