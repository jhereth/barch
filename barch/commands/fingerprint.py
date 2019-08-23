from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Sequence

import xxhash as xx
from loguru import logger


@dataclass
class Fingerprint:
    filename: str
    path: Path
    digest: str

    def jsonify(self) -> str:
        return ('{' +
                f'"filename": "{self.filename}", ' +
                f'"path": "{self.path}", ' +
                f'"digest": "{str(self.digest)}"' +
                '}')

    def xxh_format(self) -> str:
        return f'{self.digest}  {self.path}/{self.filename}'


class FileType(Enum):
    STANDARD = 0
    FILE_LINK = 1
    DIRECTORY = 10
    OTHER = -1


def file_type(file: Path) -> FileType:
    if not file.exists():
        logger.exception(f'{file} does not exist.')
        raise FileNotFoundError(f'{file} does not exist.')
    if file.is_file():
        if file.is_symlink():
            return FileType.FILE_LINK
        return FileType.STANDARD
    if file.is_dir():
        return FileType.DIRECTORY
    return FileType.OTHER


def fingerprint(file_name: Path) -> Sequence[Fingerprint]:
    logger.debug(file_type(file_name))
    # for path in Path(fname).iterdir():
    #     info = path.stat()
    #     print(info)

    hash = xx.xxh64()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return [Fingerprint(
        filename=file_name.name,
        path=file_name.absolute().parent,
        digest=hash.hexdigest()
    )]
