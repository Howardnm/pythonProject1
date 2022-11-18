#
################################################################
# 可以转任意编码到utf-8编码
################################################################
import chardet
from chardet.universaldetector import UniversalDetector


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data=f.read()
        return chardet.detect(data)['encoding']


def get_encode_info(file):
    with open(file, 'rb') as f:
        detector=UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']


def read_file(file):
    with open(file, 'rb') as f:
        return f.read()


def write_file(content, file):
    with open(file, 'wb') as f:
        f.write(content)


def convert_encode2utf8(file, original_encode, des_encode):
    file_content=read_file(file)
    file_decode=file_content.decode(original_encode, 'ignore')
    file_encode=file_decode.encode(des_encode)
    write_file(file_encode, file)


def encodeFile2Utf8(filename):
    file_content=read_file(filename)
    encode_info=get_encode_info(filename)
    if encode_info != 'utf-8':
        convert_encode2utf8(filename, encode_info, 'utf-8')


filename=input("输入文件")

encode_info=get_encode_info(filename)  # 获取文件编码
print(encode_info)

encodeFile2Utf8(filename)  # 转文件编码到utf8格式
