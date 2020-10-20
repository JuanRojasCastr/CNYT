import unittest
import TeoriaCuantica


class TestComplexCalculator(unittest.TestCase):

    #PORBABILITIES TEST

    def test_prob(self):
        a = [(-3, -1), (0, -2), (0, 1), (2, 0)]
        b = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
        self.assertEqual(TeoriaCuantica.probabilities(a, 2), 5.26)
        self.assertEqual(TeoriaCuantica.probabilities(b, 7), 10.87)
        self.assertEqual(TeoriaCuantica.probabilities(b, 8) == TeoriaCuantica.probabilities(b, 4), True)

    # AMPLITUD TEST

    def test_amplitud(self):
        a = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
        b = [[(0, 0)], [(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
        c = [[(2, 1)], [(-1, 2)], [(0, 1)], [(1, 0)], [(3, -1)], [(2, 0)], [(0, -2)], [(-2, 1)], [(1, -3)], [(0, -1)]]
        d = [[(-1, -4)], [(2, -3)], [(-7, 6)], [(-1, 1)], [(-5, -3)], [(5, 0)], [(5, 8)], [(4, -4)], [(8, -7)], [(2, -7)]]
        self.assertEqual(TeoriaCuantica.amplitud(a, b), (0, 0))
        self.assertEqual(TeoriaCuantica.amplitud(c, d), (-0.02, -0.13))

    # HERMITAIN

    def test_hermitain(self):
        a = [[(4, 0), (1, 8)], [(1, -8), (-2, 0)]]
        b = [[(7, 0), (4, 3)], [(4, -3), (5, 0)]]
        c = [[(2, 0), (2, 2)], [(2, -2), (3, 0)]]
        d = [[(3, 2), (3, 6)], [(3, -6), (-3, 2)]]

        self.assertEqual(TeoriaCuantica.m_herm(a), True)
        self.assertEqual(TeoriaCuantica.m_herm(b), True)
        self.assertEqual(TeoriaCuantica.m_herm(c), True)
        self.assertEqual(TeoriaCuantica.m_herm(d), False)

    # MEDIA

    def test_media(self):
        a = [[(0, 0),(0, -1)],[(0, 1),(0, 0)]]
        b = [(1/(2**(1/2)), 0), (0, 1/(2**(1/2)))]

        self.assertEqual((TeoriaCuantica.media(a, b)), (1.0, 0.0))

    # VARIANZA

    def test_varianza(self):
        a = [[(0, 0),(0, -1)],[(0, 1),(0, 0)]]
        b = [(1/(2**(1/2)), 0), (0, 1/(2**(1/2)))]

        self.assertEqual(TeoriaCuantica.varianza(a, b), (0.0, 0.0))

    # VALORES PROPIOS

    def test_valuores_vectors(self):
        a = [[0j, 1 + 0j], [1 + 0j, 0j]]
        b = [[0j, -1j], [1j, 0j]]
        c = [[0j, -1j, 2 - 2j], [2 + 1j, 2 + 5j, 1 + 7j], [1j, 2 + 7j, 3 + 5j]]
        d = ([(0.9999999999999996, 0.0), (-0.9999999999999999, 0.0)], [[(0.7071067811865474, -0.0), (0.7071067811865475, 0.0)], [(0.7071067811865476, 0.0), (-0.7071067811865475, 0.0)]])
        e = ([(0.9999999999999996, 0.0), (-0.9999999999999999, 0.0)], [[(-0.0, -0.7071067811865474), (0.7071067811865475, 0.0)], [(0.7071067811865476, 0.0), (0.0, -0.7071067811865475)]])
        f = (([(4.047014267690816, 11.56808775119902), (0.45775009249001486, 1.0575606085180616), (0.49523563981917584, -2.6256483597170743)], [[(-0.1194235325816442, -0.1745690207462312), (0.8817486259374302, 0.0), (-0.2840793435801329, -0.36742009674251547)], [(0.6577790765758859, 0.10591486483377263), (-0.16720273561834997, -0.2581033052677608), (0.6653374599840982, 0.0)], [(0.7151030727717798, 0.0), (-0.025894014361110187, 0.35675592453289107), (-0.5836681464021171, 0.030967051493920192)]]))

        self.assertEqual(TeoriaCuantica.valores_vectores(a), d)
        self.assertEqual(TeoriaCuantica.valores_vectores(b), e)
        self.assertEqual(TeoriaCuantica.valores_vectores(c), f)

    # DINAMICA
    def test_dinamica(self):
        a = [[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)], [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (-1 / (2 ** (1 / 2)), 0)], [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)], [(0, 0), (-1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)]]
        b = [(1, 0), (0, 0), (0, 0), (0, 0)]
        c = [[(0, 1), (0, 0)], [(0, 0), (0, 1)]]
        d = [(1, 0), (0, 0)]
        e = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]

        self.assertEqual(TeoriaCuantica.dinamica(a, b, 1), "Matriz no valida")
        self.assertEqual(TeoriaCuantica.dinamica(c, d, 1), [[(0, 1)], [(0, 0)]])
        self.assertEqual(TeoriaCuantica.dinamica(e, d, 1), [[(1, 0)], [(0, 0)]])
