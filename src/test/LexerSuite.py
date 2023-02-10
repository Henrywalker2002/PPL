import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test1(self):
        self.assertTrue(TestLexer.test("01","0,1,<EOF>",100))