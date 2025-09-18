from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
data=spark.sql("select * from employee")
data.count()
