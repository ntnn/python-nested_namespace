from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

from nested_namespace import __version__

setup(
    name='nested_namespace',
    version=__version__,

    # TODO: Add description
    description='Simple nested Namespaces',
    long_description=long_description,

    url='https://github.com/ntnn/python-nested_namespace',

    author='Nelo-T. Wallus',
    author_email='nelo@wallus.de',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='nested recursive namespace namespaces',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],
    extras_require={
        'test': [
            'pep8',
            'pylint',
            'pytest',
            'pytest-cov',
            'pytest-mock',
        ],
    },
)
