matrix=[[1,2,3,1],[0,0,0,2],[5,1,1,1],[3,4,1,6]]
matrix_suavizada=[]
suma=0
divisor=0
for i in range(0,4):
    matrix_suavizada.append([])
    for j in range(0,4):
        suma=suma+matrix[i][j]
        if i>0:
            suma=suma+matrix[i-1][j]
            divisor=divisor+1
        if i>0 and j<3:
            suma=suma+matrix[i-1][j+1]
            divisor=divisor+1
        if j<3:
            suma=suma+matrix[i][j+1]
            divisor=divisor+1
        if i<3 and j<3:
            suma=suma+matrix[i+1][j+1]
            divisor=divisor+1
        if i<3:
            suma=suma+matrix[i+1][j]
            divisor=divisor+1
        if i<3 and j>0:
            suma=suma+matrix[i+1][j-1]
            divisor=divisor+1
        if i>0:
            suma=suma+matrix[i][j-1]
            divisor=divisor+1
        if i>0 and j>0:
            suma=suma+matrix[i-1][j-1]
            divisor=divisor+1
        imagensuavisada=suma//divisor
        matrix_suavizada[i].append(imagensuavisada)
        print(matrix[i][j], end=" ")
        suma=0
        divisor=0
    print()
print("Imagen suavisada")
for i in range(0,4):
    for j in range(0,4):
        print(matrix_suavizada[i][j], end=" ")
    print()