#coding=utf-8
from os import path
from scipy.misc import imread
import jieba
import sys
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS



def show_wordcloud(content):

    #结巴分词 cut_all=True 设置为全模式
    wordlist = jieba.cut(content, cut_all = True)


    #使用空格连接 进行中文分词
    wl_space_split = " ".join(wordlist)
    # wl_space_split = content

    # 读取mask/color图片
    d = path.dirname(__file__)
    nana_coloring = imread(path.join(d, "luffy.jpg"))

    # 对分词后的文本生成词云
    my_wordcloud = WordCloud( background_color = 'white',      # 设置背景颜色
                                mask = nana_coloring,          # 设置背景图片
                                max_words = 2000,              # 设置最大现实的字数
                                stopwords = STOPWORDS,         # 设置停用词
                                max_font_size = 50,            # 设置字体最大值
                                random_state = 30,             # 设置有多少种随机生成状态，即有多少种配色方案
                                )
    # generate word cloud
    my_wordcloud.generate(wl_space_split)

    # create coloring from image
    image_colors = ImageColorGenerator(nana_coloring)

    # recolor wordcloud and show
    my_wordcloud.recolor(color_func=image_colors)

    plt.imshow(my_wordcloud)    # 显示词云图
    plt.axis("off")             # 是否显示x轴、y轴下标
    plt.show()
    # save img
    # my_wordcloud.to_file(path.join(d, "cloudimg.png"))

#打开本体TXT文件
# text = open(u'test.txt').read()
# show_wordcloud(text)

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

def deleteStopwords(word_list):
    stopword_list = getstopwordlist(stopwords = open('data/stopwords.csv', 'r'))
    finalwords = [word for word in word_list if word not in stopword_list]
    return finalwords

if __name__ == '__main__':
    # data = [5, 20, 15, 25, 10]
    #
    # plt.bar(range(len(data)), data)
    # plt.show()
    if '结果' in '结果表明':
        print 1