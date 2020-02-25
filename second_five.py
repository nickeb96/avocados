
import pandas as pd

df = pd.read_csv("avocado.csv")

months = {x: 0 for x in range(1, 13)}
for date in df["Date"]:
    month_number = int(date.split("-")[1])
    months[month_number] += 1
print("Month {} had the most avocado sales.".format(max((v, k) for k, v in months.items())[1]))


