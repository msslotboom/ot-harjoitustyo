from invoke import task
@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src",pty=True)

@task
def coveragereport(ctx):
    ctx.run("coverage run --branch -m pytest src",pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)