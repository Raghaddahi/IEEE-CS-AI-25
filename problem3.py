total=0
num=int(input())
num=str(num)
for digit in  num:
    total+=int(digit)
print(f"The sum of digits is {total}",end="")
sum="+".join(num)
print(f"({sum})")


