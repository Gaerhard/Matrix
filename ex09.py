import matrix

def main():

    print("Enter 1st matrix data")
    matrix1 = matrix.createMatrix()

    print ("matrix 1 = ", matrix1.data)

    matrix1.validityCheck()

    print("--------matrix---------")
    print("Transpose = ", matrix1.transpose())

main()