def fibonacci(number):
    if number==0:
        return 0
    if number==1:
        return 1
    if number>=2:
        return fibonacci(number-1)+fibonacci(number-2)
m=int(input("Enter the number upto which you want the Fibonacci Series"))
print("Fibonacci series upto {}".format(m))
for i in range(m):
    print(fibonacci(i))