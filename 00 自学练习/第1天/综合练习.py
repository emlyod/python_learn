import string

def read_file(file_path):
    """生成器：逐行读取文件内容"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # 去除每行的首尾空白字符

def clean_and_split(line):
    """清理文本并拆分为单词列表"""
    translator = str.maketrans('', '', string.punctuation)  # 移除标点
    line = line.translate(translator)  # 去掉标点，string.punctuation 是标点符号
    return line.lower().split()  # 转小写并拆分为单词列表

def count_words(file_path):
    """统计文件中每个单词出现的次数"""
    word_count = {}
    for line in read_file(file_path):
        words = clean_and_split(line)
        for word in words:
            # 如果字典里面有这个键，则返回他的值，反之返回默认值。
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    file_path = "test.txt"  # 测试文件路径
    result = count_words(file_path)
    print("Word frequencies:", result)
