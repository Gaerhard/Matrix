import pyfma
import vector

class Matrix:
    def __init__(self, numberOfRows, numberOfColumns, data):
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.data = data

    def add(self, m2: "Matrix"):
        result = []
        if (self.numberOfColumns != m2.numberOfColumns or 
            self.numberOfRows != self.numberOfRows):
            print("Matrices should have the same size")
            return
        for i in range(self.numberOfRows):
            newRow = []
            for j in range(self.numberOfColumns):
                newRow.append(self.data[i][j] + m2.data[i][j])
            result.append(newRow)
        return result

    def sub(self, m2: "Matrix"):
        result = []
        if (self.numberOfColumns != m2.numberOfColumns or 
            self.numberOfRows != self.numberOfRows):
            print("Matrices should have the same size")
            return
        for i in range(self.numberOfRows):
            newRow = []
            for j in range(self.numberOfColumns):
                newRow.append(self.data[i][j] - m2.data[i][j])
            result.append(newRow)
        return result

    def scl(self, scalar):
        result = []
        for i in range(self.numberOfRows):
            newRow = []
            for j in range(self.numberOfColumns):
                newRow.append(self.data[i][j] * scalar)
            result.append(newRow)
        return result
    
    def validityCheck(self):
        if (not self.data or not self.numberOfColumns or not self.numberOfRows):
            print("Invalid matrix")
            exit()
        if (self.numberOfRows != len(self.data)):
            print("Invalid number of lines in matrix")
            exit()
        for i in range(self.numberOfRows):
            if (self.numberOfColumns != len(self.data[i])):
                print("Invalid number of Columns in matrix")
                exit()
    
    def mulMatrix(self, m: "Matrix"):
        if (self.numberOfColumns != m.numberOfColumns
            or self.numberOfRows != m.numberOfRows
            or self.numberOfRows != self.numberOfColumns):
            print("Both matrices should be square matrices and should have the same dimensions")
            return
        m_map = []
        for i in range(self.numberOfRows):
            newRow = []
            for k in range(m.numberOfColumns):
                tmp = 0
                for j in range(self.numberOfColumns):
                    tmp = pyfma.fma(self.data[i][j], m.data[j][k], tmp)
                newRow.append(tmp)
            m_map.append(newRow)
        return m_map

    def mulVector(self, v: vector.Vector):
        if (self.numberOfColumns != self.numberOfRows 
            or self.numberOfColumns != v.numberOfColumns):
            print("Matrix should be a square matrix and have the same amount of columns as the vector")
            return
        result = []
        for i in range(self.numberOfRows):
            tmp = 0
            for j in range(self.numberOfColumns):
                tmp = pyfma.fma(self.data[i][j], v.data[j], tmp)
            result.append(tmp)
        return result

    def trace(self):
        if (self.numberOfRows != self.numberOfColumns):
            print("The matrix should be a square matrix")
            return
        result = 0
        for i in range(self.numberOfRows):
            result += self.data[i][i]
        return result

    def transpose(self):
        m_transp = [[0 for x in range(self.numberOfColumns)] for y in range(self.numberOfRows)]
        for i in range(self.numberOfRows):
            for j in range(self.numberOfColumns):
                m_transp[j][i] = self.data[i][j]
        return m_transp

    def reducedRowEchelon(self):
        m = self
        pivot_coord = 0
        for r in range(m.numberOfRows):
            if (m.numberOfColumns <= pivot_coord):
                return m
            i = r
            while m.data[i][pivot_coord] == 0:
                i += 1
                if (i == m.numberOfRows):
                    i = r
                    pivot_coord += 1
                    if (pivot_coord == m.numberOfColumns):
                        return m
            m.data[i],m.data[r] = m.data[r],m.data[i]
            pivot_val = m.data[r][pivot_coord]
            m.data[r] = [ m_element / pivot_val for m_element in m.data[r]]
            for i in range(m.numberOfRows):
                if (i != r):
                    pivot_val = m.data[i][pivot_coord]
                    m.data[i] = [i_val - r_val * pivot_val for r_val, i_val in (zip(m.data[r], m.data[i]))]
            pivot_coord += 1
        return m

def createMatrix():
    r = int(input("enter rows: "))
    c = int(input("enter columns: "))

    m = []
    for i in range(r):
        l = []
        for j in range(c):
            print("enter value for row", i, "column", j)
            v = float(input())
            l.append(v)
        m.append(l)
    matrix = Matrix(r, c, m)
    return matrix

