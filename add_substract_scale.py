import matrix
import vector

def sumVector(v1: vector.Vector, v2: vector.Vector):
    result = []
    if (v1.numberOfColumns != v2.numberOfColumns):
        print("vectors must have the same length")
        exit ()
    for i in range(v1.numberOfColumns):
        result.append(v1.data[i] + v2.data[i])
    return result

def diffVector(v1: vector.Vector, v2: vector.Vector):
    result = []
    if (v1.numberOfColumns != v2.numberOfColumns):
        print("vectors must have the same length")
        exit ()
    for i in range(v1.numberOfColumns):
        result.append(v1.data[i] - v2.data[i])
    return result
    
def dotVector(v1: vector.Vector, scalar):
    result = []
    for i in range(v1.numberOfColumns):
        result.append(v1.data[i] * scalar)
    return result

def sumMatrix(m1: matrix.Matrix, m2: matrix.Matrix):
    result = []
    if (m1.numberOfColumns != m2.numberOfColumns or 
        m1.numberOfRows != m1.numberOfRows):
        print("Matrices should have the same size")
        return
    for i in range(m1.numberOfRows):
        newRow = []
        for j in range(m1.numberOfColumns):
            newRow.append(m1.data[i][j] + m2.data[i][j])
        result.append(newRow)
    return result

def diffMatrix(m1: matrix.Matrix, m2: matrix.Matrix):
    result = []
    if (m1.numberOfColumns != m2.numberOfColumns or 
        m1.numberOfRows != m1.numberOfRows):
        print("Matrices should have the same size")
        return
    for i in range(m1.numberOfRows):
        newRow = []
        for j in range(m1.numberOfColumns):
            newRow.append(m1.data[i][j] - m2.data[i][j])
        result.append(newRow)
    return result

def dotMatrix(m1: matrix.Matrix, scalar):
    result = []
    for i in range(m1.numberOfRows):
        newRow = []
        for j in range(m1.numberOfColumns):
            newRow.append(m1.data[i][j] * scalar)
        result.append(newRow)
    return result