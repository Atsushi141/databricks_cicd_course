def get_spark():
  try:
    print(spark.session_id)
  except:
    from databricks.connect import DatabricksSession
    return DatabricksSession.builder.getOrCreate()
