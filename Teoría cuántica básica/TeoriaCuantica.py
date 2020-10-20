import Aux_ComplexVectorSapces as Spaces
import numpy as np
import Aux_ComplexCalculator as Calculator

def diagonal(m):
    mI = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                mI[i][j] = (1, 0)
    return mI


def length(v1, v2):
    if len(v1) == len(v2):
        return True
    else:
        return False


# Punto 1

def probabilities(Ket1, pos):
    norm = Spaces.v_norm(Ket1)
    pos2 = Calculator.mod(Ket1[pos]) ** 2
    result = round((pos2/norm ** 2) * 100, 2)
    return result


def amplitud(Ket1, Ket2):
    v1 = []
    for index in range(len(Ket2)):
        aux = [Ket2[index]]
        v1 += [aux]
    Ket2 = Spaces.m_conj(v1)
    v2 = []
    for index in range(len(Ket2)):
        v2 += Ket2[index]
    norm_1 = Spaces.v_norm(Ket1)
    norm_2 = Spaces.v_norm(v2)
    norm = norm_1 * norm_2
    prob = [Spaces.v_inner(v2, Ket1)]
    point = Spaces.v_scalar((1/norm, 0), prob)[0]
    point = (round(point[0], 2), round(point[1], 2))
    return point



# Punto 2

def m_herm(m1):
    flag = True
    m2 = Spaces.m_adj(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != m2[i][j]:
                flag = False
    if flag:
        return True
    else:
        return False


def media(observable, Ket):
    Ket_aux = []
    for index in range(len(Ket)):
        aux = [Ket[index]]
        Ket_aux += [aux]
    if m_herm(observable):
        Bra = Spaces.m_conj(Ket_aux)
        action = Spaces.m_action(observable, Ket_aux)
        point = Spaces.v_inner(action, Bra)
        point = (round(point[0], 2), round(point[1], 2))
        return point
    else:
        return "No es un observable valido"

def varianza(observable, Ket):
    Ket_aux = []
    for index in range(len(Ket)):
        aux = [Ket[index]]
        Ket_aux += [aux]
    Bra = Spaces.m_conj(Ket_aux)
    med = media(observable, Ket)
    id_med = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                id_med[i][j] = Calculator.multi((-1, 0), med)
    id_med = Spaces.m_add(id_med, observable)
    cudrado = Spaces.m_mul(id_med, id_med)
    action = Spaces.m_action(cudrado, Ket_aux)
    return Spaces.v_inner(action, Bra)

# print(media([[(0, 0),(0, -1)],[(0, 1),(0, 0)]],[(1/(2**(1/2)), 0), (0, 1/(2**(1/2)))]))

# print(varianza([[(0, 0),(0, -1)],[(0, 1),(0, 0)]],[(1/(2**(1/2)), 0), (0, 1/(2**(1/2)))]))

# print(amplitud([[(2, 1)], [(-1, 2)], [(0, 1)], [(1, 0)], [(3, -1)], [(2, 0)], [(0, -2)], [(-2, 1)], [(1, -3)],[(0, -1)]], [[(-1, -4)], [(2, -3)], [(-7, 6)], [(-1, 1)], [(-5, -3)], [(5, 0)], [(5, 8)], [(4, -4)], [(8, -7)], [(2, -7)]]))


# Punto 3

def valores_vectores(observable):
    valores, vectores = np.linalg.eig(observable)
    lista_valores = []
    lista_vectores = []
    for index in range(len(valores)):
        lista_valores += [(valores[index].real, valores[index].imag)]
    for index in range(len(vectores)):
        vector = []
        for index_2 in range(len(vectores[0])):
            vector += [(vectores[index][index_2].real, vectores[index][index_2].imag)]
        lista_vectores += [vector]
    return lista_valores, lista_vectores


def probabilidades_vectores(inicial, observable, posicion):
    vectores = valores_vectores(observable)[1]
    return amplitud(inicial, vectores[posicion])


# print(probabilidades_vectores([(1/(2**(1/2)), 0), (0, 1/(2**(1/2)))], [[0, -1j], [1j, 0]], 1))

# print(valores_vectores([[0j, 1 + 0j], [1 + 0j, 0j]]))

# Punto 4

def m_unitaria(m1):
    if length(m1, m1[0]):
        mI = diagonal((len(m1)))
        m2 = Spaces.m_adj(m1)
        product = Spaces.m_mul(m1, m2)
        flag = True
        aux = Spaces.f_aux(product)
        for i in range(len(m1)):
            for j in range(len(m1)):
                if product[i][j] != mI[i][j]:
                    flag = False
        if flag:
            return True
        else:
            return False
    else:
        return False


def dinamica(mat_u, v1, t):
    if m_unitaria(mat_u):
        for index in range(t):
            v1 = Spaces.m_action(mat_u, v1)
        return v1
    else:
        return "Matriz no valida"

print(dinamica([[(0, 1), (0, 0)], [(0, 0), (0, 1)]], [(1, 0), (0, 0)], 1))

"""
# Ejercicio 4.3.1

# Vector inicial :

v1 = [[(1, 0)], [(0, 0)]]

observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]

vr = Spaces.m_action(observable_x, v1)

valores_x, vectores_x = valores_vectores(observable_x)


print("El resultado de la observacion es: ", vr)

print("Los valores porpios del observable son: ", valores_x, "ademas sus vectores poropios son: ", vectores_x, " por tanto el sistema colapsa en un vector poropio")


# Ejercicio 4.3.2

# p1 = probabilidades_vectores(vr, observable_x, 1)

# Excercise 4.4.1

v1_4 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
v2_4 = [[((2**(1/2))/2, 0), ((2**(1/2))/2, 0)], [((2**(1/2))/2, 0), (-(2**(1/2))/2, 0)]]
if m_unitaria(v1_4) and m_unitaria(v2_4):
    print(m_unitaria(Spaces.m_mul(v1_4,v2_4)))

# Excercise 4.4.2

print(dinamica([[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],
                    [(1/(2**(1/2)), 0), (0, 0), (0, 0), (-1/(2**(1/2)), 0)],
                    [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                    [(0, 0), (-1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]],
                    [(1,0), (0,0), (0,0), (0,0)], 3))

print(dinamica([[(0, 0), (1 / (2 ** (1 / 2)), 0), (1 / (2 ** (1 / 2)), 0), (0, 0)],
               [(0, 1 / (2 ** (1 / 2))), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
               [(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (0, 1 / (2 ** (1 / 2)))],
               [(0, 0), (1 / (2 ** (1 / 2)), 0), (-1 / (2 ** (1 / 2)), 0), (0, 0)]],
              [(1, 0), (0, 0), (0, 0), (0, 0)], 3))
"""