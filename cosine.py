import vector

def angleCos(v1: vector.Vector, v2: vector.Vector):
    cosine = v1.dotProduct(v2) / (v1.norm2() * v2.norm2())
    return round(cosine, 9)