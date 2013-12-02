# -*- coding: utf-8 -*-
#
# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

"""
Tests for AMF Remoting AMF0 style.

@since: 0.6
"""

import unittest

from pyamf import remoting
from pyamf.remoting import amf0


class MockGateway(object):
    """
    """

    debug = True


class BaseTestCase(unittest.TestCase):
    """
    Provides a L{processor} attribute.
    """

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.gateway = MockGateway()
        self.processor = amf0.RequestProcessor(self.gateway)


class ExceptionTestCase(BaseTestCase):
    """
    Tests exception handling
    """

    def generate_exception(self, msg='foobar'):
        try:
            raise NameError(msg)
        except NameError:
            import sys

            return sys.exc_info()

    def test_debug(self):
        self.assertTrue(self.gateway.debug)

        response = self.processor.buildErrorResponse(None, error=self.generate_exception())

        self.assertEqual(response.status, remoting.STATUS_ERROR)

        error = response.body

        self.assertEqual(error.level, 'error')
        self.assertEqual(error.code, 'NameError')
        self.assertEqual(error.description, 'foobar')
        self.assertTrue(isinstance(error.details, list))

    def test_no_debug(self):
        self.gateway.debug = False

        response = self.processor.buildErrorResponse(None, error=self.generate_exception())

        self.assertEqual(response.status, remoting.STATUS_ERROR)

        error = response.body

        self.assertEqual(error.level, 'error')
        self.assertEqual(error.code, 'NameError')
        self.assertEqual(error.description, 'foobar')
        self.assertEqual(error.details, None)

    def test_utf_8_exception(self):
        msg = 'oh no ☹!'
        response = self.processor.buildErrorResponse(
            None, error=self.generate_exception(msg))
        error = response.body
        self.assertEqual(error.description, msg.decode('utf-8'))

    def test_unicode_exception(self):
        msg = u'oh no ☹!'
        response = self.processor.buildErrorResponse(
            None, error=self.generate_exception(msg))
        error = response.body
        self.assertEqual(error.description, msg)
