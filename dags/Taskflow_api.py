from airflow.decorators import dag, task

from datetime import datetime, timedelta

default_args = {
    'owner' : 'Dashrath',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=2)
}

@dag(
    dag_id = 'taskflow_api',
    default_args = default_args,
    start_date = datetime(2023,11,25),
    schedule_interval = '@daily')

def Hello_world():
    @task()
    def get_name():
        return 'Dashrath'

    @task()
    def get_age():
        return 23

    @task()
    def Greet(name, age):
        print(f'my name is {name} and i am {age} years old')

    name = get_name()
    age = get_age()

    Greet(name = name,age=age)

I = Hello_world()
        
