# 描述
# 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 例如，9表示1001，因此输入9，输出2。

# 思路：如果整数不等于0，那么该整数的二进制表示中至少有1位是1。
#
# 先假设这个数的最右边一位是1，那么该数减去1后，最右边一位变成了0，其他位不变。
#
# 再假设最后一位不是1而是0，而最右边的1在第m位，那么该数减去1，
# 第m位变成0，m右边的位变成1，m之前的位不变。
#
# 上面两种情况总结，一个整数减去1，都是把最右边的1变成0，
# 如果它后面还有0，那么0变成1。
# 那么我们把一个整数减去1,与该整数做位运算，相当于把最右边的1变成了0，
# 比如1100与1011做位与运算，得到1000。
# 那么一个整数中有多少个1就可以做多少次这样的运算。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        if n > 0:
            return bin(n)[2:].count("1")
        if n < 0:
            return bin(n & 0xffffffff)[2:].count("1")

    def NumberOf1_1(self, n):
        # write code here
        count = 0
        while n:
            n = (n - 1) & n
            count = count + 1
        return count

    def NumberOf1_2(self, n):
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
        return count
