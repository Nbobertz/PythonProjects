import random

def howlong():
    year = random.randint(1,50)
    money = random.randint(1,10)
    print(f"You have {year} years left unti you retire!!!")
    print(f"Your net worth when you retire is going to be {money} million")
    salary = round((money/year) * 1000000)
    print(f'This means that you are going to make ${salary} per year until you retire')
howlong()