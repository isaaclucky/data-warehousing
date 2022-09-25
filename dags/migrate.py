import airflow.utils.dates
from airflow.models import DAG
import pandas as pd
from airflow.providers.postgres.operators.postgres import PostgresOperator
import os
from sqlalchemy import create_engine
from airflow.operators.python import PythonOperator
from datetime import timedelta
import psycopg2





args = {
    'owner': 'yishaktadele',
    'email_on_failure': True,
    'email': ['isaaclucky88@gmail.com'],
    'retry_delay':timedelta(minutes=5),
    'retries' : 2
    
}
# args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5)
# }




def migrate_data(path,db_table):
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/airflow",
             echo=True, future=True)
    df = pd.read_csv(path,sep="[,;:]",index_col=False)
    print("<<<<<<<<<<start migrating data>>>>>>>>>>>>>>")
    df.to_sql(db_table, con=engine, if_exists='replace',index_label='id')
    print("<<<<<<<<<<<<<<<<<<<completed>>>>>>>>>>>>>>>>")


dag =  DAG(
    dag_id="migrate_data",
    default_args=args,
    schedule_interval='@once',
    start_date=airflow.utils.dates.days_ago(1),
    catchup=True,
)
create_table = PostgresOperator(
    task_id="create_table",
    postgres_conn_id="postgres",
    sql="sql/create_table.sql",
    dag=dag
)
migrate = PythonOperator(
        task_id='migrate',
        dag=dag,
        python_callable=migrate_data,
        op_kwargs={
            "path": "./data/20181024_d1_0830_0900.csv",
            "db_table":"traffic_data"
        }
    )
read_data = PostgresOperator(
    dag=dag,
    task_id="read_data",
    sql = "sql/read.sql",
    postgres_conn_id="postgres"
    )

create_table >> migrate>> read_data


if __name__ == "__main__":
    dag.cli()