import subprocess

import typer


app = typer.Typer()


@app.command()
def pipexec(package: str):
    typer.echo(f'Starting your {package} shell...')
    subprocess.call(['python3', '-m', 'venv', '.venv'])
    subprocess.call(['/bin/sh', '.venv/bin/activate'])
    subprocess.call(['pip', 'install', f'{package}'])
    subprocess.call(['python3'])
    typer.echo('Cleaning up...')
    subprocess.call(['rm', '-rf', '.venv'])
    typer.echo('Done.')
    typer.echo('Bye!')


def main():
    app()
