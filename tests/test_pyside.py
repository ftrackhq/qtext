
def test_translate_and_UnicodeUTF8(PySide, python_version):
    _str_ = str
    if python_version[0] == 2:
        _str_ = basestring

    from QtExt import QtWidgets

    # this does exist in PySide
    assert QtWidgets.QApplication.UnicodeUTF8 is not None

    # use patched method with old arguments
    result = QtWidgets.QApplication.translate(
        u'Href_Gui',
        u'Text',
        u'None',
        QtWidgets.QApplication.UnicodeUTF8
    )
    assert isinstance(result, _str_)


def test_qheaderview_pyside_forward_compatiblity(PySide):
    from QtExt import QtWidgets
    from QtExt import QtGui
    assert QtWidgets.QHeaderView.setSectionResizeMode
    assert QtWidgets.QHeaderView.setResizeMode
    assert QtGui.QHeaderView.setSectionResizeMode
    assert QtGui.QHeaderView.setResizeMode
