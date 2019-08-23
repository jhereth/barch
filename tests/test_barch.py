from barch import __version__
import toml
from .conftest import TESTING


def test_version():
    """Make sure that module version is aligned with poetry config."""
    config = toml.load(TESTING / '../pyproject.toml')
    assert __version__ == config['tool']['poetry']['version']
