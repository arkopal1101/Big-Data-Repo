import sys

from pyspark import SparkContext
from pyspark.sql import SQLContext

location = sys.argv[1]
path = sys.argv[2]

spark_context = SparkContext.getOrCreate()
spark = SQLContext(spark_context)

df = spark.read.option('header', 'true').csv(path, inferSchema=True)
df = df.withColumn('AverageTemperature', df['AverageTemperature'].cast('float'))

df1 = df.filter(df.Country == location)

df2 = df1.groupBy('City').avg("AverageTemperature").withColumnRenamed("avg(AverageTemperature)", 'AvgTemp')
df2 = df2.withColumnRenamed('City', 'New')

df1 = df1.join(df2, df1.City == df2.New, 'outer')
df1 = df1.filter(df1.AverageTemperature > df1.AvgTemp)

ans = df1.groupBy('City').count().collect()
ans.sort()

for record in ans:
    print(str(record[0]) + '\t' + str(record[1]))
