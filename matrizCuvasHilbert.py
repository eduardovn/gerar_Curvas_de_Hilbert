from hilbertcurve.hilbertcurve import HilbertCurve
from matplotlib import pyplot as plt
import numpy as np

def matrizDeHilbert():
  X = np.array([ [0, 1, 2, 3, 4, 5, 6, 7], 
                 [8, 9, 10, 11, 12, 13, 14, 15], 
                 [16, 17, 18, 19, 20, 21, 22, 23], 
                 [24, 25, 26, 27, 28, 29, 30, 31],
                 [32, 33, 34, 35, 36, 37, 38, 39], 
                 [40, 41, 42, 43, 44, 45, 46, 47], 
                 [48, 49, 50, 51, 52, 53, 54, 55], 
                 [56, 57, 58, 59, 60, 61, 62, 63] 
                ])


  print("X: ",X)
  p = 4
  N = 2

  hilbert_curve = HilbertCurve(p, N)
  indexes = np.zeros((8*8,N), dtype='int')

  for i in range(8*8):
    coords = hilbert_curve.point_from_distance(i)
    indexes[i,:] = coords

 
  lista = [X[x,y] for x,y in indexes]
  print(lista)
  print("tam: ",len(lista))
  
  

  


if __name__=="__main__":
  
  matrizDeHilbert()
  