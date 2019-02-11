"""Unittests for pycalc."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import pycalc

class TestPyCalc(unittest.TestCase):

  def testToPostfixSimply(self):
    py_calc = pycalc.PyCalc('')
    result = py_calc._ToPostfix('3+4')

    self.assertEqual(result, ['3', '4', '+'])

  def testToPostfixNull(self):
    py_calc = pycalc.PyCalc('')
    result = py_calc._ToPostfix('')

    self.assertEqual(result, [])

  def testToPostfixNominal(self):
    py_calc = pycalc.PyCalc('')
    result = py_calc._ToPostfix('(4+2)*4')

    self.assertEqual(result, ['4', '2', '+', '4', '*'])

  def testToPostfixFail(self):
    py_calc = pycalc.PyCalc('')
    result = py_calc._ToPostfix('test')

    self.assertEqual(result, [])

  def testToPostfixSin(self):
    py_calc = pycalc.PyCalc('')
    result = py_calc._ToPostfix('sin(2+3)')

    self.assertEqual(result, ['2', '3', '+', 'sin'])

  def testParseNominal(self):
    py_calc = pycalc.PyCalc('(4+2)*4')
    result = py_calc.Parse()

    self.assertEqual(result, 24)

  def testParseNominal2(self):
    py_calc = pycalc.PyCalc('4+2')
    result = py_calc.Parse()

    self.assertEqual(result, 6)

  def testParseNominal3(self):
    py_calc = pycalc.PyCalc('(4+2)*(2+4)')
    result = py_calc.Parse()

    self.assertEqual(result, 36)

  def testParseNominal4(self):
    py_calc = pycalc.PyCalc('sin(4+2)')
    result = py_calc.Parse()

    self.assertEqual(result, -0.27941549819892586)