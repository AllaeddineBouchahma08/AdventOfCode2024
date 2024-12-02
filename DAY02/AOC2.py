with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

def is_good(numbers):
    inc_or_dec = (numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True))
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if not 1 <= diff <= 3:
            return False
    return inc_or_dec

SafeTotal = 0 
for line in lines:
    numbers = list(map(int, line.split()))  
    if is_good(numbers):  
        SafeTotal += 1
        print(numbers)  

print(SafeTotal)  
