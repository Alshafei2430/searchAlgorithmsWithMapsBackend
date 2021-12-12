import pandas as pd
old_CSV_File=pd.read_csv('egypt-DistanceBetweenCitiesUnicodeFormated.csv')

# 'from'    'to '   'distance'
# 'Cairo'   'Giza'  '10031'
# 'Cairo'   'Tanta' '91496'

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

realDistances=pd.DataFrame(dic_cities)
realDistances.insert(loc=0, column='Cities', value=cities)
print(realDistances)
realDistances.to_csv('realDistancesUnicodeFormated.csv',index=False)
