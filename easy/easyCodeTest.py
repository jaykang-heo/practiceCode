from . import easyCode as code
from shutil import copyfile
import unittest

assert([1, 4]==code.twoNumberSum([4,6,1], 5) )
assert([6, 4]== code.twoNumberSum([4, 6], 10))
assert([-3, 6]== code.twoNumberSum([4, 6, 1, -3], 3))
assert([-1, 11]== code.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
assert([9, 8]== code.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
assert([15, 3]== code.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
assert([0, -5]== code.twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
assert([-47, 210]== code.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
assert([]== code.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
assert([]== code.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))
print('Two Number Sum Passed')

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
test = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
    .insert(-51)
    .insert(-403)
    .insert(1001)
    .insert(57)
    .insert(60)
    .insert(4500)
)

assert(code.findClosestValueInBst(test, 100)==100)
assert(code.findClosestValueInBst(test, 208)==208)
assert(code.findClosestValueInBst(test, 4500)==4500)
assert(code.findClosestValueInBst(test, 4501)==4500)
assert(code.findClosestValueInBst(test, -70)==-51)
assert(code.findClosestValueInBst(test, 2000)==1001)
assert(code.findClosestValueInBst(test, 30000)==55000)
assert(code.findClosestValueInBst(test, -1)==1)
assert(code.findClosestValueInBst(test, 29749)==4500)
print('find closest value in bst passed')

assert(code.getNthFib(1)==0)
assert(code.getNthFib(2)==1)
assert(code.getNthFib(3)==1)
assert(code.getNthFib(4)==2)
assert(code.getNthFib(5)==3)
assert(code.getNthFib(6)==5)
assert(code.getNthFib(7)==8)
assert(code.getNthFib(8)==13)
assert(code.getNthFib(9)==21)
assert(code.getNthFib(10)==34)
assert(code.getNthFib(11)==55)
assert(code.getNthFib(12)==89)
assert(code.getNthFib(13)==144)
assert(code.getNthFib(14)==233)
assert(code.getNthFib(15)==377)
assert(code.getNthFib(16)==610)
assert(code.getNthFib(17)==987)
assert(code.getNthFib(18)==1597)
print('get nth fib passed')

assert(code.productSum([1, 2, 3, 4, 5])==15)
assert(code.productSum([1, 2, [3], 4, 5])==18)
assert(code.productSum([[1, 2], 3, [4, 5]])==27)
assert(code.productSum([[[[[5]]]]])==600)
assert(code.productSum([
            9,
            [2, -3, 4],
            1,
            [1, 1, [1, 1, 1]],
            [[[[3, 4, 1]]], 8],
            [1, 2, 3, 4, 5, [6, 7], -7],
            [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
            [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]],
            -3,
        ])==1351)
assert(code.productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])==12)
print('product sum passed')

assert(code.binarySearch([1, 5, 23, 111], 111)==3)
assert(code.binarySearch([1, 5, 23, 111], 35)== -1)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)== 3)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72)== 8)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73)== 9)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70)== -1)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355)== 10)
assert(code.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354)== -1)
print('binary search passed')

assert(code.findThreeLargestNumbers([55, 7, 8])== [7, 8, 55])
assert(code.findThreeLargestNumbers([55, 43, 11, 3, -3, 10])== [11, 43, 55])
assert(code.findThreeLargestNumbers([7, 8, 3, 11, 43, 55])== [11, 43, 55])
assert(code.findThreeLargestNumbers([55, 7, 8, 3, 43, 11])== [11, 43, 55])
assert(code.findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])== [7, 7, 7])
assert(code.findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7])== [7, 7, 8])
assert(code.findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])== [18, 141, 541])
assert(code.findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7])== [-2, -1, 7])
print('find three largest numbers passed')

assert(code.bubbleSort([1])== [1])
assert(code.bubbleSort([1, 2])== [1, 2])
assert(code.bubbleSort([2, 1])== [1, 2])
assert(code.bubbleSort([1, 3, 2])== [1, 2, 3])
assert(code.bubbleSort([3, 1, 2])== [1, 2, 3])
assert(code.bubbleSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8])==
        [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10])
assert(code.bubbleSort([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])==
        [-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10])
assert(code.bubbleSort([8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4])==
        [-10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10])
print('bubble sort passed')

assert(code.insertionSort([1])== [1])
assert(code.insertionSort([1, 2])== [1, 2])
assert(code.insertionSort([2, 1])== [1, 2])
assert(code.insertionSort([1, 3, 2])== [1, 2, 3])
assert(code.insertionSort([3, 1, 2])== [1, 2, 3])
assert(code.insertionSort([1, 2, 3])== [1, 2, 3])
print('insertion sort passed')

assert(code.selectionSort([1])== [1])
assert(code.selectionSort([1, 2])== [1, 2])
assert(code.selectionSort([2, 1])== [1, 2])
assert(code.selectionSort([1, 3, 2])== [1, 2, 3])
print('selection sort passed')

assert(code.isPalindrome("a")== True)
assert(code.isPalindrome("ab")== False)
assert(code.isPalindrome("aba")== True)
assert(code.isPalindrome("abb")==False)
assert(code.isPalindrome("abba")== True)
assert(code.isPalindrome("abcdcba")== True)
assert(code.isPalindrome("abcdefghhgfedcba")== True)
print('is palindrome passed')

###############################################################################################
test1 = code.Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = code.Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = code.Node("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = code.Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")

test5 = code.Node("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")

assert(test1.depthFirstSearch([])==["A", "B", "D", "C"])
assert(test2.depthFirstSearch([])==["A", "B", "C", "F", "D", "E"])
assert(test3.depthFirstSearch([])==["A", "B", "C", "D", "F", "E"])
assert(test4.depthFirstSearch([])==["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
assert(test5.depthFirstSearch([])==
            [
                "A",
                "B",
                "E",
                "Q",
                "R",
                "F",
                "I",
                "J",
                "O",
                "C",
                "P",
                "D",
                "G",
                "K",
                "H",
                "L",
                "M",
                "S",
                "W",
                "X",
                "Y",
                "Z",
                "T",
                "U",
                "V",
            ])

import json
with open('keepTrack.json') as f:
    data = json.load(f)
    data['num'] += 1
    print('Congratulations! You Are Awesome!')
    print('Total Number For Easy Code', data['num'])
with open('keepTrack.json', 'w') as file:
    json.dump(data, file)
open('easyCode.py', 'w')
copyfile('easyCodeOriginal.py', 'easyCode.py')

