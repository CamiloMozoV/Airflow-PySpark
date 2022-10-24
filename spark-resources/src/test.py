from pyspark.sql import SparkSession

if __name__=="__main__":
    # Create a session
    spark = SparkSession.builder\
            .appName("Test")\
            .master("spark://spark-master:7077")\
            .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    print("= = ="*15)
    print("====== TEST is Working ======")
    print("= = ="*15)

    spark.stop()