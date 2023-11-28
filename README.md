最近在App Store发现了一款在电脑背单词的软件，可以充分利用上班的碎片时间记单词

![Snipaste_2023-11-26_17-34-03.jpg](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/17009925291124hGKfF64.jpg)

同时我在Github发现了一个主题为 **程序员工作中常见的英语词汇** 的仓库

![image.png](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/1700992529243xt2bBQ78.png)

我打算把这些单词用碎片化时间记一下，于是写了个脚本，实现了一键导入，最终效果如图

![image.png](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/1700992529389bX2cTrhW.png)


## 获取原项目数据

```
mkdir get-most-frequent-technology-english-words-csv
cd get-most-frequent-technology-english-words-csv
git clone --depth=1 https://github.com/Wei-Xia/most-frequent-technology-english-words.git
pipenv --python 3.11
pipenv shell
touch create_csv.py
```
## 安装依赖包

```
pipenv install  pandas openpyxl xlsxwriter
```

##   在`create_csv.py`中写入以下代码

```
import os
import glob
import csv
import pandas as pd

def read_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.readlines()
        metadata_lines = contents[1:contents.index('---\n', 1)]  # 获取元数据部分
        metadata = {}
        for line in metadata_lines:
            key, value = line.split(":", 1)  # 只根据第一个冒号来分割
            metadata[key.strip()] = value.strip()
        return metadata

def main():
    csv_file = 'most-frequent-technology-english-words.csv'
    md_files = glob.glob('./most-frequent-technology-english-words/_posts/*.md')
    print('==md_files==', md_files)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'meaning', 'correct', 'note', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for md_file in md_files:
            metadata = read_metadata(md_file)
            writer.writerow(metadata)

    # 读取CSV文件
    df = pd.read_csv(csv_file)

    # 选择需要的列
    df = df[['word', 'correct', 'meaning']]

    # 重命名列
    df = df.rename(columns={
        'word': '单词(必传)',
        'correct': '音标(默认不传)',
        'meaning': '解释(默认不填)',
    })

    # 将DataFrame转换为Excel文件
    df.to_excel('most-frequent-technology-english-words.xlsx', engine="xlsxwriter", index=False, sheet_name='单词本')

if __name__ == "__main__":
    main()

```

运行 `python create_csv.py`

![image.png](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/1700992529523adMtppAZ.png)

![image.png](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/1700992529734NNJk44f5.png)

~~Excel生成后，记得用微软的Excel打开，并保存一下，才能被**摸鱼单词**识别~~ （2023年11月28日更新）经过和摸鱼单词作者的交流， 将DataFrame转换为Excel文件时，启用`engine="xlsxwriter"` , 即可被摸鱼单词识别

![](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/image-20231128182631536.png)

## 将Excel导入摸鱼单词

![2023-11-26 17.28.32.gif](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/17009925298695wBCtfYC.gif)


## 导入成功


![image.png](https://raw.githubusercontent.com/zhaoolee/get-most-frequent-technology-english-words-csv/master/README/170099253056335B1mcP0.png)


## 小结

中国大陆的程序员缺少英语语言环境，参加工作后，在学校学习的英语，会慢慢淡忘。

在桌面放一个记单词的小组件，利用碎片化时间多背背单词，可以大大减少读英语文档的难度，也能有更广阔的就业机会。





