import json
import string
from pathlib import Path
from unittest import TestCase

import barch.commands.fingerprint as fp
from .conftest import TESTING

SAMPLE_FINGERPRINT = fp.Fingerprint(
    filename='filename',
    path=Path('/some/path'),
    digest='digest'
)


class TestFingerprint(TestCase):
    def test_xxh_format(self):
        """Match [xxhsum spec for 64bit](https://github.com/Cyan4973/xxHash/blob/v0.8.0/xxhsum.c#L1847-L1865)."""
        file_name = 'fingerprint.txt'
        # TODO(#10): Simplify Fingerprint Generation for single file
        s = fp.fingerprint(
            TESTING / file_name
        ).xxh_format()
        assert all(c in string.hexdigits for c in s[:16])
        assert s[32:34] == '  '


class TestFingerprint_fingerprint(TestCase):
    def test_fingerprint_single_file(self):
        file_name = 'fingerprint.txt'
        result = fp.fingerprint(
            TESTING / file_name
        )
        with self.subTest(msg="correct filename"):
            assert result.filename == file_name
        with self.subTest(msg="correct digest"):
            assert result.digest == '86d37599cd7d43276456aa22aad48cee'
