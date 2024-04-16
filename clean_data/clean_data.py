with open("input.txt", "rb") as f:  # 打开文件
    data = f.read().decode("utf-8")
data2=[]
text=''
for i in range(0,len(data)):
    if data[i] != '\t':
        text=text+data[i]
    else:
        text=text+'\n'
        data2.append(text)
        text=''

f=open("train.txt","w",encoding='utf-8')
for line in data2:
    f.write(line)
f.close()    
