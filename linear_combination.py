import matrix
import pyfma

def linear_combination_vector(vectors, coeffs):
    #TODO Verifier que la len de coeff = nombre de vecteurs = len de chaque vecteur
    result = [0] * len(coeffs)

    for i in range(len(coeffs)):
        result = pyfma.fma(coeffs, vectors[i], result)
    return result