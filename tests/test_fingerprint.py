from pathlib import Path
from unittest import TestCase

import barch.commands.fingerprint
import barch.commands.fingerprint

TESTING = (Path(__file__).parent / '..' / 'testing').resolve()


# current_directory = os.path.split(path_to_current_file)[0]
# path_to_file = os.path.join(current_directory, "mydata.json")
# with open(path_to_file) as mydata:
#     my_json_data = json.load(mydata)

class TestFingerprint(TestCase):
    def test_fingerprint(self):
        assert (
                barch.commands.fingerprint.fingerprint(
                    TESTING / 'fingerprint.txt'
                ) == '20af7fdfb0586595'
        )
