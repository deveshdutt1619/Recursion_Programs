def toi(discs,origin,target,auxilliary):
    if discs==1:
        print("Disc moved from {} to {}".format(origin,target))
    else:
        toi(discs-1,origin,auxilliary,target)
        print("Moving one disc from {} to {}".format(origin,target))
        toi(discs-1,auxilliary,target,origin)



if __name__=='__main__':
    discs=int(input("Enter the number of discs"))
    A=input("Enter the name of origin tower:")
    B=input("Enter the name of origin tower:")
    C=input("Enter the name of origin tower:")
    print("The sequences involved in the Tower of Hanoi are:")
    toi(discs,A,B,C)
