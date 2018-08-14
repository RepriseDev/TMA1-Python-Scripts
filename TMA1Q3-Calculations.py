f = open('calculations.txt', 'w')

for i in range(1, 26):
    f.write("%d + %d = %d\n" % (i, (i*i), (i+(i*i))))