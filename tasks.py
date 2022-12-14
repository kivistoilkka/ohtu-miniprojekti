from invoke import task

@task
def run(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint --fail-under=9 src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)