# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


PACKAGES_PATH = os.path.join(os.path.dirname(__file__), 'source')


class PyTest(TestCommand):
    '''Pytest command.'''

    def finalize_options(self):
        '''Finalize options to be used.'''
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        '''Import pytest and run.'''
        import pytest
        raise SystemExit(pytest.main(self.test_args))


# General configuration.
setup(
    name='QtExt',
    version='0.1.0',
    description='Qt framework extender',
    keywords='PyQt4, PyQt5, PySide, PySide2',
    url='https://bitbucket.org/ftrack/QtExt',
    author='ftrack',
    packages=find_packages(PACKAGES_PATH),
    license='Apache License (2.0)',
    package_dir={
        '': 'source'
    },
    setup_requires=[
        'Qt.py == 0.3.4',
        'sphinx >= 1.2.2, < 2',
        'sphinx_rtd_theme >= 0.1.6, < 2'
    ],
    install_requires=[
        'Qt.py == 0.3.3',
    ],
    tests_require=['pytest >= 2.3.5, < 3'],
    cmdclass={'test': PyTest}
)
