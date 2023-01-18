#The purpose of this file is to demonstrate a very 'pythonic' way of building out a for loop.
#it is possible to build and entire for loop in one line using Python. This is a pretty cool programing trick.


#Below I use one line of code to seperate out every character in a string using one line.
name = 'Nick is the one who created this program!'
letters_list = [letter for letter in name]
print(letters_list)


#below I seperate all names into short names and then call the .upper() function to uppercase them.
names = ['Alex', 'Beth', 'Caroline', 'Dave','Eleanor', 'Freddie']
short_names =[name.upper()for name in names if len(name)<5]
print(short_names)
long_names = [name.upper() for name in names if len(name)>5]
print(long_names)