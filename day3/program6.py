def sum(List,size,sum):
    sumList =[]
    if size ==1:
        for x in list:
            sumList.append(sum+x)
        return sumList
    L2=list(List)
    for x in List:
        L2.remove(x)
        sumList.extend(sum(L2,size-1,sum + x))
    return sumList

def summation(List,size):
    sumList = list(List)
    for x in range(2,size + 1):
        sumList.extend(sum(List,x,0))
    number=1
    while True:
        if number not in sumList:
            print("The least integer which is not present in list and also cannot be represented  as the sum of sub elements of list is:",number)
            break
            number+=1
            
        num=int(input("Enter size of list: "))
        List = []
        print("Enter list elements: ")
        for x in range(0,num):
            List.append(int(input()))
            summation(List,num)
