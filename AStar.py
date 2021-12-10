from collections import deque

#---------------------------------------------------------------------
#------------------------ A* Search Function -------------------------
#---------------------------------------------------------------------

def aStar(start, end):


    class Graph:
        def __init__(self, adjac_lis):
            self.adjac_lis = adjac_lis
    
        def get_neighbors(self, v):
            return self.adjac_lis[v]
    
        # This is heuristic function which is having equal values for all nodes
        def h(self, n, v):
            
            H = {
                'Tala':         {
                                    'Tala': 0,
                                    'Alshohda': 13.7,
                                    'BerketAlseb3': 19.7,
                                    'Quesna': 32.8,
                                    'ShebinElkom': 16.3,
                                    'Minouf': 32,
                                    'SirsAllyan': 31.5,
                                    'Elbagoor': 31.9,
                                    'Ashmoon': 56.5,
                                    'Elsadat': 77.5
                                },

                'Alshohda':     {
                                    'Tala': 13.7,
                                    'Alshohda': 0,
                                    'BerketAlseb3': 28.9,
                                    'Quesna': 30.8,
                                    'ShebinElkom': 14.3,
                                    'Minouf': 22.8,
                                    'SirsAllyan': 27.1,
                                    'Elbagoor': 30.7,
                                    'Ashmoon': 41.6,
                                    'Elsadat': 78.9,
                                },

                'BerketAlseb3': {
                                    'Tala': 19.7,
                                    'Alshohda': 28.9,
                                    'BerketAlseb3': 0,
                                    'Quesna': 17.1,
                                    'ShebinElkom': 15.2,
                                    'Minouf': 31.6,
                                    'SirsAllyan': 30.1,
                                    'Elbagoor': 29.2,
                                    'Ashmoon': 51.5,
                                    'Elsadat': 82,
                                },

                'Quesna':       {
                                    'Tala': 32.8,
                                    'Alshohda': 30.8,
                                    'BerketAlseb3': 17.1,
                                    'Quesna': 0,
                                    'ShebinElkom': 18.3,
                                    'Minouf': 33.7,
                                    'SirsAllyan': 32.5,
                                    'Elbagoor': 33.7,
                                    'Ashmoon': 50.1,
                                    'Elsadat': 87.7,
                                },

                'ShebinElkom':  {
                                    'Tala': 16.3,
                                    'Alshohda': 14.3,
                                    'BerketAlseb3': 14.3,
                                    'Quesna': 18.3,
                                    'ShebinElkom': 0,
                                    'Minouf': 17.9,
                                    'SirsAllyan': 16.2,
                                    'Elbagoor': 16.2,
                                    'Ashmoon': 39.1,
                                    'Elsadat': 67.5,
                                },

                'Minouf':       {
                                    'Tala': 32,
                                    'Alshohda': 22.8,
                                    'BerketAlseb3': 31.6,
                                    'Quesna': 33.7,
                                    'ShebinElkom': 17.9,
                                    'Minouf': 0,
                                    'SirsAllyan': 7.2,
                                    'Elbagoor': 17.1,
                                    'Ashmoon': 24.1,
                                    'Elsadat': 57.7,
                                },

                'SirsAllyan':   {
                                    'Tala': 31.5,
                                    'Alshohda': 27.1,
                                    'BerketAlseb3': 30.1,
                                    'Quesna': 32.5,
                                    'ShebinElkom': 16.2,
                                    'Minouf': 7.2,
                                    'SirsAllyan': 0,
                                    'Elbagoor': 8.3,
                                    'Ashmoon': 22.2,
                                    'Elsadat': 62.6,
                                },

                'Elbagoor':     {
                                    'Tala': 31.9,
                                    'Alshohda': 30.7,
                                    'BerketAlseb3': 29.2,
                                    'Quesna': 33.7,
                                    'ShebinElkom': 16.2,
                                    'Minouf': 17.1,
                                    'SirsAllyan': 8.3,
                                    'Elbagoor': 0,
                                    'Ashmoon': 21,
                                    'Elsadat': 70.6,
                                },

                'Ashmoon':      {
                                    'Tala': 56.5,
                                    'Alshohda': 41.6,
                                    'BerketAlseb3': 51.5,
                                    'Quesna': 50.1,
                                    'ShebinElkom': 39.1,
                                    'Minouf': 24.1,
                                    'SirsAllyan': 22.2,
                                    'Elbagoor': 21,
                                    'Ashmoon': 0,
                                    'Elsadat': 75,
                                },

                'Elsadat':      {
                                    'Tala': 77.5,
                                    'Alshohda': 78.9,
                                    'BerketAlseb3': 82,
                                    'Quesna': 87.7,
                                    'ShebinElkom': 67.5,
                                    'Minouf': 57.6,
                                    'SirsAllyan': 62.6,
                                    'Elbagoor': 70.6,
                                    'Ashmoon': 75,
                                    'Elsadat': 0,
                                }

            }
    
            return H[n][v]
    
        def a_star_algorithm(self, start, stop):
            # In this open_lst is a lisy of nodes which have been visited, but who's 
            # neighbours haven't all been always inspected, It starts off with the start 
            #node
            # And closed_lst is a list of nodes which have been visited
            # and who's neighbors have been always inspected
            open_lst = set([start])
            closed_lst = set([])
    
            # poo has present distances from start to all other nodes
            # the default value is +infinity
            poo = {}
            poo[start] = 0
    
            # par contains an adjac mapping of all nodes
            par = {}
            par[start] = start
    
            while len(open_lst) > 0:
                n = None
    
                # it will find a node with the lowest value of f() -
                for v in open_lst:
                    if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                        n = v;
    
                if n == None:
                    print('Path does not exist!')
                    return None
    
                # if the current node is the stop
                # then we start again from start
                if n == stop:
                    reconst_path = []
    
                    while par[n] != n:
                        reconst_path.append(n)
                        n = par[n]
    
                    reconst_path.append(start)
    
                    reconst_path.reverse()
    
                    # print(reconst_path)
                    # print('Path found: {}'.format(reconst_path))
                    return reconst_path
    
                # for all the neighbors of the current node do
                for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                    # add it to open_lst and note n as it's par
                    if m not in open_lst and m not in closed_lst:
                        open_lst.add(m)
                        par[m] = n
                        poo[m] = poo[n] + weight
    
                    # otherwise, check if it's quicker to first visit n, then m
                    # and if it is, update par data and poo data
                    # and if the node was in the closed_lst, move it to open_lst
                    else:
                        if poo[m] > poo[n] + weight:
                            poo[m] = poo[n] + weight
                            par[m] = n
    
                            if m in closed_lst:
                                closed_lst.remove(m)
                                open_lst.add(m)
    
                # remove n from the open_lst, and add it to closed_lst
                # because all of his neighbors were inspected
                open_lst.remove(n)
                closed_lst.add(n)
    
            print('Path does not exist!')
            return None


    adj_list={
            'Tala':         [('ShebinElkom', 16.3),('BerketAlseb3', 19.7)],
            'Alshohda':     [('Minouf', 22.8)],
            'BerketAlseb3': [('Quesna', 17.1), ('Tala', 19.7)],
            'Quesna':       [('BerketAlseb3', 17.1),('ShebinElkom', 18.3)],
            'ShebinElkom':  [('Tala', 16.3),('Minouf', 17.9),('Quesna', 18.3)],
            'Minouf':       [('SirsAllyan', 7.2),('ShebinElkom', 17.9),('Alshohda', 22.8)],
            'SirsAllyan':   [('Minouf', 7.2),('Elbagoor', 8.3)],
            'Elbagoor':     [('SirsAllyan', 3.8)],
            'Ashmoon':      [('Elsadat', 75)],
            'Elsadat':      [('Minouf', 57.6), ('Ashmoon', 75)]
            }

    first = start
    last = end
    graph1 = Graph(adj_list)
    path = graph1.a_star_algorithm(first, last)
    return path

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

path = aStar('Ashmoon', 'BerketAlseb3')
print(path)