import shutil
import string
from pathlib import Path

import pytest
import pytest_check as check

import barch.commands.fingerprint as fp
from testing.create_data import create_directory_with_data
from .conftest import TESTING

SAMPLE_FINGERPRINT = fp.Fingerprint(
    filename='filename',
    path=Path('/some/path'),
    digest='digest'
)


class TestFingerprint:
    @pytest.fixture()
    def recursive_data(self):
        def _create_recursive_date(base_path: str) -> Path:

            path = create_directory_with_data(base_path)
            create_directory_with_data(base_path + "/subdir1", start=2, end=6)
            self.recursive_data_path = base_path
            return path

        yield _create_recursive_date
        shutil.rmtree(Path.cwd() / self.recursive_data_path)

    def test_xxh_format(self):
        """Match [xxhsum spec for 64bit](https://github.com/Cyan4973/xxHash/blob/v0.8.0/xxhsum.c#L1847-L1865)."""
        file_name = 'fingerprint.txt'
        # TODO(#10): Simplify Fingerprint Generation for single file
        s = fp.fingerprint(
            TESTING / file_name
        ).xxh_format()
        for c in s[:16]:
            check.is_in(c, string.hexdigits)
        check.equal(s[32:34], '  ')

    def test_fingerprint__works_recursively(self, recursive_data):
        dir = recursive_data("testing1")
        s = fp.fingerprint(dir)
        print(s)
        # assert False


class TestFingerprint_fingerprint:
    def test_fingerprint_single_file(self):
        file_name = 'fingerprint.txt'
        result = fp.fingerprint(
            TESTING / file_name
        )
        check.equal(result.filename, file_name, "correct filename")
        check.equal(result.digest, '86d37599cd7d43276456aa22aad48cee',
                       "correct digest")
