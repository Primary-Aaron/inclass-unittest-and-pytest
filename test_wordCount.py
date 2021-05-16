import unittest
import pytest
import wordCount

class test_wordCount(unittest.TestCase):
  def test_average1(self):
    clause = "my mother is epic"
    self.assertEqual(wordCount.wordCount(clause), 4)
  def test_average2(self):
    clause = "racecar  bumbum"
    self.assertEqual(wordCount.wordCount(clause), 2)
  def test_average3(self):
    clause = "Urmomsux"
    self.assertEqual(wordCount.wordCount(clause), 1)


def test_average3(self):
    clause = "bye bye, see you later "
    self.assertEqual(wordCount.wordCount(clause), 5)