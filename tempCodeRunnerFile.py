for i in range(5):
    for j in range(5):
         print("*" ,end=" ")
    print()




for i in range(1,6):
    print(" "*(5-i),end=" ")
print(" * "*i)




for i in range(3):
    for j in range(3):
         print("*", end=" ")
    print()


for i in range(1, 4):
    print("*" * i)

for i in range(3, 0, -1):
    print("*" * i)


for i in range(1, 6):
    print(i)


for i in range(1, 6):
    print(i, end=" ")

for i in range(1, 4):
    print(i, i, i)



 
num=1
while num<=10:
    print(num)
    num+=1

num=2
while num<=16:
    print(num)
    num+=2

num=1
sum=0
while num<=5:
    sum+=num
    num+=1
    print("sum=", sum)    
num=121
temp=num
rev=0
while num >0:
    digit=num%10
    rev=rev*10+digit
    num//=10
    if temp==rev:
        print("palindrone")
else:
    print("Not palindrome")
num=12345
count=0
while num>0:
    num//=10
    count+=1
    print("Digits:",count)
num=5
fact=1
i=1
while i <=num:
    fact*=i
    i+=1
    print("Factorial:",fact)
num=5
i=1
while i <=10:
    print(num,"x",i,i,"=",num*1)
    i+=1