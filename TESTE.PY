
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)


2,3,5,7,11,13,17,19,23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107