# import xxhash as xx
from enum import Enum
from pathlib import Path

from loguru import logger


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


def fingerprint(fname):
    print(file_type(fname))
    # for path in Path(fname).iterdir():
    #     info = path.stat()
    #     print(info)

    # hash = xx.xxh64()
    # with open(fname, "rb") as f:
    #     for chunk in iter(lambda: f.read(4096), b""):
    #         hash.update(chunk)
    # return hash.hexdigest()
