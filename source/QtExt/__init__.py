# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

import os
import sys

# Provide default resolution order for Qt
_default_resolution_older_ = 'PySide:PySide2'
os.environ['QT_PREFERRED_BINDING'] = _default_resolution_older_


def _pyqt4_():

    import Qt
    from Qt import QtWidgets

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode
    return Qt


def _pyqt5_():

    import Qt
    from Qt import QtWidgets

    # Monkey Patch for backward compatibility
    def setResizeMode(self, *args, **kwargs):
        return self.setSectionResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setResizeMode = setResizeMode

    # provide mocked UnicodeUTF8 For backward compatibility
    QtWidgets.QApplication.UnicodeUTF8 = -1

    old_translate_fn = QtWidgets.QApplication.translate

    def translate(context, key, disambiguation=None, encoding=None, n=0):
        return old_translate_fn(context, key, disambiguation, n)

    QtWidgets.QApplication.translate = staticmethod(translate)

    return Qt


def _pyside_():

    import Qt
    from Qt import QtWidgets

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    return Qt


def _pyside2_():

    import Qt
    from Qt import QtWidgets

    # Monkey Patch for backward compatibility
    def setResizeMode(self, *args, **kwargs):
        return self.setSectionResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setResizeMode = setResizeMode

    # provide mocked UnicodeUTF8 For backward compatibility
    QtWidgets.QApplication.UnicodeUTF8 = -1

    old_translate_fn = QtWidgets.QApplication.translate

    def translate(context, key, disambiguation=None, encoding=None, n=0):
        return old_translate_fn(context, key, disambiguation, n)

    QtWidgets.QApplication.translate = staticmethod(translate)

    return Qt

mapping = {
    'PyQt4': _pyqt4_,
    'PySide': _pyqt5_,
    'PyQt5': _pyside_,
    'PySide2': _pyside2_
}

from Qt import __binding__
patch_qt = mapping.get(__binding__)
sys.modules['QtExt'] = patch_qt()