from . import mediumCodeTest

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left=i+2
        right =len(array)-1
        while left < right:
            total = array[i]+array[left]+array[right]
            if total ==targetSum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif total < targetSum:
                left+=1
            elif total>targetSum:
                right-=1
    return triplets

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    id1 =0
    id2=0
    small = float('inf')
    cur = float('inf')
    smallestpair = []
    while id1 < len(arrayOne) and id2<len(arrayTwo):
        first = arrayOne[id1]
        second = arrayTwo[id2]
        if first < second:
            cur = second - first
            id1 += 1
        elif second < first:
            cur = first - second
            id2 +=2
        else:
            return [first, second]
        if small > cur:
            small = cur
            smallestpair = [first,second]
    return smallestpair


    pass
def moveElementToEnd(array, toMove):
    # Write your code here.
    pass
def isMonotonic(array):
    # Write your code here.
    pass
def spiralTraverse(matrix):
    # Write your code here.
    pass
def longestPeak(array):
    # Write your code here.
    pass
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

def inOrderTraverse(tree, array):
    # Write your code here.
    pass


def preOrderTraverse(tree, array):
    # Write your code here.
    pass


def postOrderTraverse(tree, array):
    # Write your code here.
    pass
def invertBinaryTree(tree):
    # Write your code here.
    pass
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    pass
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    pass
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    pass
def levenshteinDistance(str1, str2):
    # Write your code here.
    pass
def kadanesAlgorithm(array):
    # Write your code here.
    pass
def hasSingleCycle(array):
    # Write your code here.
    pass
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        pass
def riverSizes(matrix):
    # Write your code here.
    pass
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    pass
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        pass

    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self):
        # Write your code here.
        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        # Write your code here.
        pass
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    pass
def getPermutations(array):
    # Write your code here.
    pass
def powerset(array):
    # Write your code here.
    pass
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    pass
class MinMaxStack:
    def peek(self):
        # Write your code here.
        pass

    def pop(self):
        # Write your code here.
        pass

    def push(self, number):
        # Write your code here.
        pass

    def getMin(self):
        # Write your code here.
        pass

    def getMax(self):
        # Write your code here.
        pass
def balancedBrackets(string):
    # Write your code here.
    pass
def longestPalindromicSubstring(string):
    # Write your code here.
    pass
def groupAnagrams(words):
    # Write your code here.
    pass
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        pass

    def contains(self, string):
        # Write your code here.
        pass

mediumCodeTest