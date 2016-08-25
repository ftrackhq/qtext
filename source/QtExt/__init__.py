from Qt import __binding__


def _pyqt4_():
    import Qt as QtExt
    from QtExt import QtWidgets

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode
    return QtExt


def _pyqt5_():
    import Qt as QtExt
    from QtExt import QtWidgets

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

    return QtExt


def _pyside_():
    import Qt as QtExt
    from QtExt import QtWidgets

    # Monkey Patch for forward compatibility
    def setSectionResizeMode(self, *args, **kwargs):
        return self.setResizeMode(*args, **kwargs)

    QtWidgets.QHeaderView.setSectionResizeMode = setSectionResizeMode

    return QtExt


def _pyside2_():
    import Qt as QtExt
    from QtExt import QtWidgets

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

    return QtExt


mapping = {
    'pyqt4': _pyqt4_,
    'pyqt5': _pyqt5_,
    'pyside': _pyside_,
    'pyside2': _pyside2_
}


patch_it = mapping.get(__binding__)
patch_it()