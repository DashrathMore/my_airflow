from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime,timedelta
import os

default_args = {
    'owner': 'Dashrath',
    'start_date': datetime(2023, 11, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def upload_to_s3():
    filename = '/opt/airflow/dags/example.csv'
    key = 'example.csv'
    bucket_name = 'post-air'

    hook = S3Hook('aws_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)
    print('File uploaded to S3.')

with DAG(
    dag_id='s3_upload_csv', 
    default_args=default_args, 
    schedule_interval=None,
    ) as dag:
    upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )
    upload_task