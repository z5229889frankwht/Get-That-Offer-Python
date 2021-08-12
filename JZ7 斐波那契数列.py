# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n > 0:
            a, b = 1, 1
            for i in range(2, n):
                a, b = b, a + b
            return b
        else:
            return 0

    def Fibonacci_1(self, n):
        if n <= 0:
            return 0
        a = b = 1
        for i in range(2, n):
            a, b = b, a + b
        return b
