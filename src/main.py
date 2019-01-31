"""Main file."""
from command_line import PyCalcCommandLine

if __name__ == '__main__':
  calc = PyCalcCommandLine()
  calc.Parse()
