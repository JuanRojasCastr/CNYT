import unittest
import ComplexCalculator
import Clasico_Cuantico


class TestComplexCalculator(unittest.TestCase):

    # Canicas con Booleanos

    def test_canicas(self):
        a = [[False, False, False, False, False, False], [False, False, False, False, False, False], [False, True, False, False, False, True], [False, False, False, True, False, False], [False, False, True, False, False, False], [True, False, False, False, True, False]]
        b = [[6], [2], [1], [5], [3], [10]]
        c = [[False, False, True], [True, False, False], [False, True, False]]
        d = [[3], [5], [2]]
        e = [[False, False, True], [False, True, False]]
        f = [[8], [4], [7]]

        self.assertEqual(Clasico_Cuantico.canicas(a, b, 1), [[0], [0], [12], [5], [1], [9]])
        self.assertEqual(Clasico_Cuantico.canicas(c, d, 1), [[2], [3], [5]])
        self.assertEqual(Clasico_Cuantico.canicas(e, f, 1), "Length error")

    def test_clasic(self):
        a = [[0, 1/6, 5/6], [1/3, 1/2, 1/6], [2/3, 1/3, 0]]
        b = [[1/6], [1/6], [2/3]]
        c = [[0, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0] , [0, 1/3, 0, 1, 0, 0, 0, 0], [0, 1/3, 0, 0, 1, 0, 0, 0], [0, 1/3, 1/3, 0, 0, 1, 0, 0], [0, 0, 1/3, 0, 0, 0, 1, 0], [0, 0, 1/3, 0, 0, 0, 0, 1]]
        d = [[1], [0], [0], [0], [0], [0], [0], [0]]
        e = [[0, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0] , [0, 1/3, 0, 1, 0, 0, 0, 0], [0, 1/3, 0, 0, 1, 0, 0, 0], [0, 1/3, 1/3, 0, 0, 1, 0, 0], [0, 0, 1/3, 0, 0, 0, 1, 0], [0, 0, 1/3, 0, 0, 0, 0, 1]]
        f = [[1], [0], [0], [0], [0], [0], [0]]

        self.assertEqual(Clasico_Cuantico.rendijas_clasico(a, b, 1), [[21/36], [9/36], [6/36]])
        self.assertEqual(Clasico_Cuantico.rendijas_clasico(c, d, 2), [[0], [0], [0], [1/6], [1/6], [1/3], [1/6], [1/6]])
        self.assertEqual(Clasico_Cuantico.rendijas_clasico(e, f, 1), "Length error")

    def test_cuantico(self):
        c1 = (-1 / (6 ** 0.5), 1 / (6 ** 0.5))
        c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
        c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))
        a = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
        b = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
        c = [[(1/(2 ** 0.5), 0), (1/(2 ** 0.5), 0), (0, 0)], [(0, -1/(2 ** 0.5)), (0, 1/(2 ** 0.5)), (0, 0)], [(0, 0), (0, 0), (0, 1)]]
        d = [[(1/(3 ** 0.5), 0)], [(0, 2/(15 ** 0.5))], [((2/5)**0.5, 0)]]

        self.assertEqual(Clasico_Cuantico.rendijas_cuantico(a, b, 2), [[(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(-0.20412414523193154, 0.20412414523193154)], [(-0.20412414523193154, -0.20412414523193154)], [(0.0, 0.0)], [(-0.20412414523193154, -0.20412414523193154)], [(0.20412414523193154, -0.20412414523193154)]])
        self.assertEqual(Clasico_Cuantico.rendijas_cuantico(a, b, 1), [[(0, 0)], [(0.5, 0.0)], [(0.5, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)]])
        self.assertEqual(Clasico_Cuantico.rendijas_cuantico(c, d, 4), [[(0.5468740243419739, -0.030476244847651823)], [(-0.5468740243419739, -0.030476244847651823)], [(0.6324555320336759, 0.0)]])

if __name__ == '__main__':
    unittest.main()