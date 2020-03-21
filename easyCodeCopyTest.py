import easyCodeCopy as code
from shutil import copyfile
import os 
import unittest

assert([1, 4] == code.twoNumberSum([4,6,1], 5))
assert([6, 4]== code.twoNumberSum([4, 6], 10))
assert([-3, 6]== code.twoNumberSum([4, 6, 1, -3], 3))
assert([-1, 11]== code.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
assert([9, 8]== code.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
assert([15, 3]== code.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
assert([0, -5]== code.twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
assert([-47, 210]== code.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
assert([]== code.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
assert([]== code.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))

###############################################################################################
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

###############################################################################################
class BinaryTree(code.BinaryTree):    
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

assert(code.branchSums(BinaryTree(1))==[1])
assert(code.branchSums(BinaryTree(1).insert([2]))==[3])
assert(code.branchSums(BinaryTree(1).insert([2, 3]))==[3, 4])
assert(code.branchSums(BinaryTree(1).insert([2, 3, 4, 5]))==[7, 8, 4])
assert(code.branchSums(BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10]))==[15, 16, 18, 10, 11])
assert(code.branchSums(BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1]))==[15, 16, 18, 9, 11, 11, 11])
tree = BinaryTree(0)
tree.left = BinaryTree(1)
tree.left.left = BinaryTree(10)
tree.left.left.left = BinaryTree(100)
assert(code.branchSums(tree)==[111])
tree = BinaryTree(0)
tree.right = BinaryTree(1)
tree.right.right = BinaryTree(10)
tree.right.right.right = BinaryTree(100)
assert(code.branchSums(tree)==[111])
tree = BinaryTree(0)
tree.left = BinaryTree(9)
tree.right = BinaryTree(1)
tree.right.left = BinaryTree(15)
tree.right.right = BinaryTree(10)
tree.right.right.left = BinaryTree(100)
tree.right.right.right = BinaryTree(200)
assert(code.branchSums(tree)==[9, 16, 111, 211])

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

def test12(self):
    print('hello')
    self.assertEqual(test1.depthFirstSearch([]), ["A", "B", "D", "C"])
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

###############################################################################################
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

###############################################################################################
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




open('/home/jay/Desktop/practiceCode/easyCodeCopy1.py', 'w')
copyfile('/home/jay/Desktop/practiceCode/easyCode.py', '/home/jay/Desktop/practiceCode/easyCodeCopy1.py')