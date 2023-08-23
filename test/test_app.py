import unittest
from app.multi import multiplicacion

class TestMulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiplicacion(4, 4), 16)

if __name__ == '__main__':
    unittest.main()
