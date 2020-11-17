import requests
from lxml import etree


url = "https://cdn.jsdelivr.net/gh/ReaJason/reajason.github.io@master/archives/index.html"
domain = "https://reajason.top"
page_res = requests.get(url)
html = etree.HTML(page_res.text)
url_list = [f'{domain}{i}' for i in html.xpath('//div[@class="list-group"]/a/@href')]
title_list = html.xpath('//div[@class="list-group"]/a/span/text()')
post_list = [f"- [{post[1]}]({post[0]})" for post in zip(url_list, title_list)]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'''### 👋 Hi there 

I'm a programming amateur. I'd like to make some interesting and practical tools and share some thoughts on my blog.

### 🎨 Latest blogs

''')
    f.write('\n'.join(post_list))
    f.write(f'''

[>>> More]({domain}/archives/)

### 🔰 Statistics 

![ReaJason's GitHub Stats](https://github-readme-stats.vercel.app/api?username=reajason&show_icons=true&theme=tokyonight)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=reajason&layout=compact&theme=tokyonight)
''')