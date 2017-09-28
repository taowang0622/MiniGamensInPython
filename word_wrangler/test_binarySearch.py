from unittest import TestCase
import word_wrangler

class TestBinarySearch(TestCase):
    def test_binarySearch(self):
        self.assertEqual(True, word_wrangler.binary_search([1, 2, 3, 4, 5], 5))