def sum_to(n) :
    S = 0
    for k in range(n) :
        S += k+1
    return S

print(sum_to(100))