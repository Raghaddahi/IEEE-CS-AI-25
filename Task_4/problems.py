def get_numbers():
    while True:
        try:
            nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
            if len(nums)<2:
                raise ValueError("You must enter at least two numbers")
            return nums
        except ValueError:
            print("Invalid input! Please enter a list of numbers separated by spaces.")
            return get_numbers()

def find_min(numbers):
    mini=numbers[0]
    for num in numbers:
        if num < mini:
            mini=num
    return mini

def find_max(numbers):
    maxi=numbers[0]
    for num in numbers:
        if num > maxi:
            maxi=num
    return maxi

def find_mean(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum/len(numbers)

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n%2==0:
        median1=sorted_numbers[n//2]
        median2=sorted_numbers[n//2-1]
        return (median1+median2)/2
    else:
        return sorted_numbers[n//2]


def find_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency.setdefault(num, 0)
        frequency[num] += 1
    highest_frequency = max(frequency.values())
    if list(frequency.values()).count(highest_frequency) == len(frequency):
        return "No mode, all numbers have the same frequency."
    mode_list = [num for num, freq in frequency.items() if freq == highest_frequency]
    return mode_list




def find_range(numbers):
    return find_max(numbers)-find_min(numbers)

def find_variance(numbers):
   mean=find_mean(numbers)
   sum=0
   for num in numbers:
       sum+=(num-mean) ** 2
   return sum/(len(numbers)-1)


def find_STD(numbers):
    return find_variance(numbers)**.5


def find_Quariles(numbers):
    sorted_numbers = sorted(numbers)
    n=len(numbers)
    if n % 2 == 1:
        lower_half = sorted_numbers[:n // 2]
        upper_half = sorted_numbers[n // 2 + 1:]
    else:
        lower_half = sorted_numbers[:n // 2]
        upper_half = sorted_numbers[n // 2:]
    Q2=find_median(sorted_numbers)
    Q1=find_median(lower_half)
    Q3=find_median(upper_half)
    return Q1, Q2, Q3

def find_IQR(numbers):
    Q1, Q2, Q3 = find_Quariles(numbers)
    return Q3 - Q1

numbers = get_numbers()
print("Min:", find_min(numbers))
print("Max:", find_max(numbers))
print("Mean:", find_mean(numbers))
print("Mode:", find_mode(numbers))
print("Median:", find_median(numbers))
print("Range:", find_range(numbers))
print("Variance:", find_variance(numbers))
print("Standard Deviation:", find_STD(numbers))
print("Quartiles:", find_Quariles(numbers))
print("Interquartile Range (IQR):", find_IQR(numbers))