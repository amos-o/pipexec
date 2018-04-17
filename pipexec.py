import argparse


parser = argparse.ArgumentParser(description="Create a shell with a pip package")

parser.add_argument('package_name', metavar='package_name', type=str,
                    help='The name of the package to be included in your shell environment')

arg = parser.parse_args()
