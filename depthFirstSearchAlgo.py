import json
# from ai import tree
from getCityNeighboursLatLng import getPathCitiesLatLng

def depthFirstSearchAlgo(country = "egypt", startCity = "Sakha", endCity = "Giza"):
    # adjacent list
    with open("adjacent.txt") as json_file:
        tree = json.load(json_file)

    # algorithim
    stack = []
    visited = {}
    dfs__traversed_output = []
    for node in tree.keys():
        visited[node] = False
    startNode = startCity
    stack.append(startNode)

    while(len(stack) > 0):
        node = stack.pop()
        if(not visited[node]):
            visited[node] = True
            dfs__traversed_output.append(node)
            if node == endCity:
                break
            for unvisitedNeighbourNode in tree[node]:
                stack.append(unvisitedNeighbourNode)
    path =  getPathCitiesLatLng(dfs__traversed_output)
    path.reverse()
    return path

if __name__ == '__main__':
    pass
