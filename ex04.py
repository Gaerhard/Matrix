import vector

def main():

    vector1 = vector.createVector()

    print("-----------------------")
    print ("vector 1 = ", vector1.data)

    vector1.validityCheck()

    print("--------VECTORS---------")
    print("Manhattan norm = ", vector1.norm1())
    print("Euclidian norm = ", vector1.norm2())
    print("SUpremum norm = ", vector1.normInfinity())



main()