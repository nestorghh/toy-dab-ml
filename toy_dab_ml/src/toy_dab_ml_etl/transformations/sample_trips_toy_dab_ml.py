from pyspark import pipelines as dp # type: ignore[attr-defined]



# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def sample_trips_toy_dab_ml():
    return spark.read.table("samples.nyctaxi.trips")
