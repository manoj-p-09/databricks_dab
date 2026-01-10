import argparse
import sys
from databricks.sdk.runtime import spark

sys.path.append("../src")
from DataIngestion import DataIngestion
sys.path.append("../transformations")
from transformation import Transformations

parser = argparse.ArgumentParser(description="Databricks job with catalog and schema parameters")
parser.add_argument("--catalog", required=True)
parser.add_argument("--schema", required=True)
parser.add_argument("--src", required=False)
parser.add_argument("--tgt_tbl", required=True)
args = parser.parse_args()


#variables & Parameters:
catalog = args.catalog
schema = args.schema
src = args.src 
tgt_tbl = args.tgt_tbl
# src = '/Volumes/dbacademy_learning/sourcedataset/source_dataset/Electric_Vehicle_Population_Data.csv'
# tgt_tbl = "tbl_ev_population"

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


