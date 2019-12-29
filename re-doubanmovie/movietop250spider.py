import requests
from requests.exceptions import RequestException
import re
import json
import time

#获取页面源码
def get_page(start):
    try:
        url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#提取数据
def parse_page(html):
    parse = re.compile('<li>.*?pic.*?"">(.*?)</em>.*?src="(.*?)".*?title">(.*?)</span>.*?"">(.*?)'
                       '<br>.*?(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?age">(.*?)</span>.*?<span>(.*?)</span>.*?'
                       'inq">(.*?)</span>.*?</li>', re.S)
    items = re.findall(parse, html)
    for item in items:
        yield {
            'number': item[0],
            'image': item[1],
            'title': item[2],
            'worker': item[3].replace('\\n'and'&nbsp;', '').strip(),
            'year': item[4].replace('\\n', '').strip(),
            'country': item[5],
            'category': item[6].replace('\\n', '').strip(),
            'score': item[7],
            'appraise': item[8],
            'description': item[9]
        }

#将提取的数据保存为文本文件
def write_to_text(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        print(content)

#分页爬取
def main():
    for i in range(0, 11):
        j = i * 25
        html = get_page(j)
        content = parse_page(html)
        for item in content:
            write_to_text(item)
        time.sleep(1)


if __name__ == '__main__':
    main()

