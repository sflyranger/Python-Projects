# This script shows different examples of how to create arrays and how to use simple statistics on those arrays.
# It also has some more advanced methods of statistics.
# Data is not included just examples.


# Creating an array that allows for array calculations through numpy
np_baseball = np.array(baseball)
# Calculating mean, median, standard deviation and correlation coefficient of arrays.
# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. 0 here refers to the first column
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. 0 here refers to the first column
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. 0 here refers to the first column 1 refers to the second. Two column arguments are needed.
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)


# Heights of the goalkeepers: gk_heights, specific position designation in array.
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
# Show plot
plt.show()

Help on function hist in module
matplotlib.pyplot:hist(x, bins=None, range=None, density=False, weights=None, cumulative=False,
                       bottom=None, histtype='bar', align='mid', orientation='vertical',
                       rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)
Plot a histogram.
Compute and draw the histogram of *x*.
The return value is a
tuple (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...],     *bins*, [*patches0*, *patches1*, ...])
if the input contains     multiple data.

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins

plt.hist(life_exp, bins=20)
# Show and clean up again
plt.show()
plt.clf()


# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop= np.array(pop)

# Double np_pop
np_pop= np_pop* 2

# Update: set s argument to np_pop,s here refers to sizing based on np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


# Specify c and alpha inside plt.scatter(), here c refers to how color is designated and alpha refers to the
# transparency of the bubbles inside the scatter
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c= col, alpha= 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call, indicating that gridlines will be shown in the scatter.
plt.grid(True)

# Show the plot
plt.show()


# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy']= 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland']= 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']= 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')
# change first column to index
cars= pd.read_csv('cars.csv', index_col=0)
# Print out cars
print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series, includes dtype and name as a row.
print(cars['country'])

# Print out country column as Pandas DataFrame, this removes name and dtype rows.
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations, iloc is based on integer relationships, loc can be used to call
# specific rows by name.
print(cars.iloc[[0,1,2]])

# Print out fourth, fifth and sixth observation, iloc is based on integer relationships, loc can be used to call
# specific rows by name.
print(cars.iloc[[3,4,5]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
#Using print to inspect name of row for loc.
print(cars)
# Print out observation for Japan, uses cars.loc for name specific
print(cars.loc[['JPN']])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG' ]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right value of Morocco
print(cars.loc[['MOR'],['drives_right']])

# Print sub-DataFrame with country and drives_right status for Russia and Morocco only.
#First set of square brackets designates row, second designates the column names selected. Could use iloc with integer notation
print(cars.loc[['RU','MOR'],['country', 'drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(cars.iloc[:,2])

# Print out drives_right column as DataFrame
print(cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])

# Comparison of booleans
True == False

# Comparison of integers
-5*15!= 75

# Comparison of strings
'pyscript'=='PyScript'

# Compare a boolean with an integer
True == 1

# Comparison of integers
x = -3 * 6
print(x>= -10)

# Comparison of strings
y = "test"
print('test'<= y)

# Comparison of booleans
print(True > False)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
[ True  True False False] #response from python
[False  True  True False] #

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen> 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen < 3*your_kitchen)
False
True
True

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or( my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and( my_house <11, your_house < 11))
[False  True False  True]
[False False False  True]

#IF, ELSE and ELIF

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if(area>15):
    print('big place!')
looking around in the kitchen. #output

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area, notice spacing needs to be correct otherwise there will be an error message in the output.
if area > 15 :
    print("big place!")
else:
    print('pretty small')
looking around in the kitchen.
pretty small


# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area, notice where the semi colons are located in the elif and if statements.
if area > 15 :
    print("big place!")
elif area > 10:
    print('medium size, nice!')
else :
    print("pretty small.")
looking around in the bedroom.
medium size, nice!
