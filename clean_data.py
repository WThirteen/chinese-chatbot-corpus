class Config():
    # 读取文件路径
    filename_in = "clean_chat_corpus/chatterbot.tsv"

    # 保存文件路径 
    filesname_out = "clean_data/train_chatterbot.txt"


def load_data():
    config = Config()
    print(config.filename_in)
    # 打开文件
    with open(config.filename_in, "rb") as f:  
        data = f.read().decode("utf-8")
    return data


def clean(data):
    data1 = []
    text = ''
    for i in range(0,len(data)):
        if data[i] != '\t':
            text=text+data[i]
            if data[i] == '\n':
                text=text+'\n'
        else:

            text=text+'\n'
            data1.append(text)
            text=''
    return data1


def save_file(data):
    config = Config()
    f=open(config.filesname_out,"w",encoding='utf-8')
    for line in data:
        f.write(line)
    f.close()    
    print("数据已保存")

def run():
    print("读取文件")
    data=load_data()
    print("整理数据")
    data1=clean(data)
    save_file(data1)

if __name__ == '__main__':
    run()