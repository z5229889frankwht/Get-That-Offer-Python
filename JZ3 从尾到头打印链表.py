# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        #  方法一 使用栈的方式去实现
        arrayList = []
        while listNode:
            arrayList.append(listNode.val)
            listNode = listNode.next
        return arrayList[::-1]

        # 方法二 使用递归的方式去实现
        # if listNode:
        #     if listNode.next:
        #         self.printListFromTailToHead(listNode.next)
        #     self.arrayList.append(listNode.val)
        # return self.arrayList
