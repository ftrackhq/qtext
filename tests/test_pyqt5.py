# :coding: utf-8
# :copyright: Copyright (c) 2016 ftrack

def test_translate_and_UnicodeUTF8(PyQt5, python_version):
    _str_ = str
    if python_version[0] == 2:
        _str_ = basestring

    from QtExt import QtWidgets

    # this does not exist in PyQt5 by default
    assert QtWidgets.QApplication.UnicodeUTF8 is -1

    # use patched method with old arguments
    result = QtWidgets.QApplication.translate(
        u'SomeText',
        u'Form',
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


def test_qheaderview_forward_compatiblity(PyQt5):
    from QtExt import QtWidgets
    assert QtWidgets.QHeaderView.setSectionResizeMode
    assert QtWidgets.QHeaderView.setResizeMode


def test_QtWebCompat_QtWebPage_setProxy_methods(PyQt5):
    from QtExt import QtWebCompat
    web = QtWebCompat.QtWebPage
    assert hasattr(web, 'setProxy')


def test_QtWebCompat_QtWebView_evaluateJavaScript_methods(PyQt5):
    from QtExt import QtWebCompat
    view = QtWebCompat.QtWebView
    assert hasattr(view, 'evaluateJavaScript')


def test_is_webwidget_supported(PyQt5):
    from QtExt import is_webwidget_supported