# For n = 9, print
# 0
# 11
# 222
# 3333
# 44444
# 555555
# 6666666
# 77777777
# 888888888
# 9999999999
# 888888888
# 77777777
# 6666666
# 555555
# 44444
# 3333
# 222
# 11
# 0

n = 9
for i in range(0,n+1):
    for j in range(i):
        print(i ,end="")
    print(i)

for a in range(n-1,-1,-1):
    for b in range(a):
        print(a,end="")
    print(a)  


