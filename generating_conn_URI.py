"""
    Run this script, the output should be something like:
    AIRFLOW_CONN_TEST_SPARK=spark://spark-master:7077/?queue=root.default&deploy_mode=cluster&spark_home=%2Fopt%2Fbitnami%2Fspark%2F&spark_binary=spark-submit
"""
from airflow.models.connection import Connection

spark_conn = Connection(
    conn_id="test_spark",
    conn_type="spark",
    host="spark-master",
    port=7077,
    extra={"queue": "root.default", 
           "deploy_mode": "cluster", 
           "spark_home": "/opt/bitnami/spark/", 
           "spark_binary": "spark-submit"
        }
)

print(f"AIRFLOW_CONN_{spark_conn.conn_id.upper()}={spark_conn.get_uri()}")