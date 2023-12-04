from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'Dashrath',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=1) 
}

def first():
    print('**** start dag ****')

def Greet (ti):
    first_name = ti.xcom_pull(task_id = 'get_name', key='first_name')
    last_name = ti.xcom_pull(task_id = 'get_name', key='last_name')
    age = ti.xcom_pull(task_id = 'get_age', key='age')

    print(f"Hello my friends i am {first_name} {last_name}\nAnd i am {age} years old")

def get_name(ti):
    ti.xcom_push(key = 'first_name', value = 'Dashrath')
    ti.xcom_push(key = 'last_name', value = 'More')

def get_age(ti):
    ti.xcom_push(key='age', value=23)

with DAG(
    dag_id = 'crone_exp',
    default_args = default_args,
    start_date = datetime(2023,11,25),
    schedule_interval = '@daily',
    description = 'xcom operations'

    ) as dag:

    task1 = PythonOperator(
        task_id='first',
        python_callable = first
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable = get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable = get_age
    )

    task4 = PythonOperator(
        task_id='final_output',
        python_callable = Greet
    )
    task1 >> task2 >> task3 >> task4