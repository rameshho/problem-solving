def matrixmultiplication(m1, m2):
    """
    Does multiply 2 matrix and returns the result
    """
    lenofm1 = len(m1)
    lenofm2 = len(m2)

    if lenofm1 != lenofm2:
        print("Not matrix")

    m3 = []
    for i in range(len(m1)):
        m = []
        for j in range(len(m2)):
            m.append(0)
        m3.append(m)

    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k]*m2[k][j]
    return m3

if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    result = matrixmultiplication(m1, m2)
    print(result)
