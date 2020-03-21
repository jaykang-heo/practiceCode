import easyCodeCopyTest

def twoNumberSum(array, targetSum):
    # Write your code here.
    res = {}
    for i in array:
        target = targetSum - i
        if target in res:
            return [i, target]
        else:
            res[i] = True
    return []


def findClosestValueInBst(tree, target):
    # Write your code here.
    def helper(tree, target, closest):
        currentNode = tree
        while currentNode is not None:
            if abs(target-closest) > abs(target-currentNode.value):
                closest = currentNode.value
            if target < currentNode.value:
                currentNode = currentNode.left
            elif target > currentNode.value:
                currentNode = currentNode.right
            else:
                break
        return closest
    return helper(tree, target, float('inf'))

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # Write your code here.
    sums = []
    def helper(node, runningSum, sums):
        if node is None:
            return 
        newRunningSum = runningSum + node.value
        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return 
        helper(node.left, newRunningSum, sums)
        helper(node.right, newRunningSum, sums)
        
    helper(root, 0, sums)
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
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# This is an input class. Do not edit.
class Node1:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return 
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next 
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next 
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

def getNthFib(n):
    # Write your code here.
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n>1 else lastTwo[0]

def productSum(array, multiplier=1):
    # Write your code here.
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

def binarySearch(array, target):
    # Write your code here.
    def helper(array, target, left, right):
        while left <= right:
            middle = (left + right)//2
            potentialMatch = array[middle]
            if target == potentialMatch:
                return middle
            elif target < potentialMatch:
                right = middle -1
            else:
                left = middle + 1
        return -1
    return helper(array, target, 0, len(array)-1)

def findThreeLargestNumbers(array):
    # Write your code here.
    pass

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
    pass

def caesarCipherEncryptor(string, key):
    # Write your code here.
    pass

easyCodeCopyTest