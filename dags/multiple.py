from airflow.decorators import dag, task

from datetime import datetime, timedelta

default_args = {
    'owner' : 'Dashrath',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=2)
}

@dag(
    dag_id = 'api_dag1',
    default_args = default_args,
    start_date = datetime(2023,11,25),
    schedule_interval = '@daily',
    catchup = False,
)

def Hello_world():

    @task(multiple_outputs = True)
    def get_name():
        return {'first_name': 'Dashrath', 'last_name':'More'}

    @task()
    def get_age():
        return 23

    @task()
    def Greet(first_name, last_name, age):
        print(f'my name is {first_name} {last_name} and i am {age} years old')

    name_dict = get_name()
    age = get_age()
    first_name = name_dict['first_name']
    last_name = name_dict['last_name']
    Greet(first_name = first_name, last_name = last_name,age=age)

I = Hello_world()
        