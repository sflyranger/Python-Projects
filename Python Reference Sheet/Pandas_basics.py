# Print the head of data
print(df.head())
# Print information about the data
print(df.info())
# Print the shape of the data, notice there is no parenthesis after shape.
print(df.shape)
# Print a description of the data.
print(df.describe())

# Import pandas using the alias pd
import pandas as pd
# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'], ascending=[True,False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[['state','family_members']]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

# Print the head of the result
print(ind_state.head())
#    individuals       state  #output
# 0       2570.0     Alabama
# 1       1434.0      Alaska
# 2       7259.0     Arizona
# 3       2280.0    Arkansas
# 4     109008.0  California


# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]

# See the result
print(ind_gt_10k)
#                 region       state  individuals  family_members  state_pop
# 4              Pacific  California     109008.0         20964.0   39461588
# 9       South Atlantic     Florida      21443.0          9587.0   21244317
# 32        Mid-Atlantic    New York      39827.0         52070.0   19530351
# 37             Pacific      Oregon      11139.0          3337.0    4181886
# 43  West South Central       Texas      19199.0          6111.0   28628666
# 47             Pacific  Washington      16424.0          5880.0    7523869


# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region']=='Mountain']

# See the result
print(mountain_reg)

#       region       state  individuals  family_members  state_pop
# 2   Mountain     Arizona       7259.0          2606.0    7158024
# 5   Mountain    Colorado       7607.0          3250.0    5691287
# 12  Mountain       Idaho       1297.0           715.0    1750536
# 26  Mountain     Montana        983.0           422.0    1060665
# 28  Mountain      Nevada       7058.0           486.0    3027341
# 31  Mountain  New Mexico       1949.0           602.0    2092741
# 44  Mountain        Utah       1904.0           972.0    3153550
# 50  Mountain     Wyoming        434.0           205.0     577601


# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) & (homelessness['region']=='Pacific')]

# See the result
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

#             region                 state  individuals  family_members  state_pop
# 7   South Atlantic              Delaware        708.0           374.0     965479
# 8   South Atlantic  District of Columbia       3770.0          3134.0     701547
# 9   South Atlantic               Florida      21443.0          9587.0   21244317



# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness['state'].isin(canu)

# See the result
print(mojave_homelessness)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states, make sure to put dataframe name outside one more time to pull actual data,
# otherwise the result is only boolean values.
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

# Adding new columns in pandas


# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"]/homelessness["total"]

# See the result
print(homelessness)
#                 region                 state  individuals  family_members  state_pop     total  p_individuals
# 0   East South Central               Alabama       2570.0           864.0    4887681    3434.0          0.748
# 1              Pacific                Alaska       1434.0           582.0     735139    2016.0          0.711
# 2             Mountain               Arizona       7259.0          2606.0    7158024    9865.0          0.736
# 3   West South Central              Arkansas       2280.0           432.0    3009733    2712.0          0.841
# 4              Pacific            California     109008.0         20964.0   39461588  129972.0          0.839
# 5             Mountain              Colorado       7607.0          3250.0    5691287   10857.0          0.701
# 6          New England           Connecticut       2280.0          1696.0    3571520    3976.0          0.573
# 7       South Atlantic              Delaware        708.0           374.0     965479    1082.0          0.654
# 8       South Atlantic  District of Columbia       3770.0          3134.0     701547    6904.0          0.546
# 9       South Atlantic               Florida      21443.0          9587.0   21244317   31030.0          0.691
# 10      South Atlantic               Georgia       6943.0          2556.0   10511131    9499.0          0.731
# 11             Pacific                Hawaii       4131.0          2399.0    1420593    6530.0          0.633
# 12            Mountain                 Idaho       1297.0           715.0    1750536    2012.0          0.645
# 13  East North Central              Illinois       6752.0          3891.0   12723071   10643.0          0.634
# 14  East North Central               Indiana       3776.0          1482.0    6695497    5258.0          0.718
# 15  West North Central                  Iowa       1711.0          1038.0    3148618    2749.0          0.622
# 16  West North Central                Kansas       1443.0           773.0    2911359    2216.0          0.651
# 17  East South Central              Kentucky       2735.0           953.0    4461153    3688.0          0.742
# 18  West South Central             Louisiana       2540.0           519.0    4659690    3059.0          0.830
# 19         New England                 Maine       1450.0          1066.0    1339057    2516.0          0.576
# 20      South Atlantic              Maryland       4914.0          2230.0    6035802    7144.0          0.688
# 21         New England         Massachusetts       6811.0         13257.0    6882635   20068.0          0.339
# 22  East North Central              Michigan       5209.0          3142.0    9984072    8351.0          0.624
# 23  West North Central             Minnesota       3993.0          3250.0    5606249    7243.0          0.551
# 24  East South Central           Mississippi       1024.0           328.0    2981020    1352.0          0.757
# 25  West North Central              Missouri       3776.0          2107.0    6121623    5883.0          0.642
# 26            Mountain               Montana        983.0           422.0    1060665    1405.0          0.700
# 27  West North Central              Nebraska       1745.0           676.0    1925614    2421.0          0.721
# 28            Mountain                Nevada       7058.0           486.0    3027341    7544.0          0.936
# 29         New England         New Hampshire        835.0           615.0    1353465    1450.0          0.576
# 30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025    9398.0          0.644
# 31            Mountain            New Mexico       1949.0           602.0    2092741    2551.0          0.764
# 32        Mid-Atlantic              New York      39827.0         52070.0   19530351   91897.0          0.433
# 33      South Atlantic        North Carolina       6451.0          2817.0   10381615    9268.0          0.696
# 34  West North Central          North Dakota        467.0            75.0     758080     542.0          0.862
# 35  East North Central                  Ohio       6929.0          3320.0   11676341   10249.0          0.676
# 36  West South Central              Oklahoma       2823.0          1048.0    3940235    3871.0          0.729
# 37             Pacific                Oregon      11139.0          3337.0    4181886   14476.0          0.769
# 38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922   13512.0          0.604
# 39         New England          Rhode Island        747.0           354.0    1058287    1101.0          0.678
# 40      South Atlantic        South Carolina       3082.0           851.0    5084156    3933.0          0.784
# 41  West North Central          South Dakota        836.0           323.0     878698    1159.0          0.721
# 42  East South Central             Tennessee       6139.0          1744.0    6771631    7883.0          0.779
# 43  West South Central                 Texas      19199.0          6111.0   28628666   25310.0          0.759
# 44            Mountain                  Utah       1904.0           972.0    3153550    2876.0          0.662
# 45         New England               Vermont        780.0           511.0     624358    1291.0          0.604
# 46      South Atlantic              Virginia       3928.0          2047.0    8501286    5975.0          0.657
# 47             Pacific            Washington      16424.0          5880.0    7523869   22304.0          0.736
# 48      South Atlantic         West Virginia       1021.0           222.0    1804291    1243.0          0.821
# 49  East North Central             Wisconsin       2740.0          2167.0    5807406    4907.0          0.558
# 50            Mountain               Wyoming        434.0           205.0     577601     639.0          0.679
#
#


# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"]/ homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
print(high_homelessness)
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)

print(homelessness)

#             region                 state  individuals  family_members  state_pop  indiv_per_10k
# 4          Pacific            California     109008.0         20964.0   39461588         27.624
# 8   South Atlantic  District of Columbia       3770.0          3134.0     701547         53.738
# 11         Pacific                Hawaii       4131.0          2399.0    1420593         29.079
# 28        Mountain                Nevada       7058.0           486.0    3027341         23.314
# 32    Mid-Atlantic              New York      39827.0         52070.0   19530351         20.392
# 37         Pacific                Oregon      11139.0          3337.0    4181886         26.636
# 47         Pacific            Washington      16424.0          5880.0    7523869         21.829
#                    state  indiv_per_10k
# 8   District of Columbia         53.738
# 11                Hawaii         29.079
# 4             California         27.624
# 37                Oregon         26.636
# 28                Nevada         23.314
# 47            Washington         21.829
# 32              New York         20.392
#                 region                 state  individuals  family_members  state_pop  indiv_per_10k
# 0   East South Central               Alabama       2570.0           864.0    4887681          5.258
# 1              Pacific                Alaska       1434.0           582.0     735139         19.507
# 2             Mountain               Arizona       7259.0          2606.0    7158024         10.141
# 3   West South Central              Arkansas       2280.0           432.0    3009733          7.575
# 4              Pacific            California     109008.0         20964.0   39461588         27.624
# 5             Mountain              Colorado       7607.0          3250.0    5691287         13.366
# 6          New England           Connecticut       2280.0          1696.0    3571520          6.384
# 7       South Atlantic              Delaware        708.0           374.0     965479          7.333
# 8       South Atlantic  District of Columbia       3770.0          3134.0     701547         53.738
# 9       South Atlantic               Florida      21443.0          9587.0   21244317         10.094
# 10      South Atlantic               Georgia       6943.0          2556.0   10511131          6.605
# 11             Pacific                Hawaii       4131.0          2399.0    1420593         29.079
# 12            Mountain                 Idaho       1297.0           715.0    1750536          7.409
# 13  East North Central              Illinois       6752.0          3891.0   12723071          5.307
# 14  East North Central               Indiana       3776.0          1482.0    6695497          5.640
# 15  West North Central                  Iowa       1711.0          1038.0    3148618          5.434
# 16  West North Central                Kansas       1443.0           773.0    2911359          4.956
# 17  East South Central              Kentucky       2735.0           953.0    4461153          6.131
# 18  West South Central             Louisiana       2540.0           519.0    4659690          5.451
# 19         New England                 Maine       1450.0          1066.0    1339057         10.829
# 20      South Atlantic              Maryland       4914.0          2230.0    6035802          8.141
# 21         New England         Massachusetts       6811.0         13257.0    6882635          9.896
# 22  East North Central              Michigan       5209.0          3142.0    9984072          5.217
# 23  West North Central             Minnesota       3993.0          3250.0    5606249          7.122
# 24  East South Central           Mississippi       1024.0           328.0    2981020          3.435
# 25  West North Central              Missouri       3776.0          2107.0    6121623          6.168
# 26            Mountain               Montana        983.0           422.0    1060665          9.268
# 27  West North Central              Nebraska       1745.0           676.0    1925614          9.062
# 28            Mountain                Nevada       7058.0           486.0    3027341         23.314
# 29         New England         New Hampshire        835.0           615.0    1353465          6.169
# 30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025          6.806
# 31            Mountain            New Mexico       1949.0           602.0    2092741          9.313
# 32        Mid-Atlantic              New York      39827.0         52070.0   19530351         20.392
# 33      South Atlantic        North Carolina       6451.0          2817.0   10381615          6.214
# 34  West North Central          North Dakota        467.0            75.0     758080          6.160
# 35  East North Central                  Ohio       6929.0          3320.0   11676341          5.934
# 36  West South Central              Oklahoma       2823.0          1048.0    3940235          7.165
# 37             Pacific                Oregon      11139.0          3337.0    4181886         26.636
# 38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922          6.377
# 39         New England          Rhode Island        747.0           354.0    1058287          7.059
# 40      South Atlantic        South Carolina       3082.0           851.0    5084156          6.062
# 41  West North Central          South Dakota        836.0           323.0     878698          9.514
# 42  East South Central             Tennessee       6139.0          1744.0    6771631          9.066
# 43  West South Central                 Texas      19199.0          6111.0   28628666          6.706
# 44            Mountain                  Utah       1904.0           972.0    3153550          6.038
# 45         New England               Vermont        780.0           511.0     624358         12.493
# 46      South Atlantic              Virginia       3928.0          2047.0    8501286          4.620
# 47             Pacific            Washington      16424.0          5880.0    7523869         21.829
# 48      South Atlantic         West Virginia       1021.0           222.0    1804291          5.659
# 49  East North Central             Wisconsin       2740.0          2167.0    5807406          4.718
# 50            Mountain               Wyoming        434.0           205.0     577601            7.514
#


# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())
#    store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
# 0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
# 1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8.106
# 2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7.808
# 3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7.808
# 4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7.808
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10774 entries, 0 to 10773
# Data columns (total 9 columns):
 #   Column                Non-Null Count  Dtype
# ---  ------                --------------  -----
#  0   store                 10774 non-null  int64
#  1   type                  10774 non-null  object
#  2   department            10774 non-null  int32
#  3   date                  10774 non-null  datetime64[ns]
#  4   weekly_sales          10774 non-null  float64
#  5   is_holiday            10774 non-null  bool
#  6   temperature_c         10774 non-null  float64
#  7   fuel_price_usd_per_l  10774 non-null  float64
#  8   unemployment          10774 non-null  float64
# dtypes: bool(1), datetime64[ns](1), float64(4), int32(1), int64(1), object(1)
# memory usage: 641.9+ KB
# None
# 23843.95014850566
# 12049.064999999999


print(sales["date"].max())
# 2012-10-26 00:00:00
print(sales["date"].min())
# 2010-02-05 00:00:00


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales['temperature_c'].agg(iqr))
# 16.583333333333336


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))


# temperature_c           16.583
# fuel_price_usd_per_l     0.073
# unemployment             0.565
# dtype: float64

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
# temperature_c           16.583
# fuel_price_usd_per_l     0.073
# unemployment             0.565
# dtype: float64

import numpy as np
# Custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))
#         temperature_c  fuel_price_usd_per_l  unemployment
# iqr            16.583                 0.073         0.565
# median         16.967                 0.743         8.099



# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date",ascending=[True])

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"]=sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
#          date  weekly_sales  cum_weekly_sales  cum_max_sales
# 0  2010-02-05      24924.50          24924.50       24924.50
# 1  2010-03-05      21827.90          46752.40       24924.50
# 2  2010-04-02      57258.43         104010.83       57258.43
# 3  2010-05-07      17413.94         121424.77       57258.43
# 4  2010-06-04      17558.09         138982.86       57258.43
# 5  2010-07-02      16333.14         155316.00       57258.43
# 6  2010-08-06      17508.41         172824.41       57258.43
# 7  2010-09-03      16241.78         189066.19       57258.43
# 8  2010-10-01      20094.19         209160.38       57258.43
# 9  2010-11-05      34238.88         243399.26       57258.43
# 10 2010-12-03      22517.56         265916.82       57258.43
# 11 2011-01-07      15984.24         281901.06       57258.43