import requests
from lxml import etree


url = "https://raw.fastgit.org/ReaJason/reajason.github.io/master/archives/index.html"
domain = "https://reajason.github.io"
page_res = requests.get(url)
html = etree.HTML(page_res.text)
url_list = [f'{domain}{i}' for i in html.xpath('//div[@class="list-group"]/a/@href')]
print(url_list)
title_list = html.xpath('//div[@class="list-group"]/a/div/text()')
print(title_list)
post_list = [f"- [{post[1]}]({post[0]})" for post in zip(url_list, title_list)]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'''## 👋 Hi there，I'm [ReaJason](https://reajason.top)

- ❄I'm a programming amateur.
- 🔥I'm learning Computer Networking.
- ⚡I'm working on Java.
- 📫contact me by reajason1225@gmail.com

## 🎨 Latest blogs

''')
    f.write('\n'.join(post_list[:3]))
    f.write(f'''

[>>> More]({domain}/archives/)

## 🔰 Statistics

![ReaJason's GitHub Stats](https://github-readme-stats.vercel.app/api?username=reajason&show_icons=true&theme=tokyonight&cache_seconds=1800)
''')