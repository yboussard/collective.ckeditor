# -*- coding: utf-8 -*-
## Copyright (C) 2009 Ingeniweb - all rights reserved    

from zope.testing import doctest
from unittest import TestSuite, main
from Testing import ZopeTestCase as ztc
from collective.ckeditor.tests.base import CKEditorTestCase



OPTIONFLAGS = (doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    tests = [ 'installation.txt',
              'controlpanel.txt',
              'ckeditor_jsconfig.txt',
              'uninstall.txt',
              'widget.txt',
             ]
    suite = TestSuite()
    for test in tests:
        suite.addTest(ztc.FunctionalDocFileSuite(test,
            optionflags=OPTIONFLAGS,
            package="collective.ckeditor.tests",
            test_class=CKEditorTestCase))
    return suite

