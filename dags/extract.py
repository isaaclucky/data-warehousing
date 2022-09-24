import airflow.utils.dates
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
import os


args = {
    'owner': 'yishaktadele',
    'email_on_failure': True,
    'email': ['isaaclucky88@gmail.com']
}
# args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5)
# }

dag = DAG(
    dag_id="extract",
    default_args=args,
    schedule_interval=None,
    start_date=airflow.utils.dates.days_ago(1),
    catchup=True,
)

create_table = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres",
    sql="sql/create_table.sql",
    dag=dag
)


extract_data = PostgresOperator(
    dag=dag,
    task_id="extract_data",
    sql="sql/unload.sql",
    postgres_conn_id="postgres"
)

read_data = PostgresOperator(
    dag=dag,
    task_id="read_data",
    sql = "sql/transform.sql",
    postgres_conn_id="postgres"
    )



create_table >> read_data

if __name__ == "__main__":
    dag.cli()
