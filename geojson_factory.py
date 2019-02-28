import geopandas
import pandas as pd
import numpy as np
from shapely.geometry import Point
import matplotlib.pyplot as plt


# export const addressPoints = [
# [-37.8839, null, "571"],
# [-37.8869090667, 175.3657417333, "486"],
# [-37.8894207167, 175.4015351167, "807"]
# ]

tec_pandas = pd.read_csv('/home/davi/Downloads/AMAP_26_2_2019_0h', sep=';')

maximum_size = tec_pandas.shape[0] * tec_pandas.shape[1]

latitude = np.linspace(20, -60, maximum_size)
longitude = np.linspace(-90, -30, maximum_size)
tec_pandas_list = tec_pandas.tolist()

addressPoints = np.dstack([latitude, longitude, tec_pandas_list])

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


print(
    tec_pandas_list, '\n\n',
    latitude, '\n\n',
    longitude
)

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