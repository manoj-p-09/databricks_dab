import re
from databricks.sdk.runtime import spark

class DataIngestion:
    def __init__(self,catalog,schema,table):
        if catalog is None or schema is None or table is None:
            return Exception("Catalog, schema and table must be provided!!")
        self.catalog = catalog
        self.schema = schema
        self.table = table
        self.df = None

    def ingest_into_table(self,mergeSchema='true',overwriteSChema='true',mode='overwrite'):
        (self.df
         .write
         .mode(mode)
         .option('mergeSchema',mergeSchema)
         .option('overwriteSchema',overwriteSChema)
         .saveAsTable(f'{self.catalog}.{self.schema}.{self.table}')
        )


    def read_from_csv(self,path=None,header='true',inferSchema='true'):
        if path is None:
            return Exception("Path must be provided!!")
        df = spark.read.option('header',header).option('inferSchema',inferSchema).csv(path)
        self.df = df
    
    def cleanse_column_names(self):
        for c in self.df.columns:
            self.df = self.df.withColumnRenamed(c,re.sub('[^a-zA-Z0-9]','',c))