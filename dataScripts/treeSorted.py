import pandas as pd
realDistances=pd.read_csv('realDistancesUnicodeFormated.csv')
estimatedDistances=pd.read_csv('estimatedDistancesUnicodeFormated.csv')

realDistances.set_index('Cities', inplace=True)

estimatedDistances.set_index('Cities', inplace=True)


xy_memo={}

def get_xy(current, adj_city):
    """
    Checks if we do calculations of x and y for theses cities before.If we
    do theses calculations before we don't need to repeat them again. if not, we
    will do them and store them in a memo to facilitate for re-use
    x : the difference between latitudes for current and adj_city
    y : the difference between lonitudes for current and adj_city
    current : is the city we need to find its adjacents
    adj_city :
    returns the value of x and y
    """

    # checks if the calculations of x and y for (current,adj_city) is exist in xy_memo
    if xy_memo.get((current,adj_city)):
        x,y=xy_memo[(current,adj_city)]

    # checks if the calculations of x and y for (adj_city,current) is exist in xy_memo
    elif xy_memo.get((adj_city,current)):
        x,y=xy_memo[(adj_city,current)]

    # if we don't do these calculations before, we do them and store them for further more usage
    else:
        x = estimatedDistances.loc[adj_city,'latitude']-estimatedDistances.loc[current,'latitude']
        y = estimatedDistances.loc[adj_city,'longitude']-estimatedDistances.loc[current,'longitude']
        xy_memo[(current,adj_city)]=x,y

    # return the value of x and y
    return x,y


def change_neighbour_city(current, old_city, new_city):
    """
    Changes the neighbour city value from the old city to the new city
    if the distance between the new adjacent city and current city is
    less than the distance between the old adjacent city and current city.
    current: is the city we need to find its adjacents
    old_city: is the old neighbour city
    new_city: is the new neighbour city
    returns the city with the smaller distance between it and the current city
    """
    if realDistances.loc[current,new_city]<realDistances.loc[current,old_city]:
        return new_city
    return old_city


def adj_for_city(current,xy_memo={}, adj={}):
    """
    Finds the adjacent cities to a specific city(current)
    current: is the city we need to find its adjacents
    xy_memo: is a hashtable to memorize the calculations of x and y
    returns the adjacent cities
    """
    adj_list=[]  # a list of adjacent cities of the current city
    NE_city= ''  # the neighbour city that is in the Northeast of current city
    NW_city= ''  # the neighbour city that is in the Northwest of current city
    SW_city= ''  # the neighbour city that is in the Southeast of current city
    SE_city= ''  # the neighbour city that is in the Southwest of current city

    # Initialize NE_city, NW_city, SW_city and SE_city with proper values
    for adj_city in estimatedDistances.index:

        # the current city can't be an adjacent to itself
        if adj_city==current:
            continue

        # x : the difference between latitudes for current and adj_city
        # y : the difference between lonitudes for current and adj_city
        x , y = get_xy(current, adj_city)

        # Initialize NE_city with a proper value
        if x>0 and y>0:
            NE_city=adj_city

        # Initialize NW_city with a proper value
        elif x<0 and y>0:
            NW_city=adj_city

        # Initialize SW_city with a proper value
        elif x<0 and y<0:
            SW_city=adj_city

        # Initialize SE_city with a proper value
        elif x>0 and y<0:
            SE_city=adj_city

        # if we intialize these cities with proper values, we should break the loop(or stop the iteration)
        if (NE_city and NW_city and SW_city and SE_city):
            break

    # finds the adjacent of the current city
    for adj_city in estimatedDistances.index:

        # the current city can't be an adjacent to itself
        if adj_city==current:
            continue

        x , y = get_xy(current, adj_city)

        # Neighbour in the Northeast
        if x>0 and y>0:
            NE_city = change_neighbour_city(current, NE_city, adj_city)

        # Neighbour in the Northwest
        elif x<0 and y>0:
            NW_city = change_neighbour_city(current, NW_city, adj_city)

        # Neighbour in the Southwest
        elif x<0 and y<0:
            SW_city = change_neighbour_city(current, SW_city, adj_city)

        # Neighbour in the southeast
        elif x>0 and y<0:
            SE_city = change_neighbour_city(current, SE_city, adj_city)

    adj_list= [NE_city, NW_city, SW_city, SE_city]

    while '' in adj_list:
        adj_list.remove('')

    return adj_list

def getAdjacents():
    """
    Gets the adjacent of all cities
    returns a dict. of cities each city as a key and its adjacents as a value
    """
    adj={}
    for city in realDistances.index:
        adj[city]=adj_for_city(city, xy_memo, adj)
        # sorting adjacents in ascending order according to their distance from current city
        adj[city].sort(key = lambda neighbour: realDistances.loc[city,neighbour])
    return adj


tree=getAdjacents()
