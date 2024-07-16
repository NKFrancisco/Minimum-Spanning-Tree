# Author: Nick Francisco
# CS 372 Intro to Computer Networks
# OSU Spring 2023
# Date: 6/6/2023

inputArr = [
 [0, 8, 5, 0, 0, 0, 0],
 [8, 0, 10, 2, 18, 0, 0],
 [5, 10, 0, 3, 0, 16, 0],
 [0, 2, 3, 0, 12, 30, 14],
 [0, 18, 0, 12, 0, 0, 4],
 [0, 0, 16, 30, 0, 0, 26],
 [0, 0, 0, 14, 4, 26, 0]
]

tsp = [
 [0, 2, 3, 20, 1],
 [2, 0, 15, 2, 20],
 [3, 15, 0, 20, 13],
 [20, 2, 20, 0, 9],
 [1, 20, 13, 9, 0],
]


def Prims(G):

    # Stores MST
    results = []

    # Number of vertices in graph
    vertices = len(G)

    # Array to track selected vertex
    selected = [0] * vertices

    # Track edges
    numEdges = 0

    # Start at first node
    # Set it to selected
    selected[0] = True

    # Loop until MST is created with vertices - 1 edges
    while numEdges < vertices - 1:
        minimum = float('inf')
        x = 0
        y = 0

        # Loop through all vertices
        for i in range(vertices):
            # Check connected vertices
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and G[i][j]:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j

        # Add to results
        results.append((x, y, minimum))
        selected[y] = True
        numEdges += 1

    return results


print(Prims(inputArr))
# print(Prims(tsp))
