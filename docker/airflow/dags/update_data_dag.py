from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Admin',
    'depends_on_past': False,
    'retries': 10,
    'retry_delay': timedelta(minutes=3),
}

dag = DAG(
    'update_data',
    default_args=default_args,
    description='update_data',
    schedule_interval='00 06 * * 1-5',  # 월 화 수 목 일 진행
    start_date=datetime(2023, 10, 29),
    catchup=False,
    tags=['update_data'],
)

update_data_task = BashOperator(
    task_id='update_data',
    bash_command='python3 update_data.py',
    dag=dag,
)

update_data_task
