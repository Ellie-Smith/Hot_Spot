#coding=utf-8
import csv
from os import path
from scipy.misc import imread
from TextRank4ZH.textrank4zh import TextRank4Keyword, TextRank4Sentence
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class papers:

    def __init__(self,filepath):
        self.contents = self.read_csv(filepath)
        self.date = []
        self.title = []
        self.auther = []
        self.keywords = []
        self.abstract = []
        #按时间区分的paper存储结构
        self.hotspot_dict = {}
        # 提取关键词（TextRank）
        tr4w = TextRank4Keyword()

        print "restructing"
        for c in self.contents:
            print '.',
            try:
                self.date.append(int(c[0][0:4]))
            except:
                pass
            self.title.append(c[1])
            self.auther.append(c[2])
            # self.abstract.append(c[3])
            words = jieba.cut(c[3])
            words = deleteStopwords(words)
            self.abstract.append(''.join(words))


            if len(c) < 5:
                self.keywords.extend("")
                if c[0][0:4] not in self.hotspot_dict:
                    self.hotspot_dict[c[0][0:4]] = {'abstracts': c[3], 'keywords': ''}
                else:
                    self.hotspot_dict[c[0][0:4]] = \
                        {'abstracts': c[3] + self.hotspot_dict[c[0][0:4]]['abstracts'],
                         'keywords': self.hotspot_dict[c[0][0:4]]['keywords']}
            else:
                self.keywords.extend(c[4].strip().split(','))
                if c[0][0:4] not in self.hotspot_dict:
                    self.hotspot_dict[c[0][0:4]] = {'abstracts': c[3], 'keywords': ' '.join(c[4].strip().split(','))}
                else:
                    self.hotspot_dict[c[0][0:4]] = \
                        {'abstracts': c[3] + self.hotspot_dict[c[0][0:4]]['abstracts'],
                         'keywords': ' '.join(c[4].strip().split(',')) + ' ' + self.hotspot_dict[c[0][0:4]]['keywords']}


        print "restruct finish!"
        print "extracting phrases"
        self.phrases = []
        for c in self.abstract:
            print '.',

            tr4w.analyze(text=c, lower=True,
                         window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
            for phrase in tr4w.get_keyphrases(keywords_num=20., min_occur_num=2):
                self.phrases.append(phrase)
        print "extract phrases finish!"
        #提取出的短语
        self.phrases.extend(self.keywords)



    def read_csv(self,filename):
        import csv
        csvFile = open(filename, "r")
        reader = csv.reader(csvFile)
        return reader

    #构建词云
    def show_wordcloud(self,words):
        wl_space_split = ' '.join(words)
        d = path.dirname(__file__)
        nana_coloring = imread(path.join(d, "cloud.jpg"))
        # 对分词后的文本生成词云
        my_wordcloud = WordCloud(background_color='white',  # 设置背景颜色
                                 mask=nana_coloring,  # 设置背景图片
                                 max_words=2000,  # 设置最大现实的字数
                                 stopwords=STOPWORDS,  # 设置停用词
                                 max_font_size=50,  # 设置字体最大值
                                 random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                                 )
        # generate word cloud
        my_wordcloud.generate(wl_space_split)
        # create coloring from image
        image_colors = ImageColorGenerator(nana_coloring)
        # recolor wordcloud and show
        my_wordcloud.recolor(color_func=image_colors)
        plt.imshow(my_wordcloud)  # 显示词云图
        plt.axis("off")  # 是否显示x轴、y轴下标
        plt.show()
        # save img
        # my_wordcloud.to_file(path.join(d, "cloudimg.png"))

    #每年收录文献数量统计
    def show_history_numb_paper(self,year,paper_count):
        font_yahei_consolas = FontProperties(fname="huawenfansong.ttf")
        plt.figure(figsize=(12, 10))
        plt.xlim((1980, 2017))
        plt.plot(year, paper_count, "ro-", label="paragraph")
        # plt.bar(range(len(paper_count)),paper_count)
        plt.ylabel("收录文献数量", fontproperties=font_yahei_consolas,
                   fontsize=14)
        plt.xlabel("年份", fontproperties=font_yahei_consolas,
                   fontsize=14)
        plt.title("历史文献收录数折线图", fontproperties=font_yahei_consolas,
                  fontsize=20)
        ## 添加平均值
        plt.hlines(np.mean(paper_count), 1980, 2017, "b")
        plt.show()

    # 计算文档集的tfidf
    def tfidf(self,corpus1):
        corpus = []
        for line in corpus1:
            this_list = []
            for word in jieba.cut(line):
                # try:
                #     word.decode('utf-8')
                # except:
                #     continue
                this_list.append(word)
            this_line = ' '.join(this_list)
            corpus.append(this_line)
        vectorizer = CountVectorizer()
        transformer = TfidfTransformer(norm=u'l2', use_idf=True, smooth_idf=True, sublinear_tf=False)
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
        word = vectorizer.get_feature_names()
        word_dict = {}
        for i in range(len(word)):
            word_dict[str(i)] = word[i]
        weight = tfidf.toarray()
        return word_dict, weight

def getstopwordlist(stopwords):
    stopword_list = []
    lines = stopwords.readlines()
    for line in lines:
        line = line.split()
        for word in line:
            stopword_list.append(word.encode('utf-8'))
    return stopword_list

def deleteStopwords(word_list):
    stopword_list = getstopwordlist(stopwords = open('data/stopwords.csv', 'r'))
    finalwords = [word for word in word_list if word not in stopword_list]
    return finalwords

if __name__ == '__main__':
    paper = papers('data\\yingyongyanjiu.csv')
    for w in paper.phrases:
        jieba.add_word(w)
    wordlist = jieba.cut(' '.join(paper.abstract), cut_all=True)

    phrase_dict = {}
    line = ' '.join(paper.abstract)
    for phrase in paper.phrases:
        phrase_dict[phrase] = line.count(phrase)
    wordlist = []
    for w in phrase_dict.keys():
        for i in range(phrase_dict[w]):
            wordlist.append(w)
    #收录文献热点词云
    paper.show_wordcloud(set(wordlist))

    #历史收录文献数量折线图
    print "counting date"
    date_dict = {}
    for i in paper.date:
        print '.',
        if i not in date_dict:
            date_dict[i] = 1
        else:
            date_dict[i] = date_dict[i] + 1
    keys = [int(year) for year in date_dict.keys()]
    values = [int(count) for count in date_dict.values()]
    paper.show_history_numb_paper(keys,values)

    #历史收录文献热点
    print "finding hot_spot by date"
    # for year in paper.hotspot_dict:
    #     print '.',
    #     hotest = {}
    #     for w in paper.phrases:
    #         if len(w) <= 9:
    #             continue
    #         count = paper.hotspot_dict[year]['abstracts'].count(w)
    #         if count > 0 and w != '':
    #             hotest[w] = count
    #     hotest_words = hotest.items()
    #     hotest_words = sorted(hotest_words,key=lambda item:item[1],reverse=True)
    #     if len(hotest_words) > 2:
    #         print year,hotest_words[0][0],hotest_words[0][1],hotest_words[1][0],hotest_words[1][1],hotest_words[2][0],hotest_words[2][1]
    #     else:
    #         print year,hotest_words
    corpus = [i['abstracts'] for i in paper.hotspot_dict.values()]


    words,tfidf = paper.tfidf(corpus)
    print len(words)
    print len(tfidf[0])

    hot_spot = []
    for k in range(len(paper.hotspot_dict.keys())):
        max_ = 0
        index = 0
        for i in range(len(tfidf[k])):
            if tfidf[k][i] > max_ and len(words[str(i)]) > 3:

                if '结果' in words[str(i)] or '表明' in words[str(i)] or '研究' in words[str(i)] \
                    or '收敛速度' in words[str(i)] or '数据集上' in words[str(i)] or '算法相比' in words[str(i)]\
                        or '体系结构' in words[str(i)]:
                    continue
                else:
                    max_ = tfidf[k][i]
                    index = i

        # print paper.hotspot_dict.keys()[k],words[str(index)],max_
        hot_spot.append([paper.hotspot_dict.keys()[k],words[str(index)],max_])

    hot_spot = sorted(hot_spot,key=lambda item:item[0],reverse=True)
    for i in hot_spot:
        print i[0],i[1],i[2]


