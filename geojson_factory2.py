import pandas as pd
import numpy as np
import geojson

tec_pandas = pd.read_csv('TEC-raw/AMAP_26_2_2019_0h', sep=';', header=None)
tec_pandas = tec_pandas.dropna(axis='columns')
tec_pandas_list = np.concatenate(np.array(tec_pandas))
#tec_pandas_list = tec_pandas_list[::-1]

latitude = np.arange(-60, 20, 0.5)
#latitude = np.fliplr([latitude])[0]

longitude = np.arange(-90, -30, 0.5)

latlonlist = [(lat, lon) for lat in latitude for lon in longitude]

addressPoints = []
for i, tec in enumerate(tec_pandas_list):
    addressPoints.append([latlonlist[i][0], latlonlist[i][1], tec])

# Removing -1 TEC values
addressPoints = [item for item in addressPoints if item[2] != -1]

# Saving as a javascript list
with open('Silvao.js', 'w') as myfile:
    myfile.write('export const addressPoints = ' + str(addressPoints))


# UNCOMENT THESE FOR GEOJson files
# def data2geojson(df):
#     features = []
#     insert_features = lambda X: features.append(
#             geojson.Feature(geometry=geojson.Point((X["lon"],
#                                                     X["lat"])),
#                             properties=dict(tec=X["tec"])))
#     df.apply(insert_features, axis=1)
#     with open('tec-amap.geojson', 'w', encoding='utf8') as fp:
#         geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)
#
#
# col = ['lat', 'lon', 'tec']
#
# data = addressPoints
# drop = [d for d in data if d[2] != -1]
#
# print(data[:10],'\n\n',drop[:10])
# # data = [[-29.9953, -70.5867, 760],
# #         [-30.1217, -70.4933, 1250],
# #         [-30.0953, -70.5008, 1185]]
#
# df = pd.DataFrame(drop, columns=col)
#
# data2geojson(df)
