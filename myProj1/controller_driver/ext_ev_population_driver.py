import argparse
import sys
from databricks.sdk.runtime import spark

sys.path.append("../src")
from DataIngestion import DataIngestion
sys.path.append("../transformations")
from transformation import Transformations


#variables & Parameters:
catalog = 'dbacademy_learning'
schema = 'targets'


src = '/Volumes/dbacademy_learning/sourcedataset/source_dataset/Electric_Vehicle_Population_Data.csv'
tgt_tbl = "tbl_ev_population"

#Data Ingestion for the table "tbl_ev_population" CSV as a source.
di = DataIngestion(catalog=catalog,schema=schema,table=tgt_tbl)
di.read_from_csv(path=src)
di.cleanse_column_names()
di.ingest_into_table()

#Data Preview
spark.table(f"{catalog}.{schema}.{tgt_tbl}").display()


