import pyfma

class Vector:
    def __init__(self, numberOfColumns, data):
        self.numberOfColumns = numberOfColumns
        self.data = data
    
    def add(self, v2: "Vector"):
        result = []
        if (self.numberOfColumns != v2.numberOfColumns):
            print("vectors must have the same length")
            exit ()
        for i in range(self.numberOfColumns):
            result.append(self.data[i] + v2.data[i])
        return result

    def sub(self, v2: "Vector"):
        result = []
        if (self.numberOfColumns != self.numberOfColumns):
            print("vectors must have the same length")
            exit ()
        for i in range(self.numberOfColumns):
            result.append(self.data[i] - v2.data[i])
        return result
    
    def scl(self, scalar):
        result = []
        for i in range(self.numberOfColumns):
            result.append(self.data[i] * scalar)
        return result
    
    def dotProduct(self, v2: "Vector"):
        result = 0
        if (self.numberOfColumns != v2.numberOfColumns):
            print("vectors must have the same length")
            exit ()
        for i in range(self.numberOfColumns):
            result = pyfma.fma(self.data[i], v2.data[i], result)
        return result   

    def norm1(self):
        result = 0
        for i in range(self.numberOfColumns):
            if self.data[i] >= 0:
                result += self.data[i]
            else:
                result += -self.data[i]
        return result
    
    def norm2(self):
        result = 0
        for i in range(self.numberOfColumns):
            result += pow(self.data[i], 2)
        result = pow(result, 0.5)
        return result

    def normInfinity(self):
        tmp = []
        for i in range(len(self.data)):
            tmp.append(self.data[i] if self.data[i] >= 0 else -self.data[i])
        return max(tmp)
    
    def validityCheck(self):
        if (not self.data or not self.numberOfColumns):
            print("Invalid vector")
            exit()
        if (self.numberOfColumns != len(self.data)):
            print("Invalid number of columns in vector")
            exit()

def createVector():
    r =int(input("enter rows: "))

    m = []
    for i in range(r):
        print("enter value for row", i)
        v = float(input())
        m.append(v)
    vector = Vector(r, m)
    return vector