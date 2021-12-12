import pandas as pd
old_CSV_File=pd.read_csv('egypt-EstimatedDistanceBetweenCitiesUnicodeFormated.csv')

# 'from'    'to '   'distance'
# 'Cairo'   'Giza'  '10031'
# 'Cairo'   'Tanta' '91496'

df=pd.read_csv('egyptCitiesLat&LongUnicodeFormated.csv')

# 'city'    'lat'   'lng'
# 'Cairo'  30.0561  31.2394

cities=[]

dic_cities={}

for city in old_CSV_File['from']:
    if city in cities:
        continue
    else:
        cities.append(city)

for city in cities:
    dic_cities[city]=[]

for city in cities:
    filt= (old_CSV_File["from"]==city)
    for distance in old_CSV_File.loc[filt,"distance"]:
        dic_cities[city].append(distance/1000)

estimatedDistances=pd.DataFrame(dic_cities)

estimatedDistances.insert(loc=0, column='Cities', value=cities)

latitude=df.loc[:,'lat']
latitude_list=[lat for lat in latitude]
estimatedDistances.insert(loc=1, column='latitude', value=latitude_list)

longitude=df.loc[:,'lng']
longitude_list=[lng for lng in longitude]
estimatedDistances.insert(loc=2, column='longitude', value=longitude_list)

estimatedDistances.to_csv('estimatedDistances.csv', index=False)
