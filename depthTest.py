import json

with open("adjacent.txt") as json_file:
    tree = json.load(json_file)

path = []
# DFS algorithm in Python

# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    # path.append(start)
    # if (start == end):
    #     return

    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return visited


# graph = {'0': set(['1', '2', '3']),
#          '1': set(['0', '2']),
#          '2': set(['0', '2', '4']),
#          '3': set(['0']),
#          '4': set(['2'])}

dfs(tree, 'Cairo')
print(path)