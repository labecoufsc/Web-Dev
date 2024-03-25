import datetime
import re
from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
from influxClient import InfluxClient



#client = InfluxDBClient(url="http://localhost:8086", token="Bo6LdE_XVqMZrC6hAu_OUZwhRYxwqFiea01RJx9sdPdtcxbfE0mzPi32spI2JFWkQwpQcUl5Y15Rg2NCX1WrwA==", org="Boias Livres")

IC = InfluxClient("Bo6LdE_XVqMZrC6hAu_OUZwhRYxwqFiea01RJx9sdPdtcxbfE0mzPi32spI2JFWkQwpQcUl5Y15Rg2NCX1WrwA==","Boias Livres","bucket-boias")



_point1 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.414).field("longitude", -48.518) 
_point2 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.414).field("longitude", -48.517) 
_point3 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.413).field("longitude", -48.517) 
_point4 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.412).field("longitude", -48.517) 
_point5 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.412).field("longitude", -48.516) 
_point6 = Point("boiasLivres").tag("boia_id", "2").field("latitude", -27.411).field("longitude", -48.516)
IC.write_data(_point1)
IC.write_data(_point2)
IC.write_data(_point3)
IC.write_data(_point4)
IC.write_data(_point5)
IC.write_data(_point6)
             


"""
query1 = 'from(bucket: "bucket-boias")\
|> range(start: 1633124983)\
|> filter(fn: (r) => r.boia_id == "2")\
|> group()'
"""
query3 = 'from(bucket: "bucket-boias")\
  |> range(start: 1633124983)\
  |> filter(fn: (r) => r["_measurement"] == "boiasLivres")\
  |> filter(fn: (r) => r["boia_id"] == "2")\
  |> filter(fn: (r) => r["_field"] == "latitude" or r["_field"] == "longitude")\
  |> group(columns: ["_time", "tag"])\
  |> yield(name: "mean")'

"""
query2 = f"SELECT longitude, latitude FROM {measurement} WHERE time >= '{start_time}' AND time <= '{end_time}'"
#|> group(columns: ["_time", "tag"])
#|> aggregateWindow(every: 20s, fn: mean, createEmpty: false)\
"""
c = IC.query_data(query3)

#print(c[1])

n = [i[0] for i in c]

print(n)

f = [*zip(n[::2], n[1::2])]

print(f)
