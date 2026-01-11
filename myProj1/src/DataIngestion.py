import re
from databricks.sdk.runtime import spark

class DataIngestion:
    def __init__(self,catalog,schema,table,df=None):
        if catalog is None or schema is None or table is None:
            return Exception("Catalog, schema and table must be provided!!")
        self.catalog = catalog
        self.schema = schema
        self.table = table
        self.df = df

    def ingest_into_table(self,mergeSchema='false',overwriteSChema='false',mode='append',isTruncateLoad=0):        
        tbl_name = f'{self.catalog}.{self.schema}.{self.table}'

        if isTruncateLoad:
            print(f"Truncate & Load is Set to True. Truncating the table {tbl_name}.")
            spark.sql(f"TRUNCATE TABLE {tbl_name}")
        
        (self.df
         .write
         .mode(mode)
         .option('mergeSchema',mergeSchema)
         .option('overwriteSchema',overwriteSChema)
         .saveAsTable(f'{tbl_name}')
        )
        print(f"Data Was successfully {mode} into table {tbl_name}")
  
    def cleanse_column_names(self):
        for c in self.df.columns:
            self.df = self.df.withColumnRenamed(c,re.sub('[^a-zA-Z0-9]','',c))

    #Different Type of Data source Reads..
    def read_from_csv(self,path=None,header='true',inferSchema='true'):
        if path is None:
            return Exception("Path must be provided!!")
        df = spark.read.option('header',header).option('inferSchema',inferSchema).csv(path)
        self.df = df
    
    def read_from_json(self,path=None,header='true',inferSchema='true'):
        if path is None:
            return Exception("Path must be provided!!")
        df = spark.read.option('header',header).option('inferSchema',inferSchema).json(path)
        self.df = df
    
    def read_from_parquet(self,path=None,header='true',inferSchema='true'):
        if path is None:
            return Exception("Path must be provided!!")
        df = spark.read.option('header',header).option('inferSchema',inferSchema).parquet(path)
        self.df = df

    #Declare your Reads Type and Parameters based on below suggested definition:
    # def read_from_<source_type>(<Parameters>):
    #     #Edge Case to ensure all parameters are passed!!
    #     df = spark.read.<configure based on Source Type>
    #     self.df = df








