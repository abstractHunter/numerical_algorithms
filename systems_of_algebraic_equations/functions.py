
def gauss(A, B, returnFinalMatrix=False) -> list :
    # w = working matrix, obtained by appending B to A
    w = A.extend(B)

    # upper triangularization of w
    w = w.triangularize()

    n = w.row

    results = [0] * n

    # calcul of the last solution wich will be used to calculate the other ones
    xn = round((w.data[n-1][-1] / w.data[n-1][n-1]), 4)
    results[-1] = xn

    # calcul of the other solutions recursively
    for i in range(n-2, -1, -1):
        _sum = sum([w.data[i][j] * results[j] for j in range(i+1, n)])
        results[i] = round((w.data[i][-1] - _sum ) / w.data[i][i], 4)

    if returnFinalMatrix:
        return results, w
    else:
        return results


def gaussJordan(A, B, returnFinalMatrix=False)  -> list :
    # w = working matrix, obtained by appending B to A
    w = A.extend(B)

    # diagonalization of w
    w = w.diagonalize()

    # divide each element of row k by w.data[k][k] 
    n = w.row
    for i in range(n):
        x = w.data[i][i]
        w.data[i][i] /= x
        w.data[i][-1] /= x

    # retrieving results 
    results = [round(w.data[i][-1], 4) for i in range(n)]

    if returnFinalMatrix:
        return results, w
    else:
        return results
