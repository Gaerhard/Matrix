import vector
import pyfma

def crossProduct(v1 : vector.Vector, v2: vector.Vector):
    result = [0, 0 , 0]
    if (v1.numberOfColumns != 3 and v1.numberOfColumns != v2.numberOfColumns):
        print("Both vectors should have 3 dimensions")
        return
    result[0] = pyfma.fma(v1.data[1], v2.data[2], -v1.data[2]*v2.data[1])
    result[1] = pyfma.fma(v1.data[2], v2.data[0], -v1.data[0]*v2.data[2])
    result[2] = pyfma.fma(v1.data[0], v2.data[1], -v1.data[1]*v2.data[0])

    return vector.Vector(v1.numberOfColumns, result)