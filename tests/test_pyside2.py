# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

def test_translate_and_UnicodeUTF8(PySide2, python_version):
    _str_ = str
    if python_version[0] == 2:
        _str_ = basestring

    from QtExt import QtWidgets

    # this does not exist in PySide2 by default
    assert QtWidgets.QApplication.UnicodeUTF8 is -1

    # use patched method with old arguments
    result = QtWidgets.QApplication.translate(
        u'Href_Gui',
        u'Text',
        u'None',
        QtWidgets.QApplication.UnicodeUTF8
    )
    assert isinstance(result, _str_)

    # use patched method with new arguments
    result = QtWidgets.QApplication.translate(
        u'SomeText',
        u'Form',
        u'None'
    )
    assert isinstance(result, _str_)


def test_qheaderview_forward_compatiblity(PySide2):
    from QtExt import QtWidgets
    assert QtWidgets.QHeaderView.setSectionResizeMode
    assert QtWidgets.QHeaderView.setResizeMode


def test_QtWebCompat_methods(PySide2):
    from QtExt import QtWebCompat
    web = QtWebCompat.QtWebPage
    assert hasattr(web, 'setProxy')

    view = QtWebCompat.QtWebView
    assert hasattr(view, 'evaluateJavaScript')


def test_is_webwidget_supported(PySide2):
    from QtExt import is_webwidget_supported