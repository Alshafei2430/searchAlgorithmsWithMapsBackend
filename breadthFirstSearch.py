from getCityNeighboursLatLng import getPathCitiesLatLng



def make_visited_false(tree):
    """
    Makes values of all cities to false in visited dictionary
    tree: treeacent dictionary
    returns nothing
    """
    visited={}
    for city in tree:
        visited[city]=False
    return visited

def BFS(initial_state, goal_state):
    """
    Applys breadth first search algorithm to the given graph
    initial_state: is the start city
    goal_state: the city the user want to reach
    """
    parent = {}
    queue = []

    # with open("adjacent.txt") as json_file:
    #     tree = json.load(json_file)
    from ai import tree
    visited = make_visited_false(tree)
    visited[initial_state] = True
    queue.append(initial_state)


    while queue:
        city = queue.pop(0)

        for neighbour in tree[city]:
            if visited[neighbour] == False:
                visited[neighbour] = True
                parent[neighbour] = city

                queue.append(neighbour)
                if neighbour == goal_state:
                    return parent
    




def get_path(initial_state = 'Al Husayniyah', goal_state = 'Halwan'):
    """
    Takes two cities and returns the route between the chosen cities
    initial_state: is the start city
    goal_state: the city the user want to reach

    """
    path = []
    parent =  BFS(initial_state, goal_state)

    while goal_state != initial_state:
        path.append(goal_state)
        goal_state = parent[goal_state]
    path.reverse()
    path = [initial_state] + path
     
    return getPathCitiesLatLng(path)


def algorithm_path(initial_state, goal_state, algorithm):
    """
    Takes the algorithm the user needs to apply and returns the path in the form that the frontend develloper needs
    initial_state: is the start city
    goal_state: the city the user want to reach
    algorithm: the applied algorithm
    returns the path in the form that the frontend develloper needs
    """
    pass

if __name__ == '__main__':
    pass










#
