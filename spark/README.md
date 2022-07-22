# BUCKETING AND PARTITIONING IN SPARK 

+ [Tutorial](https://selectfrom.dev/apache-spark-partitioning-bucketing-3fd350816911)
    + Bucketing - Dividing the data into N rather equal sized objects. Also uses a bit of hashing
    + Partitioning - storing the data in specific folder. (Sometimes in same location but maybe not always)
+ According to [this] and [this tutorial] Spark partition is located within 1 machine. When we speak about partitions its not necessarily the case. Here the folder structure is importand to more quickly find data. 

# INTERACTING WITH COSMOSDB 


+ Spark 2 https://github.com/Azure/azure-cosmosdb-spark
+ Spark 3  These settings seem to be working From Synapse https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/cosmos/azure-cosmos-spark_3_2-12/docs/configuration-reference.md#query-config


# SYNAPSE SPARK ARGUMENTS 

https://aboutdataai.com.au/2021/07/05/azure-synapse-notebooks-pass-parameter-and-return-output/
