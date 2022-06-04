def sum(list1,length):
        if length==0:
            return 0
        else:
            return list1[length-1] + sum(list1,length-1)

list2=[1,2,3,4,5]
length2=len(list2)
print(sum(list2,length2))