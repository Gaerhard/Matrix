import matrix
import vector

def main():

    matrix1 = matrix.createMatrix()
    matrix2 = matrix.createMatrix()
    vector1 = vector.createVector()
    vector2 = vector.createVector()

    print ("matrix 1 = ", matrix1.data)
    print ("matrix 2 = ", matrix2.data)
    print("-----------------------")
    print ("vector 1 = ", vector1.data)
    print ("vector 2 = ", vector2.data)

    matrix1.validityCheck()
    matrix2.validityCheck()
    vector1.validityCheck()
    vector2.validityCheck()

    print("--------VECTORS---------")
    print("SUM", vector1.add(vector2))
    print("------------------------")
    print("SUBSTRACTION", vector1.sub(vector2))
    print("------------------------")
    print("SCALAR", vector1.scl(10))
    print("\n--------MATRICES---------")
    print("SUM", matrix1.add(matrix2))
    print("------------------------")
    print("SUBSTRACTION", matrix1.sub(matrix2))
    print("------------------------")
    print("SCALAR", matrix1.scl(-1))




main()