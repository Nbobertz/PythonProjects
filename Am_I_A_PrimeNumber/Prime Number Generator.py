
def prime_checker(number):
  pstatus = True
  for i in range(2,number):
    if number % i == 0:
      pstatus = False
  if pstatus == True:
    print("this number is prime")
  else:
    print("This number is not prime")

n = int(input("Check to see if this number is a prime number: "))
prime_checker(number=n)



