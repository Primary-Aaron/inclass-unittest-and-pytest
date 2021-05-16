import unittest
import pytest
import Palindrome

class test_palindrome(unittest.TestCase):
  def test_average1(self):
    word = "racecar"
    self.assertEqual(Palindrome.isPalindrome(word), True)
  def test_average2(self):
    word = "racecar  "
    self.assertEqual(Palindrome.isPalindrome(word), True)
  def test_average3(self):
    word = "raceasdfcar  "
    self.assertEqual(Palindrome.isPalindrome(word), False)


def test_palindrome_true():
  assert Palindrome.isPalindrome("racecar") is True