print("enter the nth number")

rangenumber=int(input())
c=0
num=2
latest=0
while(c!=rangenumber):
    count=0
    for i in range(2,num):
        if(num%i==0):
            count+=1
            break
        if(count==0):
            c+=1
            latest=num
            num=num+1
            print(rangenumber,"th prime number is",latest)
