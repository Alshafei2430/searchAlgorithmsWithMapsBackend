import csv
def depthFirstSearchAlgo():
    country = "egypt"
    startCity = "cairo"
    endCity = "giza"
    countryCities = []
    with open('worldcities.csv', mode='r') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if country.lower() == row[4].lower():
                    long = "{:.4f}".format(float(row[3]))
                    lat = "{:.4f}".format(float(row[2]))
                    countryCities.append({
                        "id": row[10],
                        "name": row[0],
                        "coordinate": [long, lat]
                    })
        return countryCities

# country = "egypt"
#     startCity = "cairo"
#     endCity = "giza"
#     countryCities = []
#     with open('./worldcities.csv', mode='r') as csv_data:
#         csv_reader = csv.reader(csv_data, delimiter=',')
#         print(csv_reader)
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(row)
#                 if country.lower() == row[4]:
#                     countryCities.append({
#                         "city": row[0],
#                         "lat": row[2],
#                         "lng": row[3]
#                     })
    # tree = {
    #     'A': ['B', 'D'],
    #     'B': ['A', 'C'],
    #     'C': ['B'],
    #     'D': ['A', 'E', 'F'],
    #     'E': ['D', 'F', 'G'],
    #     'F': ['D', 'E', 'H'],
    #     'G': ['E', 'H'],
    #     'H': ['F', 'G'],
    # }
    # stack = []
    # visited = {}
    # dfs__traversed_output = []
    # for node in tree.keys():
    #     visited[node] = False
    # startNode = 'A'
    # stack.append(startNode)

    # while(len(stack) > 0):
    #     node = stack.pop()
    #     if(not visited[node]):
    #         visited[node] = True
    #         dfs__traversed_output.append(node)
    #         for unvisitedNeighbourNode in tree[node]:
    #             stack.append(unvisitedNeighbourNode)

    # print(stack)
    # print(visited)
    # print(dfs__traversed_output)

    # return jsonify({"data": dfs__traversed_output})
