# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

import os
import sys

# Provide default resolution order for Qt
_default_resolution_older_ = os.pathsep.join(['PySide', 'PySide2'])
os.environ.setdefault('QT_PREFERRED_BINDING', _default_resolution_older_)

from Qt import __binding__
import Qt


class QtWebMeta(type(Qt.QtCore.QObject)):

    def __new__(cls, name, bases, attrs):

        def get_framework():
            '''Check for available frameworks'''
            try:
                # QtWebEngineWidgets -- qt >= 5.6 webengine
                from Qt import QtWebEngineWidgets

                return {
                    'webkit': False,
                    'webpage': QtWebEngineWidgets.QWebEnginePage,
                    'webview': QtWebEngineWidgets.QWebEngineView
                }

            except ImportError:
                pass

            try:
                # QtWebKitWidgets -- qt < 5.6 webkit
                from Qt import QtWebKitWidgets

                return {
                    'webkit': True,
                    'webpage': QtWebKitWidgets.QWebPage,
                    'webview': QtWebKitWidgets.QWebView
                }
            except ImportError:
                pass

            try:
                # QtWebKit -- qt4 webkit
                from Qt import QtWebKit
                return {
                    'webkit': True,
                    'webpage': QtWebKit.QWebPage,
                    'webview': QtWebKit.QWebView
                }
            except ImportError:
                pass

        framework = get_framework()
        module = framework.get(name.lower())
        meta_bases = (module, bases[0])

        print meta_bases

        instance = super(QtWebMeta, cls).__new__(
            cls, name, meta_bases, attrs
        )

        setattr(
            instance, 'webkit', framework.get('webkit')
        )

        return instance


class WebPage(Qt.QtCore.QObject):
    __metaclass__ = QtWebMeta

    def setProxy(self, proxy):
        if self.webkit:
            self.networkAccessManager().setProxy(
                proxy
            )


class WebView(Qt.QtCore.QObject):
    __metaclass__ = QtWebMeta

    def evaluateJavaScript(self, javascript):
        if self.webkit:
            self.page().mainFrame().evaluateJavaScript(
                javascript
            )

        else:
            self.page().evaluateJavaScript(
                javascript
            )


def _pyqt4_():
    import Qt

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    # Remap QtSortFilterProxyModel from PyQt4.QtGui To PyQt4.QtCore.
    Qt.QtCore.QSortFilterProxyModel = Qt.QtGui.QSortFilterProxyModel

    # Provide a generic QtWebKitWidgets entry
    Qt.QtWebKitWidgets.QtWebView = WebView
    Qt.QtWebKitWidgets.QtWebPage = WebPage

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

    # Provide a generic QtWebKitWidgets entry
    Qt.QtWebKitWidgets.QtWebView = WebView
    Qt.QtWebKitWidgets.QtWebPage = WebPage

    return Qt


def _pyside_():
    import Qt

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    Qt.QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    # Provide a generic QtWebKitWidgets entry
    Qt.QtWebKitWidgets.QtWebView = WebView
    Qt.QtWebKitWidgets.QtWebPage = WebPage

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

    # Provide a generic QtWebKitWidgets entry
    Qt.QtWebKitWidgets.QtWebView = WebView
    Qt.QtWebKitWidgets.QtWebPage = WebPage

    return Qt


mapping = {
    'PyQt4': _pyqt4_,
    'PySide': _pyside_,
    'PyQt5': _pyqt5_,
    'PySide2': _pyside2_
}

patch_qt = mapping.get(__binding__)
sys.modules['QtExt'] = patch_qt()
