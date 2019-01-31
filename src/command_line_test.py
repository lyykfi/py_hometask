import unittest


class TestPyCalcCommandLine(unittest.TestCase):

  def testInit(self):
    self.assertEqual(self.proposal_row.row_index, 1)

    self.assertEqual(self.proposal_row.proposal_code, 'PROPOSAL-323')
    self.assertEqual(self.proposal_row.status, 'applied')
    self.assertEqual(self.proposal_row.decline_other, 'declined')
    self.assertEqual(self.proposal_row.comment, 'test_comment')