array = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]

target = 3
flag = 0

# 暴力搜索 时间复杂度O(n^2) 空间复杂度O(1)
if array:
    rows, cols = len(array), len(array[0])
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == target:
                flag = 1
                break
    if flag == 0:
        print(f"False")
    else:
        print(f"True")
else:
    print(f"False")

# 二分查找法
