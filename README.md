豆瓣电影TOP250爬虫

爬虫说明：该爬虫使用requests去获取豆瓣网站的页面， 然后使用正则表达式去提取页面源码的数据，分别提取了排名号，电影海报图片链接， 电影名称， 导演和主演， 年份， 国家，
类型， 评分， 评价人数等一些信息，然后使用json结构化这些数据并保存到文本文件result.txt中，而且还进行分页爬取所有top250的所有电影信息。

使用的技术：requests ，伪装请求头， 正则表达式， json等等。