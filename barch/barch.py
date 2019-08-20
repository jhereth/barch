from pathlib import Path
from commands.fingerprint import fingerprint as _fingerprint
import click


@click.group()
def cli():
    """barch - Utility to support Backup and Archiving."""
    # click.echo('cli')
    pass


@cli.command()
@click.argument('file')
def fingerprint(file: str):
    """fingerprint of files."""
    fp = _fingerprint(Path(file))
    click.echo(f'fingerprint of {file} is {fp}.')


cli.add_command(fingerprint)

if __name__ == '__main__':
    cli()
