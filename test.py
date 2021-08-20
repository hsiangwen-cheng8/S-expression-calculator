import unittest

from calc import calc


class testCalc(unittest.TestCase):
    def testNoFunc(self):
        self.assertEqual(calc("123"), 123)

    def testAdd(self):
        self.assertEqual(calc("(add 123 456)"), 579)
        self.assertEqual(calc("(add 1 1)"), 2)

    def testAddAdd(self):
        self.assertEqual(calc("(add 0 (add 3 4))"), 7)

    def testAddAddAdd(self):
        self.assertEqual(calc("(add 3 (add (add 3 3) 3))"), 12)

    def testMultiply(self):
        self.assertEqual(calc("(multiply 1 1)"), 1)

    def testMultiplyMultiply(self):
        self.assertEqual(calc("(multiply 0 (multiply 3 4))"), 0)
        self.assertEqual(calc("(multiply 2 (multiply 3 4))"), 24)

    def testMultiplyMultiplyMultiply(self):
        self.assertEqual(calc("(multiply 3 (multiply (multiply 3 3) 3))"), 81)

    def testMultiplyAdd(self):
        self.assertEqual(calc("(multiply (add 1 2) 3)"), 9)

    def testAddMultiply(self):
        self.assertEqual(calc("(add 1 (multiply 2 3))"), 7)

    def testMultiplyAddMultiply(self):
        self.assertEqual(calc("(multiply 2 (add (multiply 2 3) 8))"), 28)

    def testMultipleAddMultiply(self):
        self.assertEqual(calc("(add 1 2 3 4 (multiply 2 3 5))"), 40)
    
    def testAddMultipleAdd(self):
        self.assertEqual(calc("(add 1 (multiply (add 2 1) 3))"), 10)

    def testInvalidFuncArgs(self):
        with self.assertRaises(ValueError):
            calc("(add 1 (multiply (add 2 1) z))")

    def testInvalidFuncName(self):
        with self.assertRaises(Exception):
            calc("(Magic 1 (multiply (add 2 1) 1))")

    def testInvalidMultiply(self):
        with self.assertRaises(Exception):
            calc("(Add 1 (multiply )")
            calc("(Add 1 (multiply 1)")

    def testAllAdd(self):
        self.assertEqual(calc("(add (add 0 0) (add 0 0))"), 0)
        self.assertEqual(calc("(add (add 1 2) (add 3 4) (add 5 6))"), 21)
        self.assertEqual(calc("(add (multiply 1 2) (add 3 4))"), 9)
        self.assertEqual(calc("(add (add 1 2) (multiply 3 4))"), 15)
        self.assertEqual(calc("(multiply (add 1 2) (multiply 3 4))"), 36)



if __name__ == '__main__':
    unittest.main()
