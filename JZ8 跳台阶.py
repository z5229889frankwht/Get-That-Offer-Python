# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 解题思路： F(n) = F(n-1) + F(n-2)

def jumpFloor(self, number):
    # write code here
    # This question equals to Fibonacci Array
    if number == 1:
        return 1
    if number == 2:
        return 2
    res = [1, 1, 2]
    while len(res) <= number:
        res.append(res[-1] + res[-2])
    return res[-1]


def jumpFloor_1(self, number):
    if number < 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    result = [1, 2]
    for i in range(2, number):
        result.append(result[i - 1] + result[i - 2])
    return result[-1]
