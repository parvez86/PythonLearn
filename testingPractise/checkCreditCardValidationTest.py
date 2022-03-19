import unittest
from testingPractise.creditCardValidityCheck import *


class CreditCardValidationTest(unittest.TestCase):

    def setUp(self):
        print('Setup')

    def test_validation_valid(self):
        result = checkValidity(datetime.datetime.now(), datetime.datetime(2021, 1, 31, hour=23, minute=59, second=59))
        self.assertEqual('Valid', result)

    def test_validation_expired(self):
        with self.assertRaises(RuntimeError):
            checkValidity(datetime.datetime.now(), datetime.datetime(2020, 9, 30, hour=23, minute=59, second=59))
        # result = checkValidity(datetime.datetime.now(), datetime.datetime(2020, 9, 30, hour=23, minute=0, second=0))
        # self.assertEqual('Expired', result)

    def tearDown(self):
        print('Teardown')


if __name__ == '__main__':
        unittest.main()
