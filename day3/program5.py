n1=int(input("Enter size of list1:"))
n2=int(input("Enter size of list2:"))
List1=[]
List2=[]
print("enter elements of list1:")
for x in range(0,n1):
    List1.append(input())
print("Enter elements of list2:")
for x in range(0,n2):
    List2.append(input())
new_list=[]
for x in List1:
    for y in List2:
        if x==y:
            new_list.append(x)
print("Intersection of two lists are:",new_list)
