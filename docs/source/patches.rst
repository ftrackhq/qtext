Patches
=======

Here a list of all the function and methods which has been patched or changed.
We'll be taking PySide/PyQt4 as base comparison for the changes and differences.


QApplication.UnicodeUTF8
------------------------

.. note::
    Deprecated on PySide2 / PyQt5

As UnicodeUTF8 has been deprecated we have been adding it back with a default value of -1



QApplication.translate
------------------------

.. note::
    Signature change on PySide2 / PyQt5

As the signature of this function has been changed, we are providing a simple remapping which does add back the extra argument.



QHeaderView.setResizeMode
-------------------------

.. note::
    Function renamed on PySide2 / PyQt5

As this function has been renamed, we are providing a remap to the new function.