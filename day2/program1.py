num=int(input("Enter the no "))
#odd/even
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")
 #prime
for x in range(2,9):
    if num%x==0:
        print(num,"is not prime")
        break
else:
        print(num,"is prime")
#palindrome
temp=num
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if(temp==rev):
    print(temp,"is palindrome")
else:
    print(temp,"is not palidrome")
#armstrong
sum=0;
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit ** 3
    temp=temp//10
if num== sum:
    print("It is armstrong")
else:
    print("It is not armstrong")
