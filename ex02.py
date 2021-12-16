import vector
import matrix
import linear_interpolation

def main():

    # vector1 = vector.createVector()
    # vector2 = vector.createVector()

    # print("-----------------------")
    # print ("vector 1 = ", vector1.data)
    # print ("vector 2 = ", vector2.data)

    # vector1.validityCheck()
    # vector2.validityCheck()

    # print("--------VECTORS---------")
    # t = float(input("Enter t value between 1 and 0: "))
    # if (t < 0 or t > 1):
    #     print("t should be between 1 and 0")
    #     return
    # print("Linear interpolation", 
    #     linear_interpolation.linearInterpolationVector(vector1, vector2, t))

    matrix1 = matrix.createMatrix()
    matrix2 = matrix.createMatrix()

    print("-----------------------")
    print ("matrix 1 = ", matrix1.data)
    print ("matrix 2 = ", matrix2.data)

    matrix1.validityCheck()
    matrix2.validityCheck()

    print("--------VECTORS---------")
    t = float(input("Enter t value between 1 and 0: "))
    if (t < 0 or t > 1):
        print("t should be between 1 and 0")
        return
    print("Linear interpolation", 
        linear_interpolation.linearInterpolationMatrix(matrix1, matrix2, t))



main()