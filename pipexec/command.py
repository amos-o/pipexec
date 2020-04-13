import subprocess

from cleo import Command


class PipexecCommand(Command):
    """
    Test a pip package

    pipexec
        {package? : The package name to test}
    """
    def handle(self):
        package = self.argument('package')
        self.line(f'<info>Starting your {package} shell...</info>')
        subprocess.call(['python3', '-m', 'venv', '.venv'])
        subprocess.call(['/bin/sh', '.venv/bin/activate'])
        subprocess.call(['pip', 'install', f'{package}'])
        subprocess.call(['python3'])
        subprocess.call(['rm', '-rf', '.venv'])
        self.line('<info>Bye!</info>')
