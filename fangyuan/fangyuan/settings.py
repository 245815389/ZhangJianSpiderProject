# -*- coding: utf-8 -*-

# Scrapy settings for fangyuan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fangyuan'

SPIDER_MODULES = ['fangyuan.spiders']
NEWSPIDER_MODULE = 'fangyuan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
# 'cookie': 'acw_tc=ac11000115869659314731971e011054a3c7224ac19658be0fb1ed85f430ab; x-zp-client-id=945fd62f-89fe-428e-bf43-5e921f83aa5f; sajssdk_2015_cross_new_user=1; campusOperateJobUserInfo=c81207cf-5baa-4aef-86ac-ee282a350594; dywea=95841923.4083895301044580000.1586966023.1586966023.1586966023.1; dywec=95841923; dywez=95841923.1586966023.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; __utmz=269921210.1586966023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=269921210; __utma=269921210.1172405248.1586966023.1586966023.1586966023.1; __utmt=1; 1420ba6bb40c9512e9642a1f8c243891=541231b0-4ad8-48f5-b12f-69e24879196c; at=6653f00f48cd47b9a6819ce6f8593548; rt=5b9ade679f4d44ac85bbb676fb5e3035; JSsUserInfo=3D753D685764597549685C645F7540685D645A754D6859645B7542682664267544685B645F7541685F645C754B685B645075406853645C7542683F642675446866300E2E42682B643C7544685E64457548685F6448754B68596452754C6859645375386826645575496851643; JSpUserInfo=3D753D685764597549685C645F7540685D645A754D6859645B7542682664267544685B645F7541685F645C754B685B645075406853645C7542683F642675446866300E2E42682B643C7544685E64457548685F6448754B68596452754C6859645375386826645575496851643; MonUid=53644265516653665D7752754B6F4D754A695164; CheckedIFL=1; dywem=95841923.y; dyweb=95841923.2.10.1586966023; __utmb=269921210.2.10.1586966023; Hm_lvt_d7ede48beea78a2945672aed33b15da7=1586966023,1586966033; Hm_lpvt_d7ede48beea78a2945672aed33b15da7=1586966033; stayTimeCookie=1586966033566; referrerUrl=https%3A//xiaoyuan.zhaopin.com/indexforlogin; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221717e8a6ce0765-040dc1eeaf845d-87f133f-1327104-1717e8a6ce1abc%22%2C%22%24device_id%22%3A%221717e8a6ce0765-040dc1eeaf845d-87f133f-1327104-1717e8a6ce1abc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'fangyuan.middlewares.FangyuanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'fangyuan.middlewares.FangyuanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'fangyuan.pipelines.FangyuanPipeline': 300,
   'fangyuan.pipelines.MonPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
