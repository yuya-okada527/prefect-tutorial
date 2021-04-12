from prefect import task, Flow, Parameter


@task
def add(x, y=1):
    return x + y


@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))


with Flow("My first flow!") as flow:
    name = Parameter("name")
    say_hello(name)

state = flow.run(name="Marvin")
