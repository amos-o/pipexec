import subprocess

import typer


app = typer.Typer()


def setup(package):
    """
    Setup the environment.
    """
    typer.secho(f'Starting your {package} shell...', fg=typer.colors.GREEN)
    subprocess.call(['python3', '-m', 'venv', '.venv'])
    subprocess.call(['/bin/sh', '.venv/bin/activate'])
    subprocess.call(['pip', 'install', f'{package}'])


def teardown():
    """
    Remove the environment.
    """
    typer.secho('\nCleaning up...', fg=typer.colors.GREEN)
    subprocess.call(['rm', '-rf', '.venv'])
    typer.secho('Done', fg=typer.colors.GREEN)


@app.command()
def pipexec(package: str):
    setup(package)
    try:
        subprocess.call(['python3'])
        teardown()
    except KeyboardInterrupt:
        # handle exit from shell using CTRL + C
        teardown()


def main():
    app()
