"""
ECE406, W'21, Assignment 2, Problem 4(b) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""

def getMinDistance(distances, visited, graphSize):
    minValue = float('inf')
    minIndex = 0

    for i in range(graphSize):
        if distances[i] <= minValue and visited[i] == False:
            minValue = distances[i]
            minIndex = i
    
    return minIndex

def updateDistance(G, u, v, distances, visited):
    index = G[u][v][0]
    value = G[u][v][1]

    if (distances[u] != float('inf')
        and distances[index] > distances[u] + value
        and visited[index] == False):
        distances[index] = distances[u] + value

def getShortestPaths(G, distances, visited, graphSize):
    for i in range(graphSize):
        u = getMinDistance(distances, visited, graphSize)
        visited[u] = True

        for v in range(len(G[u])):
            updateDistance(G, u, v, distances, visited)

def existsInPath(curPath, vertex):
    for i in curPath:
        if vertex == i:
            return True
    return False

def traverse(G, src, cur, target, curDist, targetDist, curPath, numPaths):
    if cur == target:
        if curDist == targetDist:
            numPaths[0] = numPaths[0] + 1
        return
    
    for i in range(len(G[cur])):
        index = G[cur][i][0]
        value = G[cur][i][1]

        if G[cur][i][0] == src or existsInPath(curPath, index):
            continue

        curDist = curDist + value
        curPath.append(index)

        traverse(G, src, index, target, curDist, targetDist, curPath, numPaths)
        
        curDist = curDist - value
        curPath.pop()

def nshortestpaths(G, a, b):
    """
    You need to implement this method.

    You are certainly allowed to define any subroutines you want
    above this method in this file.

    We will test with inputs that match the spec only --- G will
    be a non-empty graph, i.e., at least one vertex, and a, b will
    be distinct valid vertices in G --- so that means G will have at
    least 2 vertices. Of course within those constraints, we could test
    for corner cases. E.g., a graph of no edges, e.g., G = [[],[],[]]
    """

    graphSize = len(G)

    distances = []
    visited = []

    for i in range(graphSize):
        distances.append(float('inf'))
        visited.append(False)
    
    distances[a] = 0
    
    getShortestPaths(G, distances, visited, graphSize)

    curDist = 0
    targetDist = distances[b]

    curPath = []
    curPath.append(a)

    numPaths = []
    numPaths.append(0)

    traverse(G, a, a, b, curDist, targetDist, curPath, numPaths)
    
    return numPaths[0]
