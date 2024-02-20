import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
#from include.helpers import print_msg


def print_message():
    print('Testing airflow locally for the first time this year')


with (DAG('test_dags',
          start_date=datetime(2024, 1, 1),
          schedule_interval='@daily',
          catchup=False)
      as dag):

    start_task = DummyOperator(task_id='start_task')

    first_task = PythonOperator(
        task_id='first_task',
        python_callable=print_message
    )

    end_task = DummyOperator(task_id='end_task')

    start_task >> first_task >> end_task