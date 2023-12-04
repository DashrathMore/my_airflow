from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

default_args = {
	'owner' : 'Dashrath',
	'retries' : 0,
	'retry_time' : timedelta(minutes=2)
}

with DAG(
	dag_id='catchup',
	default_args = default_args,
	description = 'This is normal catchup',
	start_date = datetime(2023,11,25),
	schedule_interval = '@daily',
    
    #the default value of catchup is True
    #catchup = True
    #it will work on previous dates

    #this will work for current date only
    catchup = False
	) as dag:
	
	task1 = BashOperator(
	task_id = 'Bash_1',
	bash_command = 'echo This is first task'
	)

	task2 = BashOperator(
	task_id = 'Bash_2',
	bash_command = 'echo this is second task'
	)

	task1 >> task2