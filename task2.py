import sys

from pyspark import SparkContext
from pyspark.sql import SQLContext

spark_context = SparkContext.getOrCreate()
sql_context = SQLContext(spark_context)

city_p = sys.argv[1].strip()
global_p = sys.argv[2].strip()

city_data = sql_context.read.csv(city_p, header=True)
global_data = sql_context.read.csv(global_p, header=True)

city_data = city_data.drop("City")
city_data = city_data.withColumn("AverageTemperature", city_data.AverageTemperature.cast('float'))

df1 = city_data.groupby('Country', 'dt').max('AverageTemperature')
condition = [df1.dt == global_data.dt, df1[-1] > global_data.LandAverageTemperature]
df = df1.join(global_data, condition, 'inner').drop(df1.dt)
df = df.groupby('Country').count()
df = df.orderBy('Country')
data = df.collect()

for record in data:
    print(record["Country"], '\t', record["count"])
