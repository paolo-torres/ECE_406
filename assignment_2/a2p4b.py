"""
ECE406, W'21, Assignment 2, Problem 4(b) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""

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

def getMinDistance(distances, visited, graphSize):
    minValue = float('inf')
    minIndex = 0

    for i in range(graphSize):
        if distances[i] <= minValue and visited[i] == False:
            minValue = distances[i]
            minIndex = i
    
    return minIndex

def updateDistance(G, u, v, distances, visited):
    if (G[u][v]
        and distances[u] != float('inf')
        and distances[G[u][v][0]] > distances[u] + G[u][v][1]
        and visited[G[u][v][0]] == False):
        distances[G[u][v][0]] = distances[u] + G[u][v][1]

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
        if G[cur][i][0] == src or existsInPath(curPath, G[cur][i][0]):
            continue

        curDist = curDist + G[cur][i][1]
        curPath.append(G[cur][i][0])

        traverse(G, src, G[cur][i][0], target, curDist, targetDist, curPath, numPaths)
        
        curDist = curDist - G[cur][i][1]
        curPath.pop()

def nshortestpaths(G, a, b):
    # vertex: [other vertex, edge weight]
    # a = 0, b = 1, c = 2, d = 3, e = 4
    # a: [1, 4],[2, 2]
    # b: [0, 4],[2, 1],[3, 2],[4, 3]
    # c: [0, 2],[1, 1],[4, 5],[3, 4]
    # d: [1, 2],[2, 4],[4, 1]
    # e: [1, 3],[3, 1],[2, 5]

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
