##
# Miscellaneous helper functions
##

from numpy import *

def random_weight_matrix(m, n):
    #### YOUR CODE HERE ####

    eps = sqrt(6.0) / sqrt(m + n)
    A0 = random.uniform(-1.0 * eps, eps, (m, n))

    #### END YOUR CODE ####
    assert(A0.shape == (m,n))
    return A0