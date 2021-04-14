from prefect import task, Flow
import prefect


@task
def create_cluster():
    print("create_cluster")


@task
def run_spark_job():
    if True:
        raise RuntimeError()
    print("run_spark_job")


@task(trigger=prefect.triggers.always_run)
def tear_down_cluster():
    print("tear_down_cluster")


with Flow("Spark") as flow:
    create_cluster()
    run_spark_job()
    tear_down_cluster()

flow.run()
