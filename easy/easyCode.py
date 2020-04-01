from easy import easyCodeTest


def twoNumberSum(array, targetSum):
    # Write your code here.
    res = {}
    for i in array:
        temp = targetSum - i
        if temp in res:
            return [i, temp]
        else:
            res[i] = True
    return []

def findClosestValueInBst(tree, target):
    # Write your code here.
    def helper(node, target, num):
        while node is not None:
            if abs(target-num) > abs(target-node.value):
                num= node.value
            if target > node.value:
                node = node.right
            elif target < node.value:
                node = node.left
            else:
                break
        return num
    return helper(tree, target, float('inf'))

def getNthFib(n):
    # Write your code here.
    last =[0,1]
    count =3
    while count <=n:
        fib = last[1]+last[0]
        last[0] = last[1]
        last[1] = fib
        count+=1
    return last[1] if n> 1 else last[0]

def productSum(array, multiplier=1):
    # Write your code here.
    sum = 0
    for i in array:
        if type(i) is list:
           sum += productSum(i, multiplier+1)
        else:
            sum+= i
    return sum*multiplier

def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        temp = array[mid]
        if temp == target:
            return mid
        elif temp < target:
            left+=1
        elif temp > target:
            right -=1
    return -1

def findThreeLargestNumbers(array):
    # Write your code here.
    def shift(arr, idx, num):
        for i in range(idx+1):
            if i == idx:
                arr[i] = num
            else:
                arr[i] = arr[i+1]
    def update(arr, num):
        if arr[2] is None or num > arr[2]:
            shift(arr, 2, num)
        elif arr[1] is None or num > arr[1]:
            shift(arr,1, num)
        elif arr[0] is None or num > arr[0]:
            shift(arr, 0, num)

    threeLarge = [None, None, None]
    for i in array:
        update(threeLarge, i)
    return threeLarge

def bubbleSort(array):
    # Write your code here.

    pass

def insertionSort(array):
    # Write your code here.
    pass

def selectionSort(array):
    # Write your code here.
    pass

def isPalindrome(string):
    # Write your code here.
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left +=1
        right -=1
    return True

def caesarCipherEncryptor(string, key):
    # Write your code here.
    pass

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # Write your code here.
    sums = []
    def helper(node, sums, cur):
        if node is None:
            return
        total = node.value + cur
        if node.left is None and node.right is None:
            sums.append(total)
        helper(node.left, sums, total)
        helper(node.right, sums, total)
    helper(root, sums, 0)
    return sums

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for i in array:
            i.depthFirstSearch(array)
        pass

easyCodeTest