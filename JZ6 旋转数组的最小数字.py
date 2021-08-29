# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray:
            for i in range(len(rotateArray) - 1):
                if rotateArray[i] > rotateArray[i + 1]:
                    return rotateArray[i + 1]
                print(rotateArray[i])
            return rotateArray[0]
        else:
            return 0


class Solution_1:  # 二分法
    def minNumberInRotateArray_1(self, rotateArray):
        if not rotateArray:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid = (l + r) / 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            else:
                r = mid
        return rotateArray[l]
