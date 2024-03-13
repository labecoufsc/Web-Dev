from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS

class InfluxClient:
    def __init__(self,token,org,bucket): 
        self._org=org 
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token=token)

    def write_data(self,data,write_option=SYNCHRONOUS):
        write_api = self._client.write_api(write_option)
        write_api.write(self._bucket, self._org , data,write_precision='s')

    def query_data(self,query):
        query_api = self._client.query_api()
        result = query_api.query(org=self._org, query=query)
        results = []
        for table in result:
            print(table)
            for record in table.records:
                results.append((record.get_value(), record.get_field()))
        print(results)
        return results 

    def query_coordinates(self, query):
        query_api = self._client.query_api()
        result = query_api.query(org=self._org, query=query)
        results =[]
        
        for table in result:
            for record in table.records:
                record.get_value()
        print(results)
        
        return results 


    def delete_data(self,measurement):
        delete_api = self._client.delete_api()
        start = "1970-01-01T00:00:00Z"
        stop = "2021-10-30T00:00:00Z"
        delete_api.delete(start, stop, f'_measurement="{measurement}"', bucket=self._bucket, org=self._org)

