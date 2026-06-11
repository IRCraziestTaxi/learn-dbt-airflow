from datetime import timedelta
from airflow.decorators import dag, task

default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(seconds=2)
}

@dag(
    dag_id="weather_pipeline",
    default_args=default_args,
    description="Test of Airflow-orchestrated DBT-based workflow in the learn-dbt-airflow project."
)
def weather_dag():
    @task.bash()
    def dbt_seed():
        return "cd /opt/airflow/dbt && dbt seed --profiles-dir . --target airflow"

    @task.bash()
    def dbt_run():
        return "cd /opt/airflow/dbt && dbt run --profiles-dir . --target airflow"

    @task.bash()
    def dbt_test():
        return "cd /opt/airflow/dbt && dbt test --profiles-dir . --target airflow"

    seed = dbt_seed()
    run = dbt_run()
    test = dbt_test()

    seed >> run >> test

weather_dag()
