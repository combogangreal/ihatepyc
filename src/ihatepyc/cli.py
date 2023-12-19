import click
from . import pycisbad

@click.group(name="ihatepyc")
def main():
    pass

@main.command(name="watch")
@click.option("--path", type=click.Path(exists=True), default=".", help="The directory to watch.")
@click.option("--interval", "-i", type=int, default=1, help="The interval to check for __pycache__ folders.")
@click.option("--recursive", "-r", is_flag=True, help="Whether to watch subdirectories.")
@click.option("--verbose", "-v", is_flag=True, help="Whether to print verbose output.")
def watch(path, interval, recursive, verbose):
    """Watches a directory and subdirectories for __pycache__ folders and deletes them."""
    watcher = pycisbad.Watcher(path, interval, recursive, verbose)
    watcher.start()