#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib
import urllib2

import time


def resolve_redirects(url):
    try:
        return urllib2.urlopen(url).geturl()
    except urllib2.HTTPError, e:
        if e.code == 429:
            print e
            time.sleep(5)
            return resolve_redirects(url)
        raise


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # headers = {'User-Agent': user_agent}
        # data = urllib.urlencode(headers)
        # url = resolve_redirects(url)
        req = urllib2.Request(url)
        response = None

        try:
            response = urllib2.urlopen(req)
            # if response.getcode() != 200:
            #     return None
            return response.read()
        except urllib2.HTTPError, e:
            print e.code
            if e.code == 429:
                print 'sleep 5sec'
                time.sleep(5)
                return self.download(url)
