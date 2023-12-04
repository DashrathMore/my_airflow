from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

default_args = {
	'owner' : 'Dashrath',
	'retries' : 2,
	'retry_delay' : timedelta(minutes=2)
	}


def Greet(name, age):
	print(f' my name is {name} and age is {age}')

with DAG(
	dag_id = 'PythonOperator',
	default_args = default_args,
	start_date = datetime(2023,11,26),
	catchup = False,
	schedule_interval = '@daily'
	) as dag:
	
	task1 = PythonOperator(
	task_id = 'operator_1',
	python_callable = Greet,
	op_kwargs = {'name' : 'Dashrath', 'age':23}
	)

	task2 = PythonOperator(
	task_id = 'operator_2',
	python_callable = Greet,
	op_kwargs = {'name' : 'Bhagavant', 'age':25}
	)

	task1