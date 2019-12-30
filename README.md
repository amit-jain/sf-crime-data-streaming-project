# SF Crime Statistics with Spark Streaming

## How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

The metric tracked was  `processedRowsPerSecond` and it either decreased and increased and the most optimum value found with values below.


## What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

The options I played around with and found the most relevant with respective values were:

```
spark.sql.shuffle.partitions                5
spark.streaming.kafka.maxRatePerPartition   5
```
The `processedRowsPerSecond` max at these values ~ 227

