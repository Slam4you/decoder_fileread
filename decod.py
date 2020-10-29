with open(r"C:\Users\Slam\Documents\dataset_3363_2.txt") as inf:
    s1 = list(inf.readline().strip())
print(s1)
deshifr = ''
memory_num = ''
for i in range(len(s1) - 1,-1,-1):
    if s1[i].isdigit():
        memory_num = s1[i] + memory_num
    else:
        deshifr = int(memory_num) * s1[i] + deshifr
        memory_num = ''
print(deshifr)
with open(r'C:\Users\Slam\Documents\deshifr.txt','w') as ouf:
    ouf.write(deshifr)