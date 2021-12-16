import matrix
import vector

def linearInterpolationVector(v1 : vector.Vector, v2: vector.Vector, t):
    result = []
    for i in range(v1.numberOfColumns):
        result.append((1-t)*v1.data[i]+t*v2.data[i])
    return result

def linearInterpolationMatrix(m1: matrix.Matrix, m2: matrix.Matrix, t):
    m_linterp = []
    for i in range(m1.numberOfRows):
        newrow = []
        for j in range(m1.numberOfColumns):
            newrow.append((1-t)*m1.data[i][j] + t*m2.data[i][j])
        m_linterp.append(newrow)
    return m_linterp