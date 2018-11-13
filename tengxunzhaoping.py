import requests
from lxml import etree

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# 获取待爬取的网页链接
def get_page_urls():
    page_urls = []
    for i in range(1, 285):
        url = "https://hr.tencent.com/position.php?keywords=&tid=0&start=" + str(i) + "0#a"
        page_urls.append(url)
    return page_urls

# 获取每一页的招聘信息列
def get_li_urls(url):
    li_urls = []
    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)
    li = html.xpath("//td[@class='l square']//a/@href")
    for i in li:
        li_urls.append('https://hr.tencent.com/' + i)
    return li_urls

# 获取目标字段
def get_data(li_url):
    response = requests.get(li_url, headers=HEADERS)
    html = etree.HTML(response.text)
    info = {}
    info['title'] = html.xpath('//tr[@class="h"]//td/text()')[0]
    info['place'] = html.xpath('//tr[@class="c bottomline"]//td[1]/text()')[0]
    info['category'] = html.xpath('//tr[@class="c bottomline"]//td[2]/text()')[0]
    info['number'] = html.xpath('//tr[@class="c bottomline"]//td[3]/text()')[0]
    info['duty'] = html.xpath('//tr[@class="c"][1]//td//ul//li/text()')[0]
    info['require'] = html.xpath('//tr[@class="c"][2]//td//ul//li/text()')[0]
    return info

if __name__ == '__main__':
    # 获取页面的招聘列链接
    # page_urls = get_page_urls()
    # for i in map(get_li_urls, page_urls):
    #     print(i)
    print(get_data('https://hr.tencent.com/position_detail.php?id=44303&keywords=&tid=0&lid=0'))