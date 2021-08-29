# 1. 矩阵顺时针旋转
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

matrix = [[1,2],[3,4]]

print(matrix)
# print(matrix[::-1])
res = []
for line in zip(*matrix):
    # print(list(line))
    res.append(list(line))
print(res)

# 2. Top K Frequent Elements
# 给定的数组
nums = [1, 1, 1, 2, 3]
k = 2
dict = {}
result = []
for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1
for i in range(k):
    m = max(dict, key=dict.get)
    result.append(m)
    del dict[m]
print()
print(nums, k)
print(result)
