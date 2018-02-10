try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from yt2mp3 import __version__

config = {
    'name': 'Yt2mp3',
    'description': 'Youtube to mp3 downloader',
    'author': 'Jim Filippou',
    'author_email': 'jimfilippou@hotmail.gr',
    'url': '',
    'download_url': '',
    'version': __version__,
    'packages': ['yt2mp3'],
    'install_requires': ['docutils', 'nose2'],
    'tests_require': ['Sphinx>=1.4.1,<2.0.0'],
}

setup(**config)