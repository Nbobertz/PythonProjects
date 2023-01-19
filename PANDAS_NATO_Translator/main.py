import pandas as pd

#imports the CSV using pandas
alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
letter_list =[]

#this takes the capital letters from the CSV file and puts them into the letter_list list.
for (index,row) in alphabet.iterrows():
    letter = (row.letter)
    letter_list.append(letter)

#this does the same but for code column in the csv
code_list =[]
for (index,row) in alphabet.iterrows():
    code = (row.code)
    code_list.append(code)

#This zips the two lists into a dictionary where the key is the letter and the value is the code
code_dict = dict(zip(letter_list,code_list))

#this asks the user what word they would like to see in the phonetic alphabet
word = input("What word would you like to translate to the the phonetic alphabet\n").upper()

#this prints the phonetic alphabet to the console
for n in word:
    print(code_dict[n])