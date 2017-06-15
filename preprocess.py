#coding=utf-8

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题


# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    lines = fopen.readlines()
    # for eachLine in lines:
    #     print "读取到得内容如下：", eachLine
    # print fopen.read()
    fopen.close()
    return lines

def writeFile(filename,content):
    fopen = open(filename,'w')
    for i in range(len(content)):
        fopen.write(content[i])
        fopen.write('\n')
    fopen.close()

def filter(content):

    for i in  range(len(content)):
        if content[i] < 0x20 or content[i] == 0x7F :
            content[i] = 0x20
    print content


if __name__ == '__main__':
    filePath = "paper/6.txt"
    filePathC = "paper"
    # eachFile(filePathC)
    content = readFile(filePath)
    print content
    for i in content :
        print i
    print '\xe8\xae\xa8\xe8\xae\xba\xe5\x85\xb3\xe4\xba\x8e\xe7\x9f\xa5\xe8\xaf\x86\xe4\xb8\x8e\xe7\x9f\xa5\xe8\xaf\x86\xe6\xb4\xbb\xe5\x8a\xa8\xe7\xa0\x94\xe7\xa9\xb6\xe7\x9a\x84\xe4\xb8\x80\xe9\x97\xa8\xe7\xa7\x91\xe5\xad\xa6\xe2\x80\x94\xe2\x80\x94\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\x9a\x84\xe8\xb5\xb7\xe6\xba\x90\xe5\x92\x8c\xe5\xad\xa6\xe7\xa7\x91\xe5\x9f\xba\xe7\xa1\x80\xef\xbc\x8c\xe5\x88\x86\xe6\x9e\x90\xe4\xbb\x8e\xe7\x9f\xa5\xe8\xaf\x86\xe8\xae\xba\xe5\x88\xb0\xe7\x9f\xa5\xe8\xaf\x86\xe7\xa7\x91\xe5\xad\xa6\xe7\x9a\x84\xe5\x8f\x91\xe5\xb1\x95\xe8\xbf\x87\xe7\xa8\x8b\xef\xbc\x8c\xe6\xa6\x82\xe8\xa6\x81\xe6\x80\xbb\xe7\xbb\x93\xe5\x85\xb3\xe4\xba\x8e\xe7\x9f\xa5\xe8\xaf\x86\xe5\x92\x8c\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\xa0\x94\xe7\xa9\xb6\xe7\x9a\x84\xe7\x8e\xb0\xe7\x8a\xb6;\xe6\x8f\x90\xe5\x87\xba\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe4\xbd\x93\xe7\xb3\xbb\xe9\x87\x8d\xe5\xbb\xba\xe7\x9a\x84\xe6\x80\x9d\xe6\x83\xb3\xef\xbc\x8c\xe6\x8c\x87\xe5\x87\xba21\xe4\xb8\x96\xe7\xba\xaa\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\x9a\x84\xe4\xbd\xbf\xe5\x91\xbd\xe6\x98\xaf\xe4\xb8\xba\xe4\xba\xba\xe7\xb1\xbb\xe7\xa4\xbe\xe4\xbc\x9a\xe7\x9a\x84\xe7\x9f\xa5\xe8\xaf\x86\xe8\xae\xb0\xe5\xbf\x86\xe4\xb8\x8e\xe5\x88\x9b\xe6\x96\xb0\xe6\x8f\x90\xe4\xbe\x9b\xe4\xbf\x9d\xe9\x9a\x9c\xef\xbc\x8c\xe5\xb9\xb6\xe4\xbd\x9c\xe7\x94\xa8\xe4\xba\x8e\xe7\xa7\x91\xe5\xad\xa6\xe6\x8a\x80\xe6\x9c\xaf\xe4\xb8\x8e\xe7\xa4\xbe\xe4\xbc\x9a\xe5\x8f\x91\xe5\xb1\x95;\xe6\x8f\x90\xe5\x87\xba\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\x9a\x84\xe4\xb8\xbb\xe8\xa6\x81\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x92\x8c\xe9\x87\x8d\xe8\xa6\x81\xe7\xa0\x94\xe7\xa9\xb6\xe9\xa2\x86\xe5\x9f\x9f\xef\xbc\x8c\xe5\x8c\x85\xe6\x8b\xac\xe7\xa1\xae\xe7\xab\x8b\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\x9a\x84\xe7\x90\x86\xe8\xae\xba\xe5\x9f\xba\xe7\xa1\x80\xef\xbc\x8c\xe5\xbb\xba\xe7\xab\x8b\xe7\x9f\xa5\xe8\xaf\x86\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x9a\x84\xe7\x90\x86\xe8\xae\xba\xe4\xb8\x8e\xe5\xba\x94\xe7\x94\xa8\xe6\x96\xb9\xe6\xb3\x95\xe4\xbd\x93\xe7\xb3\xbb\xef\xbc\x8c\xe4\xbf\x83\xe8\xbf\x9b\xe7\x9f\xa5\xe8\xaf\x86\xe6\x8a\x80\xe6\x9c\xaf\xe3\x80\x81\xe7\x9f\xa5\xe8\xaf\x86\xe5\xb7\xa5\xe7\xa8\x8b\xe4\xb8\x8e\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe5\x8e\x9f\xe7\x90\x86\xe7\xa0\x94\xe7\xa9\xb6\xe7\xbb\x93\xe5\x90\x88\xef\xbc\x8c\xe6\x9e\x84\xe5\xbb\xba\xe7\x9f\xa5\xe8\xaf\x86\xe5\xad\xa6\xe7\x9a\x84\xe6\x96\xb0\xe5\xad\xa6\xe7\xa7\x91\xe4\xbd\x93\xe7\xb3\xbb\xe3\x80\x82\r'
    print content[3].replace('\r','\r\n')
