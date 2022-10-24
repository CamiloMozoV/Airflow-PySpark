from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id="test_dag",
    default_args={
        'depends_on_past': False,
        'email': ['admin@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    },
    description="A simple DAG",
    schedule_interval=timedelta(days=1),
    start_date=datetime(year=2022, month=10, day=23),
    catchup=False,
    tags=['Test']
) as dag:
    
    test_task = SparkSubmitOperator(
        task_id="test_spark",
        application="/opt/airflow/spark-apps/test.py",
        conn_id="test_spark",
        name="Test"
    )

    test_task
