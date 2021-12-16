import vector
import cosine

def main():

    print("Enter 1st Vector data")
    vector1 = vector.createVector()
    print("Enter 2nd Vector data")
    vector2 = vector.createVector()

    print ("vector 1 = ", vector1.data)
    print ("vector 2 = ", vector2.data)

    vector1.validityCheck()
    vector2.validityCheck()

    print("--------VECTORS---------")
    print("Cosine = ", cosine.angleCos(vector1, vector2))

main()