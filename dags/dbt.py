from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args = {
  'dir': './migrate_to_dbt',
}


with DAG(
    dag_id='dbt_dag',
    default_args=default_args,
    start_date=airflow.utils.dates.days_ago(1),
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval=timedelta(days=1),
) as dag:
    extract = DummyOperator(task_id="extract")
    load = DummyOperator(task_id="load")
    ml_training = DummyOperator(task_id="ml_training")

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run'
    )

    
    extract >> load >> dbt_run >> ml_training