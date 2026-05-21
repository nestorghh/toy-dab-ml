from pyspark import pipelines as dp # type: ignore[attr-defined]
from pyspark.sql.functions import col, sum # type: ignore[attr-defined]


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def sample_zones_toy_dab_ml():
    # Read from the "sample_trips" table, then sum all the fares
    return (
        spark.read.table("sample_trips_toy_dab_ml")
        .groupBy(col("pickup_zip"))
        .agg(sum("fare_amount").alias("total_fare"))
    )
