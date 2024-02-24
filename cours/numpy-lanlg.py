# utf-8

import numpy as np

# resolution d'un systeme d'equation 2D

a = np.array([[2,3],[1,2]])
b = np.array([7,4])

s = np.linalg.solve(a,b)
