from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://movie.douban.com/subject/1292052/")
titile = r.html.find('#content',first=True)

print(titile.text)