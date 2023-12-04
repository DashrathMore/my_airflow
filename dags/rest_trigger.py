# airflow bits
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# a function to read the parameters passed
def main_task(ti, **context):
    # the sql
    SQL = """
    select count(a.dim_user_id) as total
    from table1 a,
        table2 b
    where a.dim_account_id = b.id
    and   b.global_id = {}
    and   a.dim_site_id = {}
    and   a.message NOT IN ('JOINED', 'LEFT')
    and   a.activity_date between '{}' and '{}'
    """
    
    # connect to redshift
    rs = connect_redshift()  
    
    # extract the parameters passed from the REST API Trigger 
    gid = context['dag_run'].conf['gid']
    sid = context['dag_run'].conf['sid']
    date_start = context['dag_run'].conf['date_start']
    date_end = context['dag_run'].conf['date_end']
    
    # build the SQL and get the data
    SQL = SQL.format(gid, sid, date_start, date_end)
    df = rs.redshift_to_pandas(SQL)
    
    # do more things and 


args = {
    'owner': 'brock',
    'depends_on_past': False,
    'start_date': days_ago(2),
    #'email': ['brocktibert@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=7),
    'schedule_interval': None,
    'provide_context': True
}

dag = DAG(
    dag_id='rest-trigger',
    default_args=args,
    tags=["brock"]

)

t1 = PythonOperator(task_id = "main_etl", 
                    python_callable = main_task,
                    dag = dag)
