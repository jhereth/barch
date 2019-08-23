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
    def test_jsonify(self):
        d = json.loads(SAMPLE_FINGERPRINT.jsonify())
        for k in fp.Fingerprint.__dataclass_fields__.keys():
            with self.subTest(msg='contains key', key=k):
                ref = SAMPLE_FINGERPRINT.__getattribute__(k)
                if type(ref) in [str, int]:
                    assert d[k] == ref
                else:
                    assert d[k] == str(ref)

    def test_xxh_format(self):
        """Match [xxhsum spec for 64bit](https://github.com/Cyan4973/xxHash/blob/e22268617bb287e5b407b3c6cc29c1963c8d7c2d/xxhsum.c#L1219-L1231)."""
        file_name = 'fingerprint.txt'
        # TODO(#10): Simplify Fingerprint Generation for single file
        s = fp.fingerprint(
            TESTING / file_name
        )[0].xxh_format()
        assert all(c in string.hexdigits for c in s[:16])
        assert s[16:18] == '  '


class TestFingerprint_fingerprint(TestCase):
    def test_fingerprint_single_file(self):
        file_name = 'fingerprint.txt'
        result = fp.fingerprint(
            TESTING / file_name
        )
        with self.subTest(msg="only one result"):
            assert len(result) == 1
        with self.subTest(msg="correct filename"):
            assert result[0].filename == file_name
        with self.subTest(msg="correct digest"):
            assert result[0].digest == '20af7fdfb0586595'
