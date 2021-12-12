from treeSorted import realDistances

H={} # hurestic distances
# example for H dictionary:
# H = {
#     'Tala':         {
#                         'Tala': 0,
#                         'Alshohda': 13.7,
#                         'BerketAlseb3': 19.7,
#                         'Quesna': 32.8,
#                         'ShebinElkom': 16.3,
#                         'Minouf': 32,
#                         'SirsAllyan': 31.5,
#                         'Elbagoor': 31.9,
#                         'Ashmoon': 56.5,
#                         'Elsadat': 77.5
#                     },
#
#     'Alshohda':     {
#                         'Tala': 13.7,
#                         'Alshohda': 0,
#                         'BerketAlseb3': 28.9,
#                         'Quesna': 30.8,
#                         'ShebinElkom': 14.3,
#                         'Minouf': 22.8,
#                         'SirsAllyan': 27.1,
#                         'Elbagoor': 30.7,
#                         'Ashmoon': 41.6,
#                         'Elsadat': 78.9,
#                     }
#         }

for city in realDistances.index:
    dic2={}
    for city2 in realDistances.index:
        dic2[city2]= realDistances.loc[city, city2]
    H[city]=dic2
