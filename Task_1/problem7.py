num=int(input())
prime_factors=[]
for i in range(2,num+1):
    if num%i==0:
        while num% i == 0:
            num//= i
        prime_factors.append(i)
print("Prime factors: ")
i = 0
while i < len(prime_factors)-1:
    print(f"{prime_factors[i]},", end=" ")
    i += 1
print(prime_factors[i])

