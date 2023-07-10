'''
Author: Alphonse Brandon
Date Created: 09-07-2023
Subject: Ch6 - Working python functions
'''

import unittest
import city_names as cn

class TestPairs(unittest.TestCase):
    def test_city_country(self):
        name_pair = cn.city_country('Buea', 'Cameroon')
        returned = 'Buea, Cameroon'
        self.assertEqual(name_pair, returned)

if __name__ == '__main__':
    unittest.main()