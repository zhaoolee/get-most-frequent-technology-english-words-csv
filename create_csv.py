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
