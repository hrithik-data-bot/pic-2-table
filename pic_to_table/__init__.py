"""init module for pic_to_table"""

from pic_to_table import _version
from pic_to_table.app_logging import init_logging

init_logging()
VERSION = __version__ = _version.get_versions()['version']
