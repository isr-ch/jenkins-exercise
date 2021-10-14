import unittest
import Script2

class MyTestCase(unittest.TestCase):
    def test_word_size(self):
        self.assertEqual(Script2.longes_word(),10)
if __name__ == '__main__':
    unittest.main()
