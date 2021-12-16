import linear_combination
import vector

def main():

    vector1 = vector.createVector()
    vector2 = vector.createVector()
    coeffs = vector.createVector()

    print("-----------------------")
    print ("vector 1 = ", vector1.data)
    print ("vector 2 = ", vector2.data)

    vector1.validityCheck()
    vector2.validityCheck()
    vectors = [vector1.data, vector2.data]
    coeffs.validityCheck()

    print("--------VECTORS---------")
    print("Linear combination", linear_combination.linear_combination_vector(vectors, coeffs.data))



main()