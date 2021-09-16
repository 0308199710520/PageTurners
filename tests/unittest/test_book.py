from unittest import TestCase
from book import Book

class test_Book(TestCase):
    def test_input(self):
        test = Book("Set In Darkness", "Ian Rankin", 5)
        self.assertEqual(test.score, 5)
        self.assertEqual(test.title, "Set In Darkness")
        self.assertEqual(test.author, "Ian Rankin")