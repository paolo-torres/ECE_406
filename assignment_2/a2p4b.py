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

def getMinDistance(distance, visited, graphSize):
    minValue = float('inf')
    minIndex = 0

    for i in range(graphSize):
        if distance[i] <= minValue and visited[i] == False:
            minValue = distance[i]
            minIndex = i
    
    return minIndex

def updateDistance(G, u, v, distance, visited):
    if (G[u][v]
        and distance[u] != float('inf')
        and distance[G[u][v][0]] > distance[u] + G[u][v][1]
        and visited[v] == False):
        distance[G[u][v][0]] = distance[u] + G[u][v][1]

def nshortestpaths(G, a, b):
    # vertex: [other vertex, edge weight]
    # a = 0, b = 1, c = 2, d = 3
    # a: [[1, 2], [3, 1]]
    # b: [[0, 2], [3, 1], [2, 2]]
    # c: [[1, 2]]
    # d: [[1, 1], [0, 1]]

    graphSize = len(G)

    adjacencyOrder = []
    adjacencyIndex = []
    adjacencyValue = []

    distance = []
    visited = []

    for i in range(graphSize):
        distance.append(float('inf'))
        visited.append(False)
    
    distance[a] = 0

    for i in range(graphSize):
        u = getMinDistance(distance, visited, graphSize)
        
        adjacencyOrder.append(u)

        adjacentIndex = []
        adjacentValue = []

        for v in range(len(G[u])):
            adjacentIndex.append(G[u][v][0])
            adjacentValue.append(G[u][v][1])
            updateDistance(G, u, v, distance, visited)

        adjacencyIndex.append(adjacentIndex)
        adjacencyValue.append(adjacentValue)
        visited[u] = True

    print(distance)
    print(adjacencyOrder)
    print(adjacencyIndex)
    print(adjacencyValue)

    targetDistance = distance[b]
    print(targetDistance)
    currentDistance = 0

    paths = 0
    
    return paths
