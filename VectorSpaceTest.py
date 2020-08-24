import unittest
import ComplexVectorSapces
import math

class TestComplexVectorSpaces(unittest.TestCase):

    # VECTOR ADD

    def test_v_add(self):
        a = [(1, 8), (-6, 4), (2, -1)]
        b = [(-3, 9), (4, -2), (7, 3)]
        c = [(12, 1), (5, -6), (1, -3)]
        d = [(2, -4), (2, -3), (9, 4)]

        self.assertEqual(ComplexVectorSapces.v_add(a, b), [(-2, 17), (-2, 2), (9, 2)])
        self.assertEqual(ComplexVectorSapces.v_add(a, c), [(13, 9), (-1, -2), (3, -4)])
        self.assertEqual(ComplexVectorSapces.v_add(b, d), [(-1, 5), (6, -5), (16, 7)])

    # VECTOR INVERSE ADD

    def test_v_inverse(self):
        a = [(1, 8), (-6, 4), (2, -1)]
        b = [(-3, 9), (4, -2), (7, 3)]
        c = [(12, 1), (5, -6), (1, -3)]

        self.assertEqual(ComplexVectorSapces.v_inv_add(a), [(0, 0), (0, 0), (0, 0)])
        self.assertEqual(ComplexVectorSapces.v_inv_add(b), [(0, 0), (0, 0), (0, 0)])
        self.assertEqual(ComplexVectorSapces.v_inv_add(c), [(0, 0), (0, 0), (0, 0)])

    # SCALAR MULT

    def test_scalar(self):
        a = [(10, 7), (7, 3)]
        b = [(-3, 9), (4, -2), (7, 3)]
        c = [(12, 1), (5, -6), (1, -3)]
        d = (3, 6)

        self.assertEqual(ComplexVectorSapces.v_scalar(d, a), [(-12, 81), (3, 51)])
        self.assertEqual(ComplexVectorSapces.v_scalar(d, b), [(-63, 9), (24, 18), (3, 51)])
        self.assertEqual(ComplexVectorSapces.v_scalar(d, c), [(30, 75), (51, 12), (21, -3)])

    # MATRIX ADD

    def test_m_add(self):
        a = [[(6, 5), (2, 1), (4, 3)], [(4, 4), (4, 4), (4, 4)]]
        b = [[(10, 1), (2, 3), (6, 7)], [(3, 2), (8, 2), (7, 5)]]
        c = [[(-1, 6), (8, -9), (0, 3)], [(0, 0), (8, 5), (-1, -5)]]

        self.assertEqual(ComplexVectorSapces.m_add(a, b), [[(16, 6), (4, 4), (10, 10)], [(7, 6), (12, 6), (11, 9)]])
        self.assertEqual(ComplexVectorSapces.m_add(a, c), [[(5, 11), (10, -8), (4, 6)], [(4, 4), (12, 9), (3, -1)]])
        self.assertEqual(ComplexVectorSapces.m_add(b, c), [[(9, 7), (10, -6), (6, 10)], [(3, 2), (16, 7), (6, 0)]])

    # MATRIX INVERSE

    def test_m_inv(self):
        a = [[(6, 5), (2, 1), (4, 3)], [(4, 4), (4, 4), (4, 4)]]
        b = [[(10, 1), (2, 3), (6, 7)], [(3, 2), (8, 2), (7, 5)]]
        c = [[(-1, 6), (8, -9), (0, 3)], [(0, 0), (8, 5), (-1, -5)]]

        self.assertEqual(ComplexVectorSapces.m_inv_add(a), [[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]])
        self.assertEqual(ComplexVectorSapces.m_inv_add(b), [[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]])
        self.assertEqual(ComplexVectorSapces.m_inv_add(c), [[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]])

    # MATRIX SCALAR MULTI

    def test_m_scalar(self):
        a = [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]]
        b = [[(4, 5), (1, 3)], [(1, 4), (3, 2)], [(4, 4), (4, 5)]]
        c = [[(2, 0), (5, 4)], [(4, 5), (3, 5)]]
        d = (1, 0)
        e = (-4, 2)
        f = (2, 3)

        self.assertEqual(ComplexVectorSapces.m_scalar(d, a), [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]])
        self.assertEqual(ComplexVectorSapces.m_scalar(e, b), [[(-26, -12), (-10, -10)], [(-12, -14), (-16, -2)], [(-24, -8), (-26, -12)]])
        self.assertEqual(ComplexVectorSapces.m_scalar(f, c), [[(4, 6), (-2, 23)], [(-7, 22), (-9, 19)]])

    # MATRIX/VECTOR TRANSPOSE

    def test_m_trans(self):
        a = [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]]
        b = [[(4, 5), (1, 3)], [(1, 4), (3, 2)], [(4, 4), (4, 5)]]
        c = [[(2, 0), (5, 4)], [(4, 5), (3, 5)]]
        d = [[(1, 0), (1, 3), (3, 2)]]

        self.assertEqual(ComplexVectorSapces.m_trans(a), [[(1, 0), (3, 4), (1, 4)], [(2, 0), (4, 5), (3, 2)]])
        self.assertEqual(ComplexVectorSapces.m_trans(b), [[(4, 5), (1, 4), (4, 4)], [(1, 3), (3, 2), (4, 5)]])
        self.assertEqual(ComplexVectorSapces.m_trans(c), [[(2, 0), (4, 5)], [(5, 4), (3, 5)]])
        self.assertEqual(ComplexVectorSapces.m_trans(d), [[(1, 0)], [(1, 3)], [(3, 2)]])

    # MATRIX/CONJUGATE

    def test_m_conj(self):
        a = [[(6, 5), (2, -1), (4, 3)], [(4, 4), (4, -4), (4, 4)]]
        b = [[(-10, 1), (2, 3), (-6, -7)], [(3, -2), (-8, 2), (7, -5)]]
        c = [[(-1, 6), (8, -9), (0, 3)], [(0, 0), (8, 5), (-1, -5)]]

        self.assertEqual(ComplexVectorSapces.m_conj(a), [[(6, -5), (2, 1), (4, -3)], [(4, -4), (4, 4), (4, -4)]])
        self.assertEqual(ComplexVectorSapces.m_conj(b), [[(-10, -1), (2, -3), (-6, 7)], [(3, 2), (-8, -2), (7, 5)]])
        self.assertEqual(ComplexVectorSapces.m_conj(c), [[(-1, -6), (8, 9), (0, -3)], [(0, 0), (8, -5), (-1, 5)]])

    # MATRIX/VECTOR ADJOINT

    def test_m_adj(self):
        a = [[(1, 0), (2, 0)], [(3, 4), (4, 5)], [(1, 4), (3, 2)]]
        b = [[(4, 5), (1, 3)], [(1, 4), (3, 2)], [(4, 4), (4, 5)]]
        c = [[(2, 0), (5, 4)], [(4, 5), (3, 5)]]
        d = [[(1, 0), (1, 3), (3, 2)]]

        self.assertEqual(ComplexVectorSapces.m_adj(a), [[(1, 0), (3, -4), (1, -4)], [(2, 0), (4, -5), (3, -2)]])
        self.assertEqual(ComplexVectorSapces.m_adj(b), [[(4, -5), (1, -4), (4, -4)], [(1, -3), (3, -2), (4, -5)]])
        self.assertEqual(ComplexVectorSapces.m_adj(c), [[(2, 0), (4, -5)], [(5, -4), (3, -5)]])
        self.assertEqual(ComplexVectorSapces.m_adj(d), [[(1, 0)], [(1, -3)], [(3, -2)]])

    # MATRIX MULTI

    def test_m_mult(self):
        a = [[(1, 0), (2, 0)], [(3, 4), (4, 5)]]
        b = [[(4, 5), (1, 3)], [(6, 7), (8, 9)]]
        c = [[(1, 0), (2, 0), (3, 5)], [(3, 4), (4, 5), (6, 9)]]
        d = [[(4, 5), (1, 3)], [(6, 7), (8, 9)]]
        e = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]
        f = [[(4, 5), (1, 3)], [(6, 7), (8, 9)]]

        self.assertEqual(ComplexVectorSapces.m_mul(a, b), [[(16, 19), (17, 21)], [(-19, 89), (-22, 89)]])
        self.assertEqual(ComplexVectorSapces.m_mul(c, d), "Length error")
        self.assertEqual(ComplexVectorSapces.m_mul(e, f), [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])

    # MATRIX ACTION

    def test_m_action(self):
        a = [[(-10, -1), (2, -3), (-6, 7)], [(3, 2), (-8, -2), (3, 2)]]
        b = [[(-1, 6), (8, -9), (0, 3)], [(0, 0), (8, 5), (-1, -5)]]
        c = [[(2, 4), (3, 4), (4, -7)], [(1, -4), (3, 4), (7, 5)]]
        d = [[(6, 5)], [(2, -1)], [(4, 3)]]
        e = [[(8, 1)], [(2, 3)], [(5, 2)]]
        f = [[(6, 5)], [(2, -1)], [(4, 3)]]

        self.assertEqual(ComplexVectorSapces.m_action(a, d), [[(-99, -54)], [(-4, 48)]])
        self.assertEqual(ComplexVectorSapces.m_action(b, e), [[(23, 68)], [(6, 7)]])
        self.assertEqual(ComplexVectorSapces.m_action(c, f), [[(39, 23)], [(49, 27)]])

    # INNER POINT

    def test_inner(self):
        a = [(3, 1), (2, 6), (7, 5), (3, 6)]
        b = [(4, 5), (1, 3), (29, 54), (31, 66)]
        c = [(1, 0), (1, 0), (0, 1), (0, 1)]
        d = [(6, 2), (3, 2), (2, 4), (1, 6)]
        e = [(0, 0), (0, 0), (0, 0), (0, 0)]
        f = [(2, 8), (7, 5), (9, 5), (1, 4)]

        self.assertEqual(ComplexVectorSapces.v_inner(a, b), (-379, 938))
        self.assertEqual(ComplexVectorSapces.v_inner(c, d), (-1, 7))
        self.assertEqual(ComplexVectorSapces.v_inner(e, f), (0, 0))

    # VECTOR NORM

    def test_v_norm(self):
        a = [(4, 2), (2, 6), (6, 3), (7, 8)]
        b = [(5, 1), (4, 2), (6, 3), (1, 7)]
        c = [(4, 5), (1, 3), (29, 54), (31, 66)]

        self.assertEqual(ComplexVectorSapces.v_norm(a), 14.76)
        self.assertEqual(ComplexVectorSapces.v_norm(b), 11.87)
        self.assertEqual(ComplexVectorSapces.v_norm(c), 95.52)

    # DISTANCE BETWEEN VECTORS

    def test_dist(self):
        a = [(5, 1), (4, 2), (6, 3), (1, 7)]
        b = [(3, 1), (2, 6), (7, 5), (3, 6)]
        c = [(1, 0), (2, 0)]
        d = [(3, 4), (4, 5)]
        e = [(4, 5), (1, 3)]
        f = [(3, 4), (4, 5)]

        self.assertEqual(ComplexVectorSapces.v_dist(a, b), 5.83)
        self.assertEqual(ComplexVectorSapces.v_dist(c, d), 7.0)
        self.assertEqual(ComplexVectorSapces.v_dist(e, f), 3.88)

    # UNITARY MATRIX

    def test_unit(self):
        a = [[(2/3, 0.0), (-2/3, 1/3)], [(2/3, 1/3), (2/3, 0.0)]]
        b = [[(0, 0), (0, 1)], [(0, 1), (0, 0)]]
        c = [[(1, 0), (2, 1)], [(0, 1), (0, 2)]]

        self.assertEqual(ComplexVectorSapces.m_unit(a), 'Is Unitary')
        self.assertEqual(ComplexVectorSapces.m_unit(b), 'Is Unitary')
        self.assertEqual(ComplexVectorSapces.m_unit(c), 'Is not Unitary')

    # HERMITIAN MATRIX

    def test_hermitian(self):
        a = [[(4, 0), (1, 8)], [(1, -8), (-2, 0)]]
        b = [[(7, 0), (4, 3)], [(4, -3), (5, 0)]]
        c = [[(2, 0), (2, 2)], [(2, -2), (3, 0)]]
        d = [[(3, 2), (3, 6)], [(3, -6), (-3, 2)]]

        self.assertEqual(ComplexVectorSapces.m_herm(a), "Is hermitian")
        self.assertEqual(ComplexVectorSapces.m_herm(b), "Is hermitian")
        self.assertEqual(ComplexVectorSapces.m_herm(c), "Is hermitian")
        self.assertEqual(ComplexVectorSapces.m_herm(d), "Is not hermitian")

    # TENSOR MATRIX

    def test_tensor(self):
        a = [[(2, 4), (3, 6)], [(-3, 0), (2, 2)]]
        b = [[(1, 0), (3, 4)], [(10, 2), (2, 5)]]
        c = [[(3, 2), (5, -1), (0, 2)], [(0, 0), (12, 0), (6, -3)], [(2, 0), (4, 4), (9, 3)]]
        d = [[(1, 0), (3, 4), (5, -7)], [(10, 2), (6, 0), (2, 5)], [(0, 0), (1, 0), (2, 9)]]

        # c, d is a book exercise

        self.assertEqual(ComplexVectorSapces.m_tensor(a, b), [[[[(2, 4), (-10, 20)], [(12, 44), (-16, 18)]], [[(3, 6), (-15, 30)], [(18, 66), (-24, 27)]]], [[[(-3, 0), (-9, -12)], [(-30, -6), (-6, -15)]], [[(2, 2), (-2, 14)], [(16, 24), (-6, 14)]]]])
        self.assertEqual(ComplexVectorSapces.m_tensor(c, d), [[[[(3, 2), (1, 18), (29, -11)], [(26, 26), (18, 12), (-4, 19)], [(0, 0), (3, 2), (-12, 31)]], [[(5, -1), (19, 17), (18, -40)], [(52, 0), (30, -6), (15, 23)], [(0, 0), (5, -1), (19, 43)]], [[(0, 2), (-8, 6), (14, 10)], [(-4, 20), (0, 12), (-10, 4)], [(0, 0), (0, 2), (-18, 4)]]], [[[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]], [[(12, 0), (36, 48), (60, -84)], [(120, 24), (72, 0), (24, 60)], [(0, 0), (12, 0), (24, 108)]], [[(6, -3), (30, 15), (9, -57)], [(66, -18), (36, -18), (27, 24)], [(0, 0), (6, -3), (39, 48)]]], [[[(2, 0), (6, 8), (10, -14)], [(20, 4), (12, 0), (4, 10)], [(0, 0), (2, 0), (4, 18)]], [[(4, 4), (-4, 28), (48, -8)], [(32, 48), (24, 24), (-12, 28)], [(0, 0), (4, 4), (-28, 44)]], [[(9, 3), (15, 45), (66, -48)], [(84, 48), (54, 18), (3, 51)], [(0, 0), (9, 3), (-9, 87)]]]])