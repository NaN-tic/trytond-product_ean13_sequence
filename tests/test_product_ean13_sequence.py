#!/usr/bin/env python
# This file is part product_ean13_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductEAN13SequenceTestCase(ModuleTestCase):
    'Test Product EAN13 Sequence'
    module = 'product_ean13_sequence'

    def setUp(self):
        super(ProductEAN13SequenceTestCase, self).setUp()

    def test0005views(self):
        'Test views'
        test_view('product_ean13_sequence')

    def test0006depends(self):
        'Test depends'
        test_depends()

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductEAN13SequenceTestCase))
    return suite
