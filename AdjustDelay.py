#用于微调谱面延迟
f = open('./data/music2.txt',encoding='utf-8',mode='r')#谱面选择
line = f.readline()
lineList = []
while line:
    lineList.append(line)
    line = f.readline()
f.close()
f =open('./data/music2.txt',encoding='utf-8',mode='w')
for line in lineList:
    x = line.strip().split(' ')
    f.writelines(x[0]+' '+str(float(x[1])-0.001)+'\n')#延迟调整
f.close()