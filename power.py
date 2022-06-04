def power(number,exp):
    sum=number
    for i in range(1,exp):
        sum=sum*number
    print("{} power {} is {}".format(number,exp,sum))  

num=int(input("Enter the number:"))
exponent=int(input("Power?"))
power(num,exponent)
