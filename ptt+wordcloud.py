import re
import requests
import jieba
import pandas as pd
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Discussion():
    def __init__(self):
        self.string_data = None
        self.clean_word = None
        self.wordcount_num = None
        pass
        
    def get_all_href(self,url):
        urlList = []
        res = requests.get(url)
        soup = bs(res.text, "html.parser")
        raw_titles = soup.find_all('div', class_= 'title')
        for item in raw_titles:
            title =  item.a.string
            if title:
                print(title)
                url = 'https://www.ptt.cc' + item.a["href"]
                urlList.append(url)
        return urlList
    
    def crawlerMessage(self,urlList):
        messagesList = []
        for num in range(len(urlList)):
            response = requests.get(urlList[num])
            soup = bs(response.text, 'lxml')
            articles = soup.find_all('div', class_= 'push')

            for article in articles:
                messages = article.find('span', class_ = 'f3 push-content').getText().replace(':', '').strip()
                messagesList.append(messages)
        return messagesList
    
    def crawlerptt(self,url,page,urlList):
        message_all = []
        for page in range(1,page):
            res = requests.get(url)
            soup = bs(res.text, "html.parser")
            nextLink = soup.find("a" , string = "‹ 上頁")
            up_page_href =nextLink["href"]
            next_page_url = 'https://www.ptt.cc' + up_page_href
            url = next_page_url
            urlList = self.get_all_href(url)
            message_all += self.crawlerMessage(urlList)
        return message_all
    
    def clean_data(self,messagesList):
        text = messagesList
        Str = "".join(text) 
        kk=re.sub("\n"," ",Str) #刪除\n
        string_data = kk.replace('[^\w\s]', '').replace('／', "").replace('《', '').replace('》', '').replace('，', '').replace('。', '').replace(
            '「', '').replace('」', '').replace('（', '').replace('）', '').replace('！', '').replace('？', '').replace('、','').replace(
            '▲', '').replace('…', '').replace('：', '').replace(' ','').replace('；','').replace("?"," ").replace(".", " ").replace("!"," ").replace('~',' ').replace(
            '(',' ').replace(")"," ")
        self.string_data = string_data
    def cut_words(self):
        string_data = self.string_data
        jieba.set_dictionary('./package/dict.txt.big.txt')
        sentence = jieba.cut(string_data, cut_all=False) 
        word_list = []
        for i in sentence:
            word_list.append(i)
        stopwords=[]
        for word in open("./package/stopwords.txt","r",encoding="utf-8-sig"):
            stopwords.append(word.strip())
        clean_word=[]
        trash_value = ["沒","會","都"]
        for j in word_list:
            if j not in stopwords and j not in trash_value:
                clean_word.append(j)
        self.clean_word = clean_word
    def wordcount(self):
        clean_word = self.clean_word
        word_count = dict()
        for k in clean_word:
            if k in word_count.keys():
                word_count[k] += 1
            else:
                word_count[k] = 1
        wc_list = pd.DataFrame.from_dict(word_count, orient="index", columns = ["次數"]) #using keys as rows
        wc_list = wc_list.sort_values(by=["次數"],ascending = False)
        wc_list.to_csv("wordcountfile.csv" , encoding="utf-8-sig")
        self.wordcount_num =  word_count  
    
    def wordcloud(self):
        font = "./package/SourceHanSansTW-Regular.otf"
        wc =  WordCloud(background_color="white", width=1000, height=500,
                          font_path=font,scale=1.5,
                        max_words=1500)
        wc.generate_from_frequencies(self.wordcount_num)
        plt.figure(figsize=(100,100))
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
        wc.to_file('word_cloud.png')
        
if __name__ == '__main__':
    url = 'https://www.ptt.cc/bbs/Tech_Job/search?q=%E5%8F%B0%E7%A9%8D%E9%9B%BB'#關鍵字搜尋台積電
    pttmesage = Discussion()
    urlList = pttmesage.get_all_href (url)
    message_firstpage = pttmesage.crawlerMessage(urlList)
    content = pttmesage.crawlerptt(url ,3,urlList)
    messagesList = message_firstpage + content
    pttmesage.clean_data(messagesList)
    pttmesage.cut_words()
    pttmesage.wordcount()
    pttmesage.wordcloud()
    
    
    

















