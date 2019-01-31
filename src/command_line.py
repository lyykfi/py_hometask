"""Command line parser."""

import argparse
from collections import namedtuple

import pycalc


# Arg named tuple.
_Arg = namedtuple('Arg', ('help',))


class PyCalcCommandLine(object):
  """A class for definition command line."""
  _DESCRIPTION = 'Pure-python command-line calculator.'
  _ARGUMENTS = {
      'EXPRESSION': _Arg(help='expression string to evaluate', )}

  def __init__(self):
    """Inits the class."""
    self._parser = argparse.ArgumentParser(description=self._DESCRIPTION)
    self._InitArguments()

  def _InitArguments(self):
    """ Inits arguments for args parser."""
    for name, arg in self._ARGUMENTS.iteritems():
      self._parser.add_argument(name, help=arg.help)

  def Parse(self):
    """ Parses arguments and parse expression."""
    args = self._parser.parse_args()

    py_calc = pycalc.PyCalc(args.EXPRESSION)
    print py_calc.Parse()
