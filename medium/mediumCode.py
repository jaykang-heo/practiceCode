from medium import mediumCodeTest

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    li =[]
    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            temp = array[i]+array[left]+array[right]
            if temp == targetSum:
                li.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif temp >targetSum:
                right-=1
            elif temp<targetSum:
                left+=1
    return li

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayTwo.sort()
    arrayOne.sort()
    id1,id2=0,0
    diff, cur=0,0
    pair= []
    while id1<len(arrayOne) and id2<len(arrayTwo):
        temp1 = arrayOne[id1]
        temp2= arrayTwo[id2]
        if temp1>temp2:
            cur = temp1-temp2
            id2+=1
        elif temp2>temp1:
            cur = temp2-temp1
            id1+=1
        else:
            return [temp1,temp2]
        if diff >cur:
            diff = cur
            pair= [temp1,temp2]
    return pair

def moveElementToEnd(array, toMove):
    # Write your code here.
    left=0
    right = len(array)-1
    while left<right:
        while left<right and array[right]==toMove:
            right-=1
        if array[left]==toMove:
            array[left],array[right]=array[right],array[left]
        right+=1
    return array

def isMonotonic(array):
    # Write your code here.
    increasing=True
    decreasing=False
    for i in range(1,len(array)):
        if array[i-1]<array[i]:
            increasing= True
        if array[i-1]>array[i]:
            decreasing=True
    return increasing or decreasing

def spiralTraverse(array):
    # Write your code here.
    res = []
    srow,erow=0,len(array)-1
    scol,ecol=0,len(array[0])-1
    while srow<=erow and scol<=scol:
        for col in range(scol,ecol+1):
            res.append(array[srow][col])
        for row in range(srow+1,erow+1):
            res.append(array[row][ecol])
        for col in reversed(range(scol+1,ecol+1)):
            if srow==erow:
                break
            res.append(array[erow][col])
        for row in reversed(range(srow,erow)):
            if scol==ecol:
                break
            res.append(array[row][scol])
        srow+=1
        erow-=1
        scol+=1
        ecol-=1
    return res

def longestPeak(array):
    # Write your code here.
    peak = 0
    i = 1
    while i < len(array)-1:
        ispeak = array[i-1] <array[i] and array[i] > array[i-1]
        if not ispeak:
            i+=1
            continue
        left = i-2
        while left >=0 and array[left] < array[left+1]:
            left-=1
        right=i+2
        while right <len(array) and array[right]>array[right-1]:
            right+=1
        temp = right-left-1
        peak = max(temp, peak)
        i = right
    return peak


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