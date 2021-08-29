# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。。
# 解题思路： F(n) = 2 * F(n-1)

def jumpFloor_1(self, number):
    if number < 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    result = [1, 2]
    for i in range(2, number):
        result.append(2 * result[-1])
    return result[-1]