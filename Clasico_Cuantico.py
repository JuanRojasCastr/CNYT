import ComplexCalculator

# Canicas con coeficientes Booleanos


def action_int(m1, v1):
    m = [[0 for i in range(len(v1[0]))] for j in range(len(m1))]
    for row in range(len(m1)):
        for column in range(len(v1[0])):
            for aux in range(len(m1[0])):
                m[row][column] = (m[row][column] + (m1[row][aux] * v1[aux][column]))
    return m


def m_bool_to_int(m1):
    for j in range(len(m1)):
        for i in range(len(m1[0])):
            if m1[i][j]:
                m1[i][j] = 1
            else:
                m1[i][j] = 0
    return m1


def canicas(m1, v1, t):
    if len(m1[0]) == len(v1) and len(m1[0]) == len(m1):
        m1 = m_bool_to_int(m1)
        while t > 0:
            v1 = action_int(m1, v1)
            t -= 1
        return v1
    else:
        return "Length error"

# Clasico Multiples Rendijas


def rendijas_clasico(m1, v1, t):
    if len(m1[0]) == len(v1) and len(m1[0]) == len(m1):
        while t > 0:
            v1 = action_int(m1, v1)
            t -= 1
        return v1
    else:
        return "Length error"


# Cuantico Rendijas


def action_complex(m1, v1):
    if len(m1[0]) == len(v1):
        m = [[(0, 0) for i in range(len(v1[0]))] for j in range(len(m1))]
        for row in range(len(m1)):
            for column in range(len(v1[0])):
                for aux in range(len(m1[0])):
                    m[row][column] = ComplexCalculator.add(m[row][column], ComplexCalculator.multi(m1[row][aux], v1[aux][column]))
        return m
    else:
        return "Length error"


def rendijas_cuantico(m1, v1, t):
    if len(m1[0]) == len(v1) and len(m1[0]) == len(m1):
        while t > 0:
            v1 = action_complex(m1, v1)
            t -= 1
        for i in range(len(v1)):
            v1[i][0] = ComplexCalculator.mod(v1[i][0]) ** 2
        return v1
    else:
        return "Length error"


c1 = (-1 / (6 ** 0.5), 1 / (6 ** 0.5))
c2 = (-1 / (6 ** 0.5), -1 / (6 ** 0.5))
c3 = (1 / (6 ** 0.5), -1 / (6 ** 0.5))
#print(rendijas_cuntico([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 1))


# Graficador

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def graficador(m1, v1, t):
    posiciones = [number for number in range(0, len(v1))]
    probabilidades = rendijas_cuantico(m1, v1, t)
    for index in range(len(probabilidades)):
        probabilidades[index] = probabilidades[index][0]
    fig, ax = plt.subplots()
    ax.set_ylabel('Probabilidades')
    ax.set_xlabel('Posiciones')
    ax.set_title('Probabilidades Sistema Cuantico')
    plt.bar(posiciones, probabilidades)
    plt.savefig('probabilidades_cuanticas.png')
    plt.show()


# graficador([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1 / 2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1 / 2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 2)


# print(rendijas_cuantico([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1 / 2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(1 / 2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]], 2))


# graficador([[(1/(2 ** 0.5), 0), (1/(2 ** 0.5), 0), (0, 0)], [(0, -1/(2 ** 0.5)), (0, 1/(2 ** 0.5)), (0, 0)], [(0, 0), (0, 0), (0, 1)]], [[(1/(3 ** 0.5), 0)], [(0, 2/(15 ** 0.5))], [((2/5)**0.5, 0)]], 4)