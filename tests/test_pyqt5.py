
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


def test_qheaderview_pyqt5_forward_compatiblity(PyQt5):
    from QtExt import QtWidgets
    assert QtWidgets.QHeaderView.setSectionResizeMode
    assert QtWidgets.QHeaderView.setResizeMode
