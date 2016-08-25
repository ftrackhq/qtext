import os
import sys
import pytest


@pytest.fixture
def python_version():
    return sys.version_info


@pytest.fixture
def pyside():
    os.environ["QT_PREFERRED_BINDING"] = "PySide"

    def finalizer():
        os.environment.pop('QT_PREFERRED_BINDING')


@pytest.fixture
def pyside2():
    os.environ["QT_PREFERRED_BINDING"] = "PySide2"

    def finalizer():
        os.environment.pop('QT_PREFERRED_BINDING')


@pytest.fixture
def pyqt4():
    os.environ["QT_PREFERRED_BINDING"] = "PyQt4"

    def finalizer():
        os.environment.pop('QT_PREFERRED_BINDING')


@pytest.fixture
def pyqt5():
    os.environ["QT_PREFERRED_BINDING"] = "PyQt5"

    def finalizer():
        os.environment.pop('QT_PREFERRED_BINDING')
