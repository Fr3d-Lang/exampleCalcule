###########    IMPORT     #######

import unittest
from mycode import *

import os

###########    MYTEST     ###########

class mytest(unittest.TestCase):
	def test_calculeSalaire(self):
		self.assertEqual(calculeSalaire('metier', 4), 2000)
		
##########    MAIN       ###########

if __name__ == "__main__" :
	unittest.main()


