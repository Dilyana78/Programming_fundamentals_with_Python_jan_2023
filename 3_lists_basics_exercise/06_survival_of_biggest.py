nums = [int(x) for x in input().split()]
count = int(input())
for i in range(count):
    min_num = min(nums)
    min_index = nums.index(min_num)
    nums.pop(min_index)

print(', '.join(str(item) for item in nums))

# 2 version
# numbers_str = input().split()
# numbers = []
# for num in numbers_str:
#     numbers.append(int(num))
# remover = int(input())
# for _ in range(remover):
#     numbers.remove(min(numbers))
# numbers_str_new = []
# for i in range(len(numbers)):
#     numbers_str_new.append(str(numbers[i]))
# print(", ".join(numbers_str_new))