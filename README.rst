QtExt
=====

QtExtender is built on top of Qt.py and laverage the differences from the various bindings,
simplifying the porting of code which has to work on more than one binding.


Testing
=======

As the module has to run on different binding the best way to do it is to run 
them from within a container.

build image
-----------

docker build -t ftrack/QtExtTest27 -f dockerfile-test-py27 .


run the tests
-------------

docker run --rm -v sandbox:. ftrack/QtExtTest27

