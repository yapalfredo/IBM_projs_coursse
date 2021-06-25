"""
Unit Testing For translator.py
"""
import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from translator import englishtofrench, englishtogerman

class TestTranslator(unittest.TestCase):
    """
    English to French Translation Test
    """
    def test_when_null(self):
        self.assertEqual(englishtofrench(""),"Argument Cannot Be Null or Empty") # test when argument is null output should be 'Argument Cannot Be Null or Empty'
    
    def test_when_null2(self):
        self.assertRaises(TypeError, englishtofrench(None), "Please check your argument")

    def test_word_hello(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour') # test when argument is 'Hello' ouput should be 'Bonjour'
        self.assertEqual(englishtofrench('Thanks'),'Merci') # test when argument is 'Thanks' ouput should be 'Merci'
    
    def test_word_thanks(self):
        self.assertNotEqual(englishtofrench('Thanks'),'Thanks') # test when argmuent is Thanks output should not be thanks
    """
    English to German Translation Test
    """
    def test_when_null_german(self):
        self.assertEqual(englishtogerman(""),"Argument Cannot Be Null or Empty") # test when argument is null output should be 'Argument Cannot Be Null or Empty'
    
    def test_when_null2_german(self):
        self.assertRaises(TypeError, englishtogerman(None), "Please check your argument")

    def test_word_hello_german(self):
        self.assertEqual(englishtogerman('Hello'),'Hallo') # test when argument is 'Hello' ouput should be 'Hallo'
        self.assertEqual(englishtogerman('Thank you'),'Danke.') # test when argument is 'Thanks' ouput should be 'Danke.'
        self.assertEqual(englishtogerman('Welcome'),'Begrüßung') # test when argument is 'Welcome' ouput should be 'Begrüßung'
    
    def test_word_thanks_german(self):
        self.assertNotEqual(englishtogerman('Thanks'),'Thanks') # test when argmuent is Thanks output should not be thanks

unittest.main()
