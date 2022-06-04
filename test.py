def lcm(num1,num2):
    maximum=max(num1,num2)
    while(True):
        if maximum%num1==0 and maximum%num2==0:
            lcm=maximum
            break
        maximum=maximum+1
    return lcm 
number1=int(input("Enter the number1"))
number2=int(input("Enter the number2"))   
y=lcm(10,20)   
print("LCM of the {},{} is {}".format(number1,number2,y))     
  
