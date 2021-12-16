import matrix
import vector

def main():

    print("Enter first matrix values")
    matrix1 = matrix.createMatrix()
    # print("Enter second matrix values")
    # matrix2 = matrix.createMatrix()
    print("Enter first vector values")
    vector1 = vector.createVector()

    print ("matrix 1 = ", matrix1.data)
    # print ("matrix 2 = ", matrix2.data)
    # print("-----------------------")
    print ("vector 1 = ", vector1.data)

    matrix1.validityCheck()
    # matrix2.validityCheck()
    vector1.validityCheck()

    # print("\n--------MATRICES---------")
    # print("Matrix multiplication", matrix1.mulMatrix(matrix2))
    print("------------------------")
    print("\n-------VECTORS----------")
    print("Vector multiplication", matrix1.mulVector(vector1))




main()