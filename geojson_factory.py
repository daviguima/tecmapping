#from urllib.response import addbase
import csv
#import geopandas
import pandas as pd
#import numpy as np
import random
#from shapely.geometry import Point
#import matplotlib.pyplot as plt

"""
export const addressPoints = [
    [-37.8839, null, "571"],
    [-37.8869090667, 175.3657417333, "486"],
    [-37.8894207167, 175.4015351167, "807"]
    ]
"""
tec_pandas = pd.read_csv('TEC-raw/AMAP_26_2_2019_0h', sep=';')

# stepsize = 0.5 # em graus (0.001 =~ 1 metro)
# for x in range(-90, -30, stepsize):
#     for y in range(-60, 20, stepsize):
#         yield(x, y)

maximum_size = tec_pandas.shape[0] * tec_pandas.shape[1]

latitude = [random.uniform(-60, 20) for i in range(20000)]
longitude = [random.uniform(-90, -30) for i in enumerate(latitude)]
# latitude = np.linspace(-60, 20, maximum_size)
# longitude = np.linspace(-90, -30, maximum_size)
# tec_pandas_list = np.concatenate(np.array(tec_pandas))
tec_random_list = [random.uniform(0, 80) for i in enumerate(latitude)]

addressPoints = []
for i, valor in enumerate(tec_random_list):
    addressPoints.append([latitude[i],longitude[i],valor])

with open('addressPoints.js', 'w') as myfile:
    myfile.write(str(addressPoints))

#addressPoints = np.dstack([latitude, longitude, tec_pandas_list])




# addressPoints = np.meshgrid(latitude,longitude,tec_pandas)

# latitude = np.arange(0.0, ysize)
# xsize = np.arange(0.0, xsize)
#
# def latitude(y_dataframe):
#     y_dataframe = y_dataframe * 0.5
#     y_dataframe -= 60
#     return y_dataframe
#
# def longitude(x_dataframe):
#     x_dataframe = x_dataframe * 0.5
#     x_dataframe -= 90
#     return x_dataframe

# df = pd.DataFrame(
#     {
#     'Tec': list(tec_pandas),
#     'Latitude': list(latitude(ysize)),
#     'Longitude': list(longitude(xsize))
#     })
#
# df['Coordinates'] = list(zip(df.Longitude, df.Latitude))
#
# df['Coordinates'] = df['Coordinates'].apply(Point)
#
# gdf = geopandas.GeoDataFrame(df, geometry='Coordinates')
#
# print(gdf.head())