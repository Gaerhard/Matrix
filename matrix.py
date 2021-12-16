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

