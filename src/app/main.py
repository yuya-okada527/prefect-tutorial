from prefect import task, Flow


@task
def add(x, y=1):
    return x + y


@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))


with Flow("My first flow!") as flow:
    first_result = add(1, y=2)
    second_result = add(x=first_result, y=100)

state = flow.run()
