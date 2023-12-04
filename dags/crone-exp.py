from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'Dashrath',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=1) 
}

with DAG(
    dag_id = 'crone_exp',
    default_args = default_args,
    start_date = datetime(2023,11,25),
    #schedule_interval = '0 0 * * *'

    # this is scheduled for monday to friday
    schedule_interval = '0 0 * * mon-fri'


    ) as dag:

    task1 = BashOperator(
        task_id = 'bash_1',
        bash_command = 'echo This is a example of crone expression'
    )
    task1



