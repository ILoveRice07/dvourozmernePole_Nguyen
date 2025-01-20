import numpy as np
#Vytvoření dvourozměrného pole
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#Přepsání čisla v 2. sloupci a 2. řádku
matrix[1][1] = 105
print(matrix)

#Přidání 1 řádku a sloupce
matrix_append = np.append(matrix,10)
print(matrix_append)
