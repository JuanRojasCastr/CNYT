import math
import ComplexCalculator

def f_aux(product):
    aux = 0
    if product[0][0][0] != 1 and product[0][1][0] == 0:
            if product[0][0][0] > 0:
                aux = (1/(product[0][0][0]))
            elif product[0][0][0] < 0:
                aux = (-1/(product[0][0][0]))
    return aux

def length(v1, v2):
    if len(v1) == len(v2):
        return True
    else:
        return False


def diagonal(m):
    mI = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                mI[i][j] = (1, 0)
    return mI


def conj_tup(c1):
    re = c1[0]
    im = c1[1] * -1
    res = re, im
    return res


# VECTOR ADD

def v_add(v1, v2):
    if length(v1, v2):
        m = []
        for index in range(len(v1)):
            m += [ComplexCalculator.add(v1[index], v2[index])]
        return m
    else:
        return 'Error: Different length vector'


# VECTOR INVERSE ADD

def v_inv_add(v1):
    m = []
    for index in range(len(v1)):
        m += [ComplexCalculator.sub(v1[index], v1[index])]
    return m


# VECTOR SCALAR MULTIPLICATION

def v_scalar(sc, v1):
    m = []
    for index in range(len(v1)):
        m += [ComplexCalculator.multi(sc, v1[index])]
    return m


# MATRIX ADD

def m_add(m1, m2):
    m = []
    if length(m1, m2):
        for row in range(len(m1)):
            m += [v_add(m1[row], m2[row])]
        return m
    else:
        return 'Error: Different length vector'


# MATRIX INVERSE ADD

def m_inv_add(m1):
    m = []
    for row in range(len(m1)):
        m += [v_inv_add(m1[row])]
    return m


# MATRIX SCALAR MULTIPLICATION

def m_scalar(sc, m1):
    m = []
    for row in range(len(m1)):
        m += [v_scalar(sc, m1[row])]
    return m


# MATRIX/VECTOR TRANSPOSE

def m_trans(m1):
    m = [[(0, 0) for i in range(len(m1))] for j in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m[j][i] = m1[i][j]
    return m


# MATRIX/VECTOR CONJUGATE

def m_conj(m1):
    m2 = [[(0, 0) for j in range(len(m1[0]))] for i in range(len(m1))]
    for row in range(len(m1)):
        for column in range(len(m1[0])):
            m2[row][column] = conj_tup(m1[row][column])
    return m2


# MATRIX/VECTOR ADJOINT

def m_adj(m1):
    m2 = [[m1[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    m2 = m_conj(m2)
    m2 = m_trans(m2)
    return m2


# MATRIX MULTIPLICATION

def m_mul(m1, m2):

    if len(m1[0]) == len(m2):
        m = [[(0, 0) for i in range(len(m2[0]))] for j in range(len(m1))]
        for row in range(len(m1)):
            for column in range(len(m2[0])):
                for aux in range(len(m1[0])):
                    m[row][column] = ComplexCalculator.add(m[row][column], ComplexCalculator.multi(m1[row][aux], m2[aux][column]))
        return m
    else:
        return "Length error"


# MATRIX ACTION

def m_action(m1, v1):
    return m_mul(m1, v1)


# INNER POINT

def v_inner(v1, v2):
    point = (0, 0)
    if length(v1, v2):
        for index in range(len(v1)):
            aux = ComplexCalculator.multi(v1[index], v2[index])
            point = ComplexCalculator.add(point, aux)
        return point
    else:
        return "Length error"


# VECTOR NORM

def v_norm(v1):
    aux = 0
    for index in range(len(v1)):
        aux += (ComplexCalculator.mod(v1[index])**2)
    return round(math.sqrt(aux), 2)


# DISTANCE BETWEEN VECTORS

def v_dist(v1, v2):
    if length(v1, v2):
        v = []
        for index in range(len(v1)):
            v += [ComplexCalculator.sub(v1[index], v2[index])]
        dist = abs(v_norm(v))
        return dist
    else:
        return 'Error: Different length vector'


# UNITARY MATRIX

def m_unit(m1):
    if length(m1, m1[0]):
        mI = diagonal((len(m1)))
        m2 = m_adj(m1)
        product = m_mul(m1, m2)
        flag = True
        aux = f_aux(product)
        for i in range(len(m1)):
            for j in range(len(m1)):
                if product[i][j] != mI[i][j]:
                    flag = False

        if flag:
            return "Is Unitary"
        else:
            return "Is not Unitary"
    else:
        return "The input have to be a square matrix"


# HERMITIAN MATRIX

def m_herm(m1):
    flag = True
    m2 = m_adj(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != m2[i][j]:
                flag = False
    if flag:
        return "Is hermitian"
    else:
        return "Is not hermitian"