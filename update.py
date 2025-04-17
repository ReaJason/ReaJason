import requests
from lxml import etree

if __name__ == '__main__':
    domain = "https://reajason.eu.org"
    page_res = requests.get(f"{domain}/writing")
    html = etree.HTML(page_res.text)
    post_list = []
    for li in html.xpath('//main/div[2]/ol/li')[:5]:
        a_tag = li.xpath('.//div//a')
        href = a_tag[0].get('href') if a_tag else None
        title = a_tag[0].text if a_tag else None
        subtitle_p = li.xpath('.//p[1]')
        subtitle = subtitle_p[0].text.strip() if subtitle_p else None
        date_p = li.xpath('.//p[2]')
        date = date_p[0].text.strip() if date_p else None
        post_list.append(f"- [{title} - {subtitle}]({domain}{href})（{date}）")
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(f'''## 👋 Hi there，I'm <a href="https://reajason.eu.org" target="_blank">ReaJason</a>

- 🔥 I'm a programming amateur.
- ❄ I'm learning Java Web Cybersecurity.
- ⚡ I'm working on Java(RASP).
- 📫 Contact me by reajason1225@proton.me.

### Latest Blogs

{'\n'.join(post_list)}
''')