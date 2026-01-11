import argparse
import sys
from databricks.sdk.runtime import spark

sys.path.append("../src")
from DataIngestion import DataIngestion
sys.path.append("../transformations")
from transformation import Transformations

#Read the In-Line Parameters | for Specific Testing Set the Defaults as required.
parser = argparse.ArgumentParser(description="Databricks job with catalog and schema parameters")
parser.add_argument("--catalog", required=True,default='dbacademy_learning')
parser.add_argument("--schema", required=True,default='targets')
parser.add_argument("--src", required=False,default="")
parser.add_argument("--tgt_tbl", required=True,default='ev_state_detail')
parser.add_argument("--src_table", required=False,default="")
args = parser.parse_args()

#variables & Parameters:
catalog = args.catalog
schema = args.schema
src = args.src 
tgt_tbl = args.tgt_tbl
src_table = args.src_table