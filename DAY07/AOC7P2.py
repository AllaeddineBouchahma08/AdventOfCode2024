with open("input.txt", "r") as file:
    input_data = file.readlines()

def evaluate_expression_recursive(target, nums):
    if len(nums) == 1:
        return nums[0] == target
    if evaluate_expression_recursive(target, [nums[0] + nums[1]] + nums[2:]):
        return True
    if evaluate_expression_recursive(target, [nums[0] * nums[1]] + nums[2:]):
        return True
    if evaluate_expression_recursive(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:]):
        return True
    return False

def find_valid_equations_and_sum(input_data):
    total = 0
    for line in input_data:
        line = line.strip()
        target, numbers = line.split(':')
        target = int(target.strip())
        nums = list(map(int, numbers.strip().split()))
        if evaluate_expression_recursive(target, nums):
            total += target
    return total

result = find_valid_equations_and_sum(input_data)
print(result)
