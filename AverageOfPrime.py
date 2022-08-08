#DCIT104 10973501 - EMMANUEL AMANOR

List = []
Num = int(input())

for i in range (2,Num):
    for x in range (2,i):
        if i % x == 0:
            break
    else:
        List.append(i)

a = sum(List)
b = len(List)
print(List)
print("Average =", a/b)