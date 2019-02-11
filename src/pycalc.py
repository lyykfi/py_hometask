"""Calculator."""
from math import sin


class PyCalc(object):
  """ Calculate match string. """

  # A valid operators.
  OPERATORS = set(['+', '-', '*', '/', '(', ')', 'abs', 'sin', 'round'])

  # A valid commands.
  COMMANDS = {
      '+': lambda stack: stack.pop() + stack.pop(),
      '-': lambda stack: stack.pop() - stack.pop(),
      '*': lambda stack: stack.pop() * stack.pop(),
      '/': lambda stack: stack.pop() / stack.pop(),
      '^': lambda stack: stack.pop() ** stack.pop(),
      'abs': lambda stack: abs(stack.pop()),
      'round': lambda stack: round(stack.pop()),
      'sin': lambda stack: sin(stack.pop())
  }

  # A special functs.
  FUNCTS = set(['abs', 'round', 'sin'])

  def __init__(self, expression):
    """Inits the class.

    Args:
      expression: A string with expression.
    """
    self._expression = expression

  def _PostfixEval(self, tokens):
    """Evaluate postfix array to result calculate.

    Args:
      tokens: A list with postfix symbols.

    Returns:
      A string with result.
    """
    s = []

    for symbol in tokens:
      if symbol.isdigit():
        s.append(int(symbol))
        plus = None
      if self.COMMANDS.get(symbol):
        plus = self.COMMANDS.get(symbol)(s)
      if plus is not None:
        s.append(plus)

    return s.pop()

  def _ToPostfix(self, infix):
    """Moves infix string to postfix.

    Args:
      infix: A infix string.

    Returns:
      A postfix string.
    """
    i = 0
    stack = []
    output = []
    len_infix = len(infix)
    number_ch = "0123456789"

    while i < len_infix:
      ch = infix[i]
      if ch in number_ch:
        num = ''
        j = i
        while j < len_infix:
          if not infix[j] in number_ch:
            j -= 1
            break
          else:
            num = num + infix[j]
          j += 1
        i = j
        output.append(num)
      elif ch == '(':
        stack.append(ch)
      elif ch == ')':
        top_token = stack.pop()
        while top_token != '(':
          output.append(top_token)
          top_token = stack.pop()
      else:
        j = i
        op = ''
        while j < len_infix:
          op = op + infix[j]
          if op in self.OPERATORS:
            break
          j += 1
        i = j

        stack_len = len(stack)
        while stack_len and stack[stack_len - 1] != '(':
          output.append(stack.pop())
          stack_len = len(stack)

        if op in self.OPERATORS:
          stack.append(op)

      i += 1

    while stack:
      output.append(stack.pop())

    return output


  def Parse(self):
    """Parsers for expression and return result.

    Return:
      Parsed result.
    """
    postfix = self._ToPostfix(self._expression)
    return self._PostfixEval(postfix)
