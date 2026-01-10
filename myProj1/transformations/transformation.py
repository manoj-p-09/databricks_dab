class Transformations:

    def execute_analytic_sql(self,sql):
        df = spark.sql(sql)
        display(df.show(10))
        return df
     