from medium import mediumCodeTest

def threeNumberSum(array, targetSum):
    # Write your code here.
    pass

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    pass

def moveElementToEnd(array, toMove):
    # Write your code here.
    pass

def isMonotonic(array):
    # Write your code here.
    pass

def spiralTraverse(array):
    # Write your code here.
    # srow, erow = 0, len(array) - 1
    # scol,ecol=0,len(array[0])-1
    # res = []
    # while srow<=erow and scol<=ecol:
    #     for i in range(scol,ecol+1):
    #         res.append(array[srow][i])
    #     for i in range(srow+1,erow+1):
    #         res.append(array[i][ecol])
    #     for i in reversed(range(scol,ecol)):
    #         if srow==erow:
    #             break
    #         res.append(array[erow][i])
    #     for i in reversed(range(srow+1,erow)):
    #         if scol==ecol:
    #             break
    #         res.append(array[i][scol])
    # return res
    pass

def longestPeak(array):
    # Write your code here.
    # peak = 0
    # i=1
    # while i <len(array)-1:
    #     ispeak = array[i-1]<array[i] and array[i-1]>array[i]
    #     if not ispeak:
    #         i+=1
    #         continue
    #     left =i-2
    #     while left>=0 and array[left]<array[left+1]:
    #         left-=1
    #     right=i+2
    #     while right<len(array) and array[right-1]>array[right]:
    #         right+=1
    #     temp = right-left-1
    #     peak = max(peak,temp)
    #     i=right
    # return peak
    pass

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
    # queue=[tree]
    # while len(queue):
    #     cur = queue.pop(0)
    #     if cur is None:
    #         continue
    #     tree.left, tree.right = tree.right,tree.left
    #     queue.append(tree.left)
    #     queue.append(tree.right)
    pass

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    # if not len(array):
    #     return 0
    # elif len(array)==1:
    #     return array[0]
    # temp1 = array[0]
    # temp2 = max(array[0],array[1])
    # for i in range(2,len(array)):
    #     cur = max(temp1,temp1+array[i])
    #     temp1 = temp2
    #     temp2 = cur
    # return temp2
    pass

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for amount in range(len(n + 1))]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= denoms:
                ways[amount] += ways[amount - denom]
    return ways[n]
    pass

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    coins = [float('inf') for amount in range(n + 1)]
    coins[0] = 0
    for denom in denoms:
        for amount in range(len(coins)):
            if denom <= amount:
                coins[amount] = min(coins[amount], coins[amount - denom] - 1)
    return coins[n] if coins[0] != float('inf') else -1
    pass

def levenshteinDistance(str1, str2):
    # Write your code here.
    small = str1 if len(str1) < len(str2) else str2
    big = str2 if len(str2) > len(str1) else str1
    even = [x for x in range(len(small) + 1)]
    odd = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            cur = odd
            prev = even
        else:
            cur = even
            prev = odd
        cur[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = min(prev[j - 1], prev[j], cur[j - 1])
    return even[-1] if len(big) % 2 == 0 else odd[-1]
    pass

def kadanesAlgorithm(array):
    # Write your code here.
    temp1 = array[0]
    temp2 = array[0]
    for i in range(1, len(array)):
        num = array[i]
        temp1 = max(num, temp1 + num)
        temp2 = max(temp2, temp1)
    return temp2
    pass

def hasSingleCycle(array):
    # Write your code here.
    # num = 0
    # cur = 0
    # while num < len(array):
    #     if num >0 and cur ==0:
    #         return False
    #     num += 1
    #     jump = array[cur]
    #     nextnum = (cur+jump)%len(array)
    #     cur=nextnum if nextnum>=0 else nextnum+len(array)
    # return cur==0
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
        queue = [self]
        while len(queue) > 0:
            cur = queue.pop(0)
            array.append(cur.name)
            for child in cur.children:
                queue.append(child)
        return array
        pass

def riverSizes(matrix):
    # Write your code here.
    def traverseNode(i,j,matrix,visited,sizes):
        currentRiverSize = 0
        nodesToExplore = [[i,j]]
        while len(nodesToExplore):
            currentNode = nodesToExplore.pop()
            i= currentNode[0]
            j=currentNode[1]
            if visited[i][j]:
                continue
            visited[i][j] = True
            if matrix[i][j]==0:
                continue
            currentRiverSize +=1
            unvisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited)
            for neighbor in unvisitedNeighbors:
                nodesToExplore.append(neighbor)
        if currentRiverSize >0:
            sizes.append(currentRiverSize)

    def getUnvisitedNeighbors(i,j,matrix,visited):
        unvisitedNeighbors = []
        if i >0 and not visited[i-1][j]:
            unvisitedNeighbors.append([i-1,j])
        if i < len(matrix)-1 and not visited[i+1][j]:
            unvisitedNeighbors.append([i+1,j])
        if j> 0 and not visited[i][j-1]:
            unvisitedNeighbors.append([i,j-1])
        if j <len(matrix[0])-1 and not visited[i][j+1]:
            unvisitedNeighbors.append([i,j+1])
        return unvisitedNeighbors

    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,sizes)
    return sizes
    pass

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
        while diff >0:
            lowerDescendant = lowerDescendant.ancestor
            diff -=1
        while lowerDescendant != higherDescendant:
            lowerDescendant = lowerDescendant.ancestor
            higherDescendant = higherDescendant.ancestor
        return lowerDescendant

    def getDescendantDepth(descendant, topAncestor):
        depth = 0
        while descendant != topAncestor:
            depth +=1
            descendant = descendant.ancestor
        return depth

    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne >depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne-depthTwo)
    else:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthTwo-depthOne)
    pass

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    # Write your code here.
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
    pass

def getPermutations(array):
    # Write your code here.
    # def helper(i, array, permutation):
    #     if i == len(array) - 1:
    #         permutation.append(array[:])
    #     else:
    #         for j in range(i, len(array)):
    #             array[i], array[j] = array[j], array[i]
    #             helper(i + 1, array, permutation)
    #             array[i], array[j] = array[j], array[i]
    #
    # permutations = []
    # helper(0, array, permutations)
    # return permutations
    pass

def powerset(array):
    # Write your code here.
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets
    pass

def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]
    pass

def balancedBrackets(string):
    # Write your code here.
    openingBrackets = '([{'
    closingBrackets = ')]}'
    matchingBrackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
    pass

def longestPalindromicSubstring(string):
    # Write your code here.
    def getlongestpalindromefrom(string, leftidx, rightidx):
        while leftidx >= 0 and rightidx < len(string):
            if string[leftidx] != string[rightidx]:
                break
            leftidx -=1
            rightidx +=1
        return [leftidx+1,rightidx]
    currentLongest = [0,1]
    for i in range(1,len(string)):
        odd = getlongestpalindromefrom(string, i-1,i+1)
        even = getlongestpalindromefrom(string, i-1,i)
        longest = max(odd,even,key=lambda x:x[1]-x[0])
        currentLongest = max(longest, currentLongest, key=lambda x:x[1]-x[0])
    return string[currentLongest[0]:currentLongest[1]]
    pass

def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
    pass

mediumCodeTest