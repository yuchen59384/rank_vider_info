import scrapy
from scrapy.selector import Selector
from rank.myproject.items import MyprojectItem

class MydomainSpider(scrapy.Spider):
    name = 'myproject'
    # allowed_domains = ['https://www.bilibili.com/v/popular/rank/all']
    # tag=['all','music']
    #     # ,'dance','knowledge','tech','car','life','food','animal','kichiku','fashion','ent','cinephile']
    # start_urls = []
    # for t in tag:
    #     start_urls.append('https://www.bilibili.com/v/popular/rank/'+t)
    # models_urls=[]
    def start_requests(self):
        # tag = ['all']
        tag=['all','music', 'dance', 'knowledge', 'tech', 'car', 'life', 'food', 'animal', 'kichiku', 'fashion',
               'ent', 'cinephile']
        for t in tag:
            url='https://www.bilibili.com/v/popular/rank/'+t
            print(tag)
            yield scrapy.Request(url,callback=self.parse,meta={'t':t})

    def parse(self, response):
        print(response)
        href_=response.xpath('//a[@class="title"]/@href').extract()
        title=response.xpath('//a[@class="title"]/text()').extract()
        play = response.xpath('//span[@class="data-box"]/text()').extract()
        author = response.xpath('//span[@class="data-box up-name"]/text()').extract()
        t = response.meta['t']
        #输出标题、播放量、弹幕数量
        for i in range(0,99):
            item = MyprojectItem()
            item['tag']=t
            item['title'] = title[i]
            item['author']=author[i]
            item['play'] = play[2*i-1]
            item['dm']=play[2*i]
            item['href']=href_[i]
            print(i,':',end='')
            print(title[i])
            print(play[2*i-2],play[2*i-1])
        # self.models_urls=href_
        # for url in self.models_urls:
            yield scrapy.Request('https://'+href_[i], callback=self.parse_detail,meta={'item':item})
    #解析视频页面，获取视频信息
    def parse_detail(self,response):

        dz = response.xpath('//span[@class="like"]/text()').extract_first().replace(" ","")
        tb = response.xpath('//span[@class="coin"]/text()').extract_first().replace(" ","").replace("\n","")
        sc = response.xpath('//span[@class="collect"]/text()').extract_first().replace(" ","")
        fx = response.xpath('//span[@class="share"]/text()').extract_first().replace(" ","")
        # for dz,tb,sc,fx in zip(dz,tb,sc,fx):

        item = response.meta['item']
        item['dz']=dz
        item['tb'] =tb
        item['sc'] =sc
        item['fx'] =fx
        print("点赞数:", dz, "投币数:"+ tb, "\n 收藏数:", sc, "分享数:", fx, '----------------')
        yield item



        # for li in rank_list:
        #     title= li.xpath('./div[2]/div[2]/a').extract()
        #     print(title)


        # print(rank_list)
        # li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')