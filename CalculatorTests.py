import unittest
import ComplexCalculator


class TestComplexCalculator(unittest.TestCase):

    # ADD TEST

    def test_add(self):
        a = (-2, -1)
        b = (0, 3)
        c = (1, 4)
        d = (2, 5)

        self.assertEqual(ComplexCalculator.add(a, b), (-2, 2))
        self.assertEqual(ComplexCalculator.add(a, c), (-1, 3))
        self.assertEqual(ComplexCalculator.add(b, d), (2, 8))
        self.assertEqual(ComplexCalculator.add(d, c), (3, 9))

    # MULTIPLICATION TEST

    def test_multi(self):
        a = (-4, -1)
        b = (3, 0)
        c = (2, 5)
        d = (-3, 4)

        self.assertEqual(ComplexCalculator.multi(c, b), (6, 15))
        self.assertEqual(ComplexCalculator.multi(a, d), (16, -13))
        self.assertEqual(ComplexCalculator.multi(c, d), (-26, -7))
        self.assertEqual(ComplexCalculator.multi(b, c), (6, 15))

    # SUBTRACTION TEST

    def test_sub(self):
        a = (1, -1)
        b = (0, 2)
        c = (3, 6)
        d = (4, 2)

        self.assertEqual(ComplexCalculator.sub(a, b), (1, -3))
        self.assertEqual(ComplexCalculator.sub(b, c), (-3, -4))
        self.assertEqual(ComplexCalculator.sub(d, a), (3, 3))
        self.assertEqual(ComplexCalculator.sub(d, c), (1, -4))

    # DIVISION TEST

    def test_div(self):
        a = (6, -2)
        b = (0, 3)
        c = (2, 1)
        d = (-5, 4)

        self.assertEqual(ComplexCalculator.div(b, c), (0.6, 1.2))
        self.assertEqual(ComplexCalculator.div(a, c), (2, -2))
        self.assertEqual(ComplexCalculator.div(d, b), (1.333, 1.667))
        self.assertEqual(ComplexCalculator.div(a, d), (-0.927, -0.341))

    # CONJUGATE TEST

    def test_conj(self):
        a = (-2, -2)
        b = (1, 0)
        c = (3, 2)
        d = (-4, 3)

        self.assertEqual(ComplexCalculator.conj(a), (-2, 2))
        self.assertEqual(ComplexCalculator.conj(b), (1, 0))
        self.assertEqual(ComplexCalculator.conj(c), (3, -2))
        self.assertEqual(ComplexCalculator.conj(d), (-4, -3))

    # CARTESIAN TO POLAR TEST

    def test_polar(self):
        a = (-1, 2)
        b = (2, -3)
        c = (4, 3)
        d = (-5, -1)

        self.assertEqual(ComplexCalculator.polar(a), (2.24, 2.03))
        self.assertEqual(ComplexCalculator.polar(b), (3.61, 5.3))
        self.assertEqual(ComplexCalculator.polar(c), (5, 0.64))
        self.assertEqual(ComplexCalculator.polar(d), (5.1, 3.34))

    def test_cart(self):
        a = (2.24, 2.03)
        b = (3.61, 5.3)
        c = (5, 0.64)
        d = (5.1, 3.34)

        self.assertEqual(ComplexCalculator.cart(a), (-1, 2))
        self.assertEqual(ComplexCalculator.cart(b), (2, -3))
        self.assertEqual(ComplexCalculator.cart(c), (4, 3))
        self.assertEqual(ComplexCalculator.cart(d), (-5, -1))

    def test_phase(self):
        a = (-2, 1)
        b = (1, -3)
        c = (2, 2)
        d = (-4, -2)
        self.assertEqual(ComplexCalculator.phase(a), 2.68)
        self.assertEqual(ComplexCalculator.phase(b), 5.03)
        self.assertEqual(ComplexCalculator.phase(c), 0.79)
        self.assertEqual(ComplexCalculator.phase(d), 3.61)
