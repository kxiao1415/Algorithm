#regular matrix multiplication
def standardMatrixMulti(M1,M2):
    diM1=[len(M1),len(M1[0])]
    diM2=[len(M2),len(M2[0])]
    
    M3=[[0 for j in range(diM2[1])] for i in range(diM1[0])]

    i=0
    while i <diM1[0]:
        j=0
        while j < diM2[1]:
            M3[i][j]=sum([M1[i][k]*M2[k][j] for k in range(diM2[0])])
            j+=1
        i+=1
        
    return M3

#matrix addition
def matrixAdd(M1,M2):
    diM1=[len(M1),len(M1[0])]
    M3=[[0 for j in range(diM1[1])]for i in range(diM1[0])]

    i=0
    while i < diM1[0]:
        j=0
        while j < diM1[1]:
            M3[i][j]=M1[i][j]+M2[i][j]
            j+=1
        i+=1
            
    return M3

#matrix subtraction
def matrixSub(M1,M2):
    diM1=[len(M1),len(M1[0])]
    M3=[[0 for j in range(diM1[1])]for i in range(diM1[0])]

    i=0
    while i < diM1[0]:
        j=0
        while j < diM1[1]:
            M3[i][j]=M1[i][j]-M2[i][j]
            j+=1
        i+=1
            
    return M3

#strassen algorithm for 2x2 matrix
def strassen2x2(M1,M2):
    M3=[[0,0],[0,0]]
    
    C1=(M1[0][0]+M1[1][1])*(M2[0][0]+M2[1][1])
    C2=(M1[1][0]+M1[1][1])*M2[0][0]
    C3=M1[0][0]*(M2[0][1]-M2[1][1])
    C4=M1[1][1]*(M2[1][0]-M2[0][0])
    C5=(M1[0][0]+M1[0][1])*M2[1][1]
    C6=(M1[1][0]-M1[0][0])*(M2[0][0]+M2[0][1])
    C7=(M1[0][1]-M1[1][1])*(M2[1][0]+M2[1][1])

    M3[0][0]=C1+C4-C5+C7
    M3[0][1]=C3+C5
    M3[1][0]=C2+C4
    M3[1][1]=C1-C2+C3+C6

    return M3

#divide matrix into 4 blocks.  If any matrix is <= 2X2, return itself
def subMatrix(A):
    n = len(A)
    m = len(A[0])

    if n <=2 and m>2:
        B11 = [[A[i][j]for j in range(m/2)]for i in range(n)]
        B12 = [[A[i][j]for j in range(m/2,m)]for i in range(n)]

        A=[[B11,B12]]
        
        
    elif n>2 and m <= 2:
        B11 = [[A[i][j]for j in range(m)]for i in range(n/2)]
        B21 = [[A[i][j]for j in range(m)]for i in range(n/2,n)]

        A=[[B11],[B21]]
        
    elif n >2 and m >2:
        B11 = [[A[i][j]for j in range(m/2)]for i in range(n/2)]
        B12 = [[A[i][j]for j in range(m/2,m)]for i in range(n/2)]
        B21 = [[A[i][j]for j in range(m/2)]for i in range(n/2,n)]
        B22 = [[A[i][j]for j in range(m/2,m)]for i in range(n/2,n)]

        A=[[B11,B12],[B21,B22]]
        
    return A

#stitch 4 matrices into one
def stitch(part00,part01,part10,part11):
    
    dipart00 = [len(part00),len(part00[0])]
    dipart01 = [dipart00[0],len(part01[0])]
    dipart10 = [len(part10),dipart00[1]]
    
    M3=[[0 for j in range(dipart00[1]+dipart01[1])] for i in range(dipart00[0]+dipart10[0])]

    i=0
    while i < dipart00[0]:
        j=0
        while j < dipart00[1]:
            M3[i][j]=part00[i][j]
            j+=1
        i+=1

    a = 0
    while a <dipart00[0]:
        b=dipart00[1]
        h=0
        while b < len(M3[1]):
            M3[a][b]=part01[a][h]
            b+=1
            h+=1
        a+=1

    c = dipart00[0]
    k = 0
    while c < len(M3[0]):
        d=0
        while d < dipart00[1]:
            M3[c][d]=part10[k][d]
            d+=1
        k+=1
        c+=1

    e = dipart00[0]
    l=0
    while e < len(M3[0]):
        f=dipart00[1]
        g=0
        while f < len(M3[1]):
            M3[e][f]=part11[l][g]
            f+=1
            g+=1
        e+=1
        l+=1

    return M3
    
#strassen for 2^nx2^n matrices
def strassen(M1,M2):
    lenM1 =len(M1)
    
    A = subMatrix(M1)

    if A == M1:
        if lenM1==len(M1[0])==2:
            return strassen2x2(M1,M2)
        else:
            return standardMatrixMulti(M1,M2)
        
    B = subMatrix(M2)

    m1 = strassen(matrixAdd(A[0][0],A[1][1]),matrixAdd(B[0][0],B[1][1]))
    m2 = strassen(matrixAdd(A[1][0],A[1][1]),B[0][0])
    m3 = strassen(A[0][0],matrixSub(B[0][1],B[1][1]))
    m4 = strassen(A[1][1],matrixSub(B[1][0],B[0][0]))
    m5 = strassen(matrixAdd(A[0][0],A[0][1]),B[1][1])
    m6 = strassen(matrixSub(A[1][0],A[0][0]),matrixAdd(B[0][0],B[0][1]))
    m7 = strassen(matrixSub(A[0][1],A[1][1]),matrixAdd(B[1][0],B[1][1]))

    part00 = matrixSub(matrixAdd(m4,matrixAdd(m1,m7)),m5)
    part01 = matrixAdd(m3,m5)
    part10 = matrixAdd(m2,m4)
    part11 = matrixSub(matrixAdd(m1,matrixAdd(m3,m6)),m2)
    
    M3=stitch(part00,part01,part10,part11)
    
    return M3

#check to see if a number is powers of 2
def isPwr2(num):
    
    return num !=0 and ((num & (num -1))==0)

#next power of 2
def nextPwr2(num):
    
    if isPwr2(num):
        return num
    else:
        return 2**num.bit_length()

#generalized strassen for all matrices with padding
def gStrassen(M1, M2):
    M1n = len(M1)
    M1m = len(M1[0])
    M2n = len(M2)
    M2m = len(M2[0])
    
    if M1n==M1m==M2m and isPwr2(M1n):
        return strassen(M1,M2)
    
    else:
        newSize = nextPwr2(max(M1n,M1m,M2m))
        M3=M4=[[0 for j in xrange(newSize)] for i in xrange(newSize)]

        i = 0
        while i < M1n:
            j = 0
            while j < M1m:
                M3[i][j]=M1[i][j]
                j+=1
            i+=1

        h = 0
        while h < M2n:
            k = 0
            while k < M2m:
                M4[h][k]=M2[h][k]
                k+=1
            h+=1

        M5=[i[:M2m] for i in strassen(M3,M4)[:M1n]]

        return M5

        




if __name__=='__main__':
    
    M1 =M2= [[1,2,1,1,1,2,11,1,1],
             [1,2,1,1,1,2,4,1,4],
             [1,2,1,1,1,2,1,1,6],
             [1,2,1,1,6,2,1,1,8],
             [1,2,1,7,1,2,1,1,5],
             [1,2,1,1,2,2,1,1,9],
             [1,2,1,1,1,2,1,1,23],
             [1,2,1,8,1,2,1,1,56],
             [1,2,1,8,1,2,1,1,113]]
    
    for i in gStrassen(M1,M2):
        print i

    print '-'*9

    for i in standardMatrixMulti(M1,M2):
        print i
