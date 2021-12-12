from treeSorted import realDistances
from treeSorted import tree

# key : city, value : the adjacent cities with their real distances from the current city
AStar_tree={}
# example for AStar_tree
# AStar_tree={
#         'Tala':         [('ShebinElkom', 16.3),('BerketAlseb3', 19.7)],
#         'Alshohda':     [('Minouf', 22.8)],
#         'BerketAlseb3': [('Quesna', 17.1), ('Tala', 19.7)],
#         'Quesna':       [('BerketAlseb3', 17.1),('ShebinElkom', 18.3)],
#         }

for city in tree:
    lst=[]  # a list of cities with their real distances from the current city
    for adjacent in tree[city]:
        # this tuple consist of the two values
        # 1st value is the adjacent city
        # 2nd value is the real distance from the current city
        tup=(adjacent,realDistances.loc[city,adjacent])
        lst.append(tup)
    AStar_tree[city]=lst
