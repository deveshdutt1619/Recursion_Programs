Reverse = 0
def Reverse_Integer(Number):
    global Reverse
    if(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Reverse_Integer(Number //10)
    return Reverse 

if __name__=='__main__':
    Number = int(input("Enter any Number: "))
    Reverse = Reverse_Integer(Number)
    print("Reverse of entered number is = %d" %Reverse) 