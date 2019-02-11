import collections
import unittest
import mock

import command_line

Arg = collections.namedtuple('Arg', ['EXPRESSION'])

class TestPyCalcCommandLine(unittest.TestCase):

  def testInitArguments(self):
    py_calc_command_line = command_line.PyCalcCommandLine()
    py_calc_command_line._parser.add_argument = mock.MagicMock()
    py_calc_command_line._InitArguments()

    for name, arg in py_calc_command_line._ARGUMENTS.iteritems():
      py_calc_command_line._parser.add_argument.assert_called_once_with(
          name, help=arg.help)

  def testParseNominal(self):
    py_calc_command_line = command_line.PyCalcCommandLine()

    py_calc_command_line._parser.parse_args = mock.MagicMock()
    py_calc_command_line._parser.parse_args.return_value = Arg(
        EXPRESSION='3+4')
    py_calc_command_line.Parse()

    py_calc_command_line._parser.parse_args.assert_called_once_with()