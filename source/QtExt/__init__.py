# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack
import sys

from Qt import __binding__


def _pyqt4_():
    import Qt

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    # Remap QtSortFilterProxyModel from PyQt4.QtGui To PyQt4.QtCore.
    Qt.QtCore.QSortFilterProxyModel = Qt.QtGui.QSortFilterProxyModel

    return Qt


def _pyqt5_():
    import Qt

    # Monkey Patch for backward compatibility
    def setResizeMode(self, *args, **kwargs):
        return self.setSectionResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setResizeMode = setResizeMode

    # provide mocked UnicodeUTF8 For backward compatibility
    Qt.QtWidgets.QApplication.UnicodeUTF8 = -1

    old_translate_fn = Qt.QtWidgets.QApplication.translate

    def translate(context, key, disambiguation=None, encoding=None, n=0):
        return old_translate_fn(context, key, disambiguation, n)

    Qt.QtWidgets.QApplication.translate = staticmethod(translate)

    return Qt


def _pyside_():
    import Qt

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    return Qt


def _pyside2_():
    import Qt

    # Monkey Patch for backward compatibility
    def setResizeMode(self, *args, **kwargs):
        return self.setSectionResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setResizeMode = setResizeMode

    # provide mocked UnicodeUTF8 For backward compatibility
    Qt.QtWidgets.QApplication.UnicodeUTF8 = -1

    old_translate_fn = Qt.QtWidgets.QApplication.translate

    def translate(context, key, disambiguation=None, encoding=None, n=0):
        return old_translate_fn(context, key, disambiguation, n)

    Qt.QtWidgets.QApplication.translate = staticmethod(translate)

    return Qt

mapping = {
    'PyQt4': _pyqt4_,
    'PySide': _pyside_,
    'PyQt5': _pyqt5_,
    'PySide2': _pyside2_
}

patch_qt = mapping.get(__binding__)
sys.modules['QtExt'] = patch_qt()