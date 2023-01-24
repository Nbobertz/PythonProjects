

#the following is a basic editing of the built in add function to take more then two arguments.

def add(*args):
    sum=0
    intr=0
    for n in args:
        intr = n
        sum+=intr
    print(sum)

add(1,2,3,4,50)

#now whenever you call the add function you can pass through a number of integers and it will pring the sum