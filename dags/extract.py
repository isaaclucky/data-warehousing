import airflow.utils.dates
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
    


args = {
    'owner': 'yishaktadele',
    'email_on_failure': True,
	'email': ['isaaclucky88@gmail.com']
}

dag = DAG(
   dag_id="extract",
   default_args=args,
   schedule_interval=None,
   start_date=airflow.utils.dates.days_ago(1),
   catchup=False,
)

create_table = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres_default",
    sql="sql/create_table.sql",
    dag=dag
)


extract_data = PostgresOperator(
    dag=dag,
    task_id="extract_data",
    sql="sql/unload.sql",
    postgres_conn_id="postgres_default"
)

create_table >> extract_data

if __name__ == "__main__":
    dag.cli()