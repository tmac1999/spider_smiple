#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 爬虫调度端

## URL管理器

### 添加新的URL到待爬取集合中
### 判断待添加URL是否在容器中
### 获取待爬取URL
### 判断是否还有待爬取URL
### 将URL从待爬取移动到已爬取

## 网页下载器
### urllib2
### requests

## 网页解析器

### 正则表达式
### html.parser
### BeautifulSoup
### lxml


## 分析目标
### URL格式
### 数据格式
### 网页编码
import abc

import time

import html_parser
import html_downloader
import html_outputer
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()
    @abc.abstractmethod   # 抽象方法？
    def crawGithub(self, url):
        content = self.downloader.download(url)
        self.parser.parseGithub(url,content)


if __name__ == "__main__":
    # root_url = "http://baike.baidu.com/view/21087.htm"
    # obj_spider = SpiderMain()
    # obj_spider.craw(root_url)i
    for i in range(1,100):
        url = 'https://github.com/search?o=desc&p='+str(i) +'&q=android&s=stars&type=Repositories&utf8=%E2%9C%93'
        print '================'+str(i)+'====================='
        obj_spider = SpiderMain()
        obj_spider.crawGithub(url)
        # todo urllib2.HTTPError: HTTP Error 429: Too Many Requests的问题
        if i%5==0:
            time.sleep(10)
            print '=======sleep==========='

