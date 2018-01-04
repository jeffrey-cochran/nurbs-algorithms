

def Horner1(a, u0):
    '''Horner algorithm for computing a power basis curve'''
    #
    # Get degree
    degree = len(a) - 1
    #
    # Initialize curve evaluation
    C = a[degree]
    #
    # Iterate over lower exponents
    for i in range(degree - 1, -1, -1):
        C = C * u0 + a[i]
    #
    return C