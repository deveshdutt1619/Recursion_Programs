def fibosum(number):
    if number==0:
        return 0
    if number==1:
        return 1
    else:
        return fibosum(number-2)+fibosum(number-1) 

num=int(input("Enter the number"))
sum=0
for i in range(num):        
    sum=sum+fibosum(i)
print("Sum of the FIbonacci Series upto {} is {}".format(num,sum))