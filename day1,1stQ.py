reg=int(input("enter the NO.of loaves purchased"))
old=int(input("enter the no.of old bread purchased"))
e=185
r=185*reg
d=0.6*185*reg
a=r+d
if(reg<0 or old <0):
   print("invalid input")
print("regular price",e)
print("amount of purchase loaves",r)
print("amount of purchase old bread",d)
print("total amount",a)
