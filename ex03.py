import vector

def main():

    vector1 = vector.createVector()
    vector2 = vector.createVector()

    print("-----------------------")
    print ("vector 1 = ", vector1.data)
    print ("vector 2 = ", vector2.data)

    vector1.validityCheck()
    vector2.validityCheck()

    print("--------VECTORS---------")
    print("Dot product = ", vector1.dotProduct(vector2))



main()