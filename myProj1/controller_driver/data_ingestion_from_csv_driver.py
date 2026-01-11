import sys

sys.path.append('../src')
from initial_config import *


#Data Ingestion for the table "tbl_ev_population" CSV as a source.
print("Initilizing Data Ingestion...")
di = DataIngestion(catalog=catalog,schema=schema,table=tgt_tbl)
print(f"Reading data from csv : {src}")
di.read_from_csv(path=src)
print("Cleansing Columns...")
di.cleanse_column_names()
print(f"Ingesting data into {tgt_tbl}")
di.ingest_into_table()
print("Data Ingestion Completed.")

#Data Preview
print("Showing Data preview.")
spark.table(f"{catalog}.{schema}.{tgt_tbl}").show(10)


