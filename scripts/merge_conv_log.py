import os

import pandas as pd

dir_path = 'conv_result/'
file_names = os.listdir(dir_path)

lists = []
file_nums = 0
for name in file_names:
    print(name)
    f = open(dir_path+name,"r")
    lines = f.readlines()
    for n, fields in enumerate(lines):
        fields=fields.strip();
        fields=fields.split(",");
        for i in range(len(fields)):
            # remove blank space
            fields[i] = fields[i].strip()
        if file_nums == 0:
            # for first file
            lists.append(fields)
            continue
        if fields[-1] != 'GOPS':
            lists[n][-1] = float(fields[-1]) + float(lists[n][-1])
    file_nums+=1

for j in range(len(lines)):
    if lists[j][-1] != 'GOPS':
        lists[j][-1] /= file_nums

df = pd.DataFrame(lists)
df.to_excel(dir_path+"test.xlsx", index=False)
