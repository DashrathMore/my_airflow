from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests


default_args = {
    'owner' : 'Dashrath',
    'ritries' : 2,
    'retry_delay' : timedelta(minutes=1)
}

def Call_api():
    response = requests.get('https://api.apis.guru/v2/list.json')
    print(response.json())


with DAG(
    dag_id = 'Call_public_api',
    default_args = default_args,
    start_date = datetime(2023,11,21),
    schedule_interval = '@daily',
    catchup = False
) as dag:
    task1 = PythonOperator(
        task_id = 'call-1',
        python_callable = Call_api

    )

    task1