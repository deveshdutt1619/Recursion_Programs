def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
print("Enter the numbers to find GCD")    
number1=int(input("Enter the number1\n"))   
number2=int(input("Enter the number2\n"))
number3=int(input("Enter the number3\n"))
x=gcd(number1,gcd(number2,number3)) 
print("GCD of {},{},{} is {}".format(number1,number2,number3,x))
        