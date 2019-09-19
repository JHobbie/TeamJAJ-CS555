import unittest, datetime
import project04.src.utils as utils

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(utilsTestCase)
    return suite
class utilsTestCase(unittest.TestCase):
    def setUp(self):
        self.individual = {'NAME': ['Ginger /Bred/'], 'AGE': 49, 'FAMS': ['F01'], 'BIRT': [
            '10 AUG 1970'], 'SEX': ['F'], 'type': 'INDI', 'ID': 'I02', 'DEAT': ['7 OCT 2019']}

    def tearDown(self):
        self.individual = None

    def test_calcAge(self):
        currentDate = datetime.date(2000,8,10)
        calculatedAge = utils.calculateAge(self.individual, currentDate)
        self.assertEqual(calculatedAge, 30, 'Age was calculated as %d, when it was supposed to be 30' % (calculatedAge))

    def test_calcDate(self):
        dateObj = datetime.datetime(2000,8,10)
        calculatedDate = utils.calcDate("10 AUG 2000")
        self.assertEqual(calculatedDate, dateObj, "Date was calculated as %s when it should be %s" % (calculatedDate, dateObj))
if __name__ == '__main__':
    unittest.main()

