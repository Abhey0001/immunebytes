import math
def cc(x, y, n) :
    sumx = 0
    sumy = 0
    sumxy = 0
    sqSumx = 0
    sqSumy = 0
    i = 0

    while i < n :
        sumx = sumx + x[i]
        sumy = sumy + y[i]
        sumxy = sumxy + x[i] * y[i]
        sqSumx = sqSumx + x[i] * x[i]
        sqSumy = sqSumy + y[i] * y[i]
        i = i + 1
    corr = (float)(n * sumxy - sumx * sumy)/(float)(math.sqrt((n * sqSumx - sumx * sumx)* (n * sqSumy - sumy * sumy)))
    return corr

test_case=int(input())
i=0
for i in range(test_case):
    n=int(input())
    gpa=[]
    j=0
    gpa=list(float(num) for num in input().strip().split())[:n]
    scores=[]
    j=0
    for j in range(5):
        test=[]
        m=0
        test=list(float(num) for num in input().strip().split())[:n]
        scores.append(test)
i=0
best=-2
best_ind=0
for i in range(5):
    list1 = gpa
    list2 = scores[i]
    cscore = cc(list1, list2,n)
    if cscore>best:
        best=cscore
        best_ind=i+1
print(best_ind)