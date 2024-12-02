with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

def is_good(number):
    inc_or_dec = (number == sorted(number) or number == sorted(number, reverse=True))
    for i in range(len(number) - 1):
        diff = abs(number[i] - number[i + 1])
        if not 1 <= diff <= 3:
            return False
    return inc_or_dec
def can_be_good(number):
    for i in range(len(number)):
        if is_good(number[:i] + number[i + 1:]):
            return True


SafeTotal = 0  
for line in lines:
    numbers = list(map(int, line.split()))
    if can_be_good(numbers):  
        SafeTotal += 1
        print(numbers) 

print(SafeTotal)  
