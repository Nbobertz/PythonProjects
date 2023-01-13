#The purpose of this is to take a large data file and demonstrate data anlysis using Python.
import pandas

color_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = color_data['Primary Fur Color']
#print(color['black'].count())
colors_seperated = color.value_counts()
print(colors_seperated)

colors_seperated.to_csv('Squirrel Colors')

