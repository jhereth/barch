from dataclasses import dataclass
from pathlib import Path

import xxhash as xx
from loguru import logger

from barch.utils import file_type


@dataclass
class Fingerprint:
    filename: str
    path: Path
    digest: str

    def xxh_format(self) -> str:
        return f'{self.digest}  {self.path}/{self.filename}'


def fingerprint(file_name: Path) -> Fingerprint:
    logger.debug(file_type(file_name))

    hash = xx.xxh3_128(seed=0)
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return Fingerprint(
        filename=file_name.name,
        path=file_name.absolute().parent,
        digest=hash.hexdigest()
    )
