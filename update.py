import requests
from lxml import etree

if __name__ == '__main__':
    domain = "https://reajason.eu.org"
    page_res = requests.get(f"{domain}/writing")
    html = etree.HTML(page_res.text)
    post_list = []
    for li in html.xpath('//main//ul[@class="flex flex-col gap-4"]/li')[:5]:
        a_tag = li.xpath('.//a')[0]
        href = a_tag.get('href')
        title = a_tag.xpath('.//span[1]')[0].text.strip()
        subtitle = a_tag.xpath('.//span[2]')[0].text.strip()
        date = a_tag.xpath('.//span[3]')[0].text.strip()
        post_list.append(f"- [{title} - {subtitle}]({domain}{href})({date})")
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(f'''## 👋 Hi there，I'm <a href="https://reajason.eu.org" target="_blank">ReaJason</a>

- 🔥 I'm a programming amateur.
- ❄ I'm learning Java Web Cybersecurity.
- ⚡ I'm working on Java(RASP).
- 📫 Contact me by reajason1225@proton.me.

### Latest Blogs

{'\n'.join(post_list)}
''')
