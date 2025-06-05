import unittest
from solution import strict

class TestStrictDecorator(unittest.TestCase):
    @strict
    def sum_two(self, a: int, b: int) -> int:
        return a + b

    def test_valid_types(self):
        self.assertEqual(self.sum_two(1, 2), 3)
        self.assertEqual(self.sum_two(-1, 1), 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            self.sum_two(1, 2.4)
        with self.assertRaises(TypeError):
            self.sum_two("1", 2)
        with self.assertRaises(TypeError):
            self.sum_two(1, "2")

if __name__ == '__main__':
    unittest.main() 