nums = [int(x) for x in input().split()]
count = int(input())
for i in range(count):
    min_num = min(nums)
    min_index = nums.index(min_num)
    nums.pop(min_index)

print(', '.join(str(item) for item in nums))