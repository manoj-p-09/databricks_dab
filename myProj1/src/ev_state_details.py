from initial_config import *

print("Extract Country Details from TBL_EV_POPULATION")
df = spark.sql(f"select County,City,State,PostalCode from {catalog}.{schema}.tbl_ev_population")

print("Write Data into Target Table ")
di = DataIngestion(df=df,catalog=catalog,schema=schema,table=tgt_tbl)
di.ingest_into_table(mergeSchema='true',overwriteSChema='true',mode='overwrite',isTruncateLoad=0)
