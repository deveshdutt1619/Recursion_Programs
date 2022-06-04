from math import factorial


def factorial(number):
        if number==0 or number==1:
            return 1
        else:
            return number*factorial(number-1) 
               
num=int(input("Enter the number whose factorial you want:\n"))
print("Factorial of {} is {}".format(num,factorial(num)))

    