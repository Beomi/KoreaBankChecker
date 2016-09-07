import unittest
from KoreaBankChecker.kbstar import Transaction as kb


class TestBanking(unittest.TestCase):

    def test_kb(self):
        name = input('input Name: ')
        amount = input('input Amount: ')
        kbs = kb()
        self.assertTrue(kbs.check_paid(name,amount))


if __name__ == '__main__':
    unittest.main()