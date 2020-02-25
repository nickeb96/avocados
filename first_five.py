# Sean Southland and Nicholas Boyle

import pandas as pd

df = pd.read_csv("avocado.csv")


# Question 1: Which region has the highest average avocado price?
# Answer 1: The region with the highest average avocado price is HartfordSpringfield

# Question 2: Which region has the lowest average avocado price?
# Answer 2: The region with the lowest average avocado price is Houston

# begin code for questions 1 and 2
AveragePriceByRegion = df.groupby("region")
AveragePriceByRegion = AveragePriceByRegion.sum().sort_values(['AveragePrice'], ascending=False)

answer1 = AveragePriceByRegion['AveragePrice'].head(1)
print(answer1, "\n")

answer2 = AveragePriceByRegion['AveragePrice'].tail(1)
print(answer2, "\n")
# end code for questions 1 and 2

# Question 3: Which region sells the most of each avocado size?
# Answer 3: SouthCentral sells the most 4046 avocados, Northeast sells the most 4225 avocados,
# and GreatLakes sells the most 4770 avocados

# Question 4: Which region sells the least of each avocado size?
# Answer 4: Syracuse sells the least 4046 avocados, Boise sells the least 4225 avocados,
# and StLouis sells the least 4770 avocados

# begin code for questions 3 and 4
Avocado4046ByRegion = df.groupby("region")
Avocado4046ByRegion = Avocado4046ByRegion.sum().sort_values(['4046'], ascending=False)

answer3a = Avocado4046ByRegion['4046'].head(2)
answer4a = Avocado4046ByRegion['4046'].tail(1)

Avocado4225ByRegion = df.groupby("region")
Avocado4225ByRegion = Avocado4225ByRegion.sum().sort_values(['4225'], ascending=False)

answer3b = Avocado4225ByRegion['4225'].head(2)
answer4b = Avocado4225ByRegion['4225'].tail(1)

Avocado4770ByRegion = df.groupby("region")
Avocado4770ByRegion = Avocado4770ByRegion.sum().sort_values(['4770'], ascending=False)

answer3c = Avocado4770ByRegion['4770'].head(2)
answer4c = Avocado4770ByRegion['4770'].tail(1)

print(answer3a, '\n')
print(answer3b, '\n')
print(answer3c, '\n')

print(answer4a, '\n')
print(answer4b, '\n')
print(answer4c, '\n')
# end code for questions 3 and 4

# Question 5: What is the total average price for each year? (2015, 2016, 2017, 2018)
# Answer 5: The total average price for 2015 is $1.38, the total average price for 2016 is $1.34, the total average
# price for 2017 is $1.52, and the total average price for 2018 is $1.35

# begin code for question 5
AveragePriceByYear = df.groupby('year')
AveragePriceByYear = AveragePriceByYear.mean().sort_values(['AveragePrice'], ascending=False)

answer5 = AveragePriceByYear['AveragePrice']
print(answer5)
# end code for question 5
