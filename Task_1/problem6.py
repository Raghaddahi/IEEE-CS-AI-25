total=0
num=int(input())
for i in range(1,num):
    if num%i==0:
        total+=i
if total==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
