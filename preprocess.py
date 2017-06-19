#coding=utf-8

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
import jieba
import csv
import wordcloud_test

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    file_path_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        # print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
        file_path_list.append(child.decode('gbk'))
    return file_path_list

# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    lines = fopen.readlines()
    # for eachLine in lines:
    #     print "读取到得内容如下：", eachLine
    # print fopen.read()
    fopen.close()
    return lines


def load_stopwords(csvName):
    content = []
    csvfile = file(csvName, 'rb')
    reader = csv.reader(csvfile)
    for line in reader:
        if line != []:
            content.append(line[0])
    return content


def writeFile(filename,content):
    fopen = open(filename,'w')
    for i in range(len(content)):
        fopen.write(content[i])
        fopen.write('\n')
    fopen.close()

#构建unigram词频字典
def get_unigramDict(content_list):
    unigram_dict = {}
    for c in content:
        words = [i for i in jieba.cut(c)]
        for w in words:
            if w not in unigram_dict:
                unigram_dict[w] = 1
            else:
                unigram_dict[w] = unigram_dict[w] + 1
    return unigram_dict

#构建bigram二元词频字典
def get_bigramDict(content_list,unigram_dict):
    bigram_dict = {}
    for d in unigram_dict.keys():
        bigram_dict[d] = {}
    for c in content:
        words = [i for i in jieba.cut(c)]
        for w in range(len(words) - 1):
            if words[w + 1] not in bigram_dict[words[w]]:
                bigram_dict[words[w]][words[w + 1]] = 1
            else:
                bigram_dict[words[w]][words[w + 1]] = bigram_dict[words[w]][words[w + 1]] + 1
    return bigram_dict

def write_csv(filename,content):
    # 文件头，一般就是数据名
    fileHeader = ["date", "title","authers","abstract","keywords"]

    # 写入数据
    csvFile = open(filename, "w")
    writer = csv.writer(csvFile)
    # 写入的内容都是以列表的形式传入函数
    writer.writerow(fileHeader)
    for line in content:
        writer.writerow(line)
    csvFile.close()

def read_csv(filename):
    import csv
    csvFile = open(filename, "r")
    reader = csv.reader(csvFile)
    return reader

def getstopwordlist(stopwords):
    stopword_list = []
    lines = stopwords.readlines()
    for line in lines:
        line = line.split()
        for word in line:
            stopword_list.append(word)
    return stopword_list

def deleteStopwords(word_list,stopwords):
    finalwords = [word for word in word_list if word not in stopwords]
    return finalwords

if __name__ == '__main__':
    # filePath = "paper/10.txt"
    # filePathC = "paper"
    # file_list = eachFile(filePathC)
    # count = 0
    # for file in file_list:
    #     content = readFile(file)
    #     content[3] = content[3].replace('\r','\r\n')
    #     for i in range(len(content)):
    #         content[i] = content[i].replace('\r\n','\n')
    #     writeFile(file,content)
    #     print count
    #     count += 1

    # stopwords = load_stopwords('stopwords.csv')

    date = []
    title = []
    auther = []
    keywords = []
    content = []

    cs = read_csv('paper.csv')
    for c in cs:
        date.append(c[0])
        title.append(c[1])
        auther.append(c[2])
        content.append(c[3])
        keywords.extend(c[4].strip().split(','))

    print len(keywords)



    unigram_dict = get_unigramDict(content_list=content)
    content_words = set(unigram_dict.keys())

    bigram_dict = get_bigramDict(content_list=content,unigram_dict=unigram_dict)

    print unigram_dict
    print bigram_dict



    multiwords = []
    threshold = 0.7
    count = 0
    for c in content:
        print count
        words = [i for i in jieba.cut(c)]
        for w in range(len(words) - 1):
            uni = max(unigram_dict[words[w]],unigram_dict[words[w+1]])
            bi = 1
            if words[w+1] in bigram_dict[words[w]] and words[w+1] not in stopwords and words[w] not in stopwords:
                bi = bigram_dict[words[w]][words[w+1]]
            score = bi*1.0/uni
            if score > threshold:
                multiwords.append(words[w]+words[w+1])
        count += 1

    multiwords = set(multiwords)

    for i in multiwords:
        print i
    print len(multiwords)


    # from TextRank4ZH.textrank4zh import TextRank4Keyword, TextRank4Sentence
    #
    # phrases = []
    # for c in content:
    #     # 提取关键词（TextRank）
    #     tr4w = TextRank4Keyword()
    #     tr4w.analyze(text=c, lower=True,
    #                  window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
    #     keyword_list = []
    #     # print('关键词：')
    #     # 这里设置提取的关键词数量，现在设置为30个
    #     # for item in tr4w.get_keywords(30, word_min_len=1):
    #     #     keyword_list.append(item.word)
    #     #     print "关键词:  ",item.word
    #
    #     for phrase in tr4w.get_keyphrases(keywords_num=20.,min_occur_num=2):
    #         phrases.append(phrase)
    #
    # phrases.extend(keywords)
    # # testwc2.show_wordcloud(' '.join(phrases))
    # for w in phrases:
    #     jieba.add_word(w)

    # wordcloud_test.show_wordcloud(' '.join(content))



