import json
from pathlib import Path
from barch.commands.fingerprint import fingerprint as _fingerprint
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
    click.echo(fp.xxh_format())


@cli.command()
@click.argument("file")
def metadata(file: str):
    """collect metadata of file

    - size in bytes
    - access time
    - last modification time
    - creation time
    - filemode
    """
    md = _metadata(Path(file))
    click.echo(json.dumps(md))


cli.add_command(fingerprint)

if __name__ == '__main__':
    cli()
