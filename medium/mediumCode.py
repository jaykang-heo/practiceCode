from medium import mediumCodeTest


def levenshteinDistance(str1, str2):
    # Write your code here.
    # small = str1 if len(str1) <len(str2) else str2
    # big = str2 if len(str2)>len(str1) else str1
    # even = [x for x in range(len(small)+1)]
    # odd = [None for x in range(len(small)+1)]
    # for i in range(1,len(big)+1):
    #     if i%2==1:
    #         cur = odd
    #         prev = even
    #     else:
    #         cur = even
    #         prev = odd
    #     cur[0]=i
    #     for j in range(1,len(small)+1):
    #         if big[i-1]==small[j-1]:
    #             cur[j]=prev[j-1]
    #         else:
    #             cur[j] = min(prev[j-1],prev[j],cur[j-1])
    # return even[-1] if len(big)%2==0 else odd[-1]
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


def getPermutations(array):
    # Write your code here.
    # def helper(i, array, permutation):
    #     if i==len(array)-1:
    #         permutation.append(array[:])
    #     else:
    #         for j in range(i,len(array)):
    #             array[i],array[j] = array[j],array[i]
    #             helper(i+1,array,permutation)
    #             array[i],array[j] = array[j],array[i]
    # permutations = []
    # helper(0, array, permutations)
    # return permutations
    def helper(i, array, permutation):
        if i ==len(array)-1:
            permutation.append(array[:])
        else:
            for j in range(i,len(array)):
                array[i],array[j]=array[j],array[i]
                helper(i+1,array,permutation)
                array[i],array[j]=array[j],array[i]
    permutation = []
    helper(0,array,permutation)
    return permutation
    pass

def powerset(array):
    # Write your code here.
    # subsets = [[]]
    # for ele in array:
    #     for i in range(len(subsets)):
    #         currentSubset = subsets[i]
    #         subsets.append(currentSubset+[ele])
    # return subsets

    subsets = [[]]
    for ele in array:
        for j in range(len(subsets)):
            cur = subsets[j]
            subsets.append(cur+[ele])
    return subsets
    pass


def longestPalindromicSubstring(string):
    # Write your code here.
    # def getlongestpalindromefrom(string, leftidx, rightidx):
    #     while leftidx >= 0 and rightidx < len(string):
    #         if string[leftidx] != string[rightidx]:
    #             break
    #         leftidx -=1
    #         rightidx +=1
    #     return [leftidx+1,rightidx]
    # currentLongest = [0,1]
    # for i in range(1,len(string)):
    #     odd = getlongestpalindromefrom(string, i-1,i+1)
    #     even = getlongestpalindromefrom(string, i-1,i)
    #     longest = max(odd,even,key=lambda x:x[1]-x[0])
    #     currentLongest = max(longest, currentLongest, key=lambda x:x[1]-x[0])
    # return string[currentLongest[0]:currentLongest[1]]

    def helper(string, left, right):
        while left >=0 and right < len(string):
            if string[left] != string[right]:
                break
            left -=1
            right +=1
        return [left+1, right]
    cur = [0,1]
    for i in range(1,len(string)):
        odd = helper(string,i-1,i+1)
        even = helper(string, i-1,i)
        long = max(odd, even , key=lambda x:x[1]-x[0])
        cur = max(long, cur, key=lambda x:x[1]-x[0])
    return string[cur[0]:cur[1]]
    pass


mediumCodeTest
