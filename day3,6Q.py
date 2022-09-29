n=int(input("enter year:"))
if(n>0):
    if(n%4==0 or n%400==0):
        print("it is a leap year")
    else:
        print("it is not a leap year")
        if(n%4!=0):
            n-=int(n%4)
        print("leap year:",n)
else:
    print("not valid")
