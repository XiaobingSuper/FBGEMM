import os

import pandas as pd

dir_path = 'gemm_result/'
file_names = os.listdir(dir_path)

#for file in file_names:
#df = pd.read_table("log0")

lists = []
file_nums = 0
for name in file_names:
    f = open(dir_path+name,"r")
    temp_lines = f.readlines()
    lines = []
    for line in temp_lines:
        if line != '\n':
            line=line.strip()
            line=line.split(",");
            for i in range(len(line)):
                line[i] = line[i].strip()
            if line[-2] == 'FBGEMM_i8_acc32':
                lines.append(line)

    for n, fields in enumerate(lines):
        if file_nums == 0:
            # for first file
            lists.append(fields)
            continue
        lists[n][-1] = float(fields[-1]) + float(lists[n][-1])
    file_nums+=1

for j in range(len(lines)):
    if lists[j][-1] != 'GOPS':
        lists[j][-1] /= file_nums

df = pd.DataFrame(lists)
df.to_excel(dir_path+'result.xlsx', index=False)


