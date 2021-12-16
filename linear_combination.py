import matrix
import pyfma

from vector import Vector, createVector

def linear_combination_matrix(m1: matrix.Matrix, m2: matrix.Matrix, coeffs) : 
    m_comb = []
    if (m1.numberOfRows != m2.numberOfRows or m1.numberOfColumns !=m2.numberOfColumns):
        print("Matrices should have the same size")
        return
    for i in range(m1.numberOfRows) :
        newrow = []
        for j in range(m1.numberOfColumns) :
            newrow.append(pyfma.fma(m1.data[i][j], m2.data[i][j], coeffs))
        m_comb.append(newrow)    
    return m_comb


def linear_combination_vector(vectors, coeffs):
    #TODO Verifier que la len de coeff = nombre de vecteurs = len de chaque vecteur
    result = [0] * len(coeffs)
    print("vecteurs", vectors)
    print("coeffs", coeffs)

    for i in range(len(coeffs)):
        # for j in range(len(vectors[i])):
        print("DEBUG")
        print(coeffs[i])
        #print(vectors[i][j])
        #print(result[j])
        result = pyfma.fma(coeffs, vectors[i], result)
    return result