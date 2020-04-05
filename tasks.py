from invoke import task

@task
def test(c):
    c.run("coverage run -m unittest discover")

@task(test)
def cov(c):
    c.run("coverage report")
    c.run("coverage html")

@task
def gui(c):
    c.run("python program.py gui")

@task
def cli(c):
    c.run("python program.py")